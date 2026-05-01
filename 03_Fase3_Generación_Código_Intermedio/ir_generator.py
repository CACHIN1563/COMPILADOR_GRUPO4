from llvmlite import ir
from Gramatica_v3Visitor import Gramatica_v3Visitor

class IRGenerator(Gramatica_v3Visitor):
    def __init__(self):
        self.module = ir.Module(name="compilador_grupo4_v3")
        self.int_type = ir.IntType(32)
        self.float_type = ir.FloatType()
        self.bool_type = ir.IntType(1)
        self.void_type = ir.VoidType()

        # External printf
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

        # Global format strings
        self.fmt_int = self.add_global_string("%d\n\0", "fmt_int")
        self.fmt_str = self.add_global_string("%s\n\0", "fmt_str")

        # Main function
        func_type = ir.FunctionType(self.int_type, [])
        self.main_func = ir.Function(self.module, func_type, name="main")
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        self.variables = {}
        self.loop_stack = [] # (cond_block, end_block)

    def add_global_string(self, val, name):
        fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(val)), bytearray(val.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, fmt.type, name=name)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = fmt
        return global_fmt

    def get_ir(self):
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))
        return str(self.module)

    # =====================================================
    # PROGRAMA
    # =====================================================
    def visitProgramG4(self, ctx):
        for d in ctx.declaration():
            self.visit(d)
        return None

    # =====================================================
    # VARIABLES
    # =====================================================
    def visitVarDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        # Por simplicidad, todo es Int32 en este generador básico
        ptr = self.builder.alloca(self.int_type, name=nombre)
        self.variables[nombre] = ptr

        if ctx.expr():
            valor = self.visit(ctx.expr())
        else:
            valor = ir.Constant(self.int_type, 0)

        self.builder.store(valor, ptr)
        return ptr

    def visitVarArrayDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        exprs = ctx.arrayLiteral().expr()
        size = len(exprs)
        
        array_type = ir.ArrayType(self.int_type, size)
        ptr = self.builder.alloca(array_type, name=nombre)
        self.variables[nombre] = ptr

        for i, e in enumerate(exprs):
            val = self.visit(e)
            # index = [0, i]
            idx_ptr = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), ir.Constant(self.int_type, i)])
            self.builder.store(val, idx_ptr)
        
        return ptr

    # =====================================================
    # EXPRESIONES
    # =====================================================
    def visitExprLiteralNumericaG4(self, ctx):
        val = ctx.getText()
        if "." in val:
            return ir.Constant(self.float_type, float(val))
        return ir.Constant(self.int_type, int(val))

    def visitExprLiteralCadenaG4(self, ctx):
        # LLVM IR strings are complex. Returning a pointer to a global string.
        val = ctx.getText()[1:-1] + "\0"
        return self.add_global_string(val, "str_lit")

    def visitExprLiteralBoolG4(self, ctx):
        val = ctx.getText().lower()
        return ir.Constant(self.bool_type, 1 if val == "true" else 0)

    def visitExprReferenciaVariableG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        ptr = self.variables[nombre]
        return self.builder.load(ptr, name=nombre)

    def visitExprArrayAccessG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        ptr = self.variables[nombre]
        idx = self.visit(ctx.expr())
        
        idx_ptr = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), idx])
        return self.builder.load(idx_ptr)

    # =====================================================
    # OPERACIONES
    # =====================================================
    def visitExprAritmeticaSumaResG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if ctx.TK_SUMA():
            return self.builder.add(l, r, name="addtmp")
        return self.builder.sub(l, r, name="subtmp")

    def visitExprAritmeticaMultDivModG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        texto = ctx.getText()

        if "*" in texto:
            return self.builder.mul(l, r, name="multmp")
        if "/" in texto:
            return self.builder.sdiv(l, r, name="divtmp")
        if "%" in texto:
            return self.builder.srem(l, r, name="modtmp")

        return ir.Constant(self.int_type, 0)

    # =====================================================
    # CONTROL DE FLUJO
    # =====================================================
    def visitSentenciaIfElseG4(self, ctx):
        cond = self.visit(ctx.condicional().expr())
        
        with self.builder.if_else(cond) as (then, otherwise):
            with then:
                self.visit(ctx.condicional().bloque(0))
            with otherwise:
                if ctx.condicional().bloque(1):
                    self.visit(ctx.condicional().bloque(1))

    def visitSentenciaMientrasG4(self, ctx):
        cond_block = self.builder.append_basic_block("while_cond")
        body_block = self.builder.append_basic_block("while_body")
        end_block = self.builder.append_basic_block("while_end")

        self.loop_stack.append((cond_block, end_block))

        self.builder.branch(cond_block)
        self.builder.position_at_start(cond_block)
        
        cond = self.visit(ctx.bucle_mientras().expr())
        self.builder.cbranch(cond, body_block, end_block)

        self.builder.position_at_start(body_block)
        self.visit(ctx.bucle_mientras().bloque())
        if not self.builder.block.is_terminated:
            self.builder.branch(cond_block)

        self.builder.position_at_start(end_block)
        self.loop_stack.pop()

    def visitSentenciaBreakG4(self, ctx):
        if self.loop_stack:
            _, end_block = self.loop_stack[-1]
            self.builder.branch(end_block)

    def visitSentenciaContinueG4(self, ctx):
        if self.loop_stack:
            cond_block, _ = self.loop_stack[-1]
            self.builder.branch(cond_block)

    # =====================================================
    # COMPARACIONES
    # =====================================================
    def visitExprRelacionalCompG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        return self.builder.icmp_signed(op, l, r, name="cmptmp")

    def visitExprRelacionalIgualdadG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        if op == "==": op = "=="
        elif op == "!=" or op == "<>": op = "!="
        return self.builder.icmp_signed(op, l, r, name="eqtmp")

    # =====================================================
    # IMPRIMIR
    # =====================================================
    def visitSentenciaImprimirG4(self, ctx):
        val = self.visit(ctx.impresion().expr())
        
        # Asumiendo Int32 para el ejemplo simple
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt_ptr = self.builder.bitcast(self.fmt_int, voidptr_ty)
        self.builder.call(self.printf, [fmt_ptr, val])

    def visitAsignacionVariableG4(self, ctx):
        self.visit(ctx.asignacion_core())

    def visitAsignacionCoreG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        val = self.visit(ctx.expr())
        ptr = self.variables[nombre]
        self.builder.store(val, ptr)
        return val

    def visitSentenciaReturnG4(self, ctx):
        if ctx.expr():
            val = self.visit(ctx.expr())
            self.builder.ret(val)
        else:
            self.builder.ret_void()