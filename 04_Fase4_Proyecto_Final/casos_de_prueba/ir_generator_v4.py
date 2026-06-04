from llvmlite import ir
from gramatica_v4Visitor import gramatica_v4Visitor

class IRGeneratorV4(gramatica_v4Visitor):
    def __init__(self, target_triple=None):
        self.module = ir.Module(name="compilador_grupo4_v4")
        if target_triple:
            self.module.triple = target_triple

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
        self.fmt_float = self.add_global_string("%f\n\0", "fmt_float")
        self.fmt_str = self.add_global_string("%s\n\0", "fmt_str")

        # Main function
        func_type = ir.FunctionType(self.int_type, [])
        self.main_func = ir.Function(self.module, func_type, name="main")
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        self.variables = {}
        self.loop_stack = [] # (cond_block, end_block) o (None, end_block) para switch
        
        # Struct definitions: name -> {'type': ir.LiteralStructType, 'fields': {name: index}}
        self.struct_defs = {}

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

    def get_llvm_type(self, type_str):
        if type_str in ["int", "INT"]: return self.int_type
        if type_str in ["float", "FLOAT"]: return self.float_type
        if type_str in ["bool", "BOOL"]: return self.bool_type
        if type_str in ["string", "STRING"]: return ir.IntType(8).as_pointer()
        if type_str.startswith("struct:"):
            struct_name = type_str.split(":")[1]
            return self.struct_defs[struct_name]['type']
        return self.int_type

    # =====================================================
    # PROGRAMA
    # =====================================================
    def visitProgramG4(self, ctx):
        for d in ctx.declaration():
            self.visit(d)
        return None

    def visitDeclStructG4(self, ctx):
        struct_name = ctx.structDeclaration().TK_ID().getText()
        fields_map = {}
        types_list = []
        
        idx = 0
        for field in ctx.structDeclaration().structField():
            type_str = field.type_().getText()
            field_name = field.TK_ID().getText()
            fields_map[field_name] = idx
            types_list.append(self.get_llvm_type(type_str))
            idx += 1
            
        struct_type = ir.LiteralStructType(types_list)
        self.struct_defs[struct_name] = {
            'type': struct_type,
            'fields': fields_map
        }
        return None

    # =====================================================
    # VARIABLES
    # =====================================================
    def visitVarDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        tipo_str = ctx.type_().getText()
        
        if tipo_str in self.struct_defs:
            llvm_type = self.struct_defs[tipo_str]['type']
        else:
            llvm_type = self.get_llvm_type(tipo_str)
            
        ptr = self.builder.alloca(llvm_type, name=nombre)
        self.variables[nombre] = { 'ptr': ptr, 'type_str': tipo_str }

        if ctx.expr():
            valor = self.visit(ctx.expr())
            # Basic auto-cast for literal assignment
            if llvm_type == self.float_type and valor.type == self.int_type:
                valor = self.builder.sitofp(valor, self.float_type)
            self.builder.store(valor, ptr)
        else:
            # Init con 0 para primitivos (simplificado)
            if llvm_type == self.int_type:
                self.builder.store(ir.Constant(self.int_type, 0), ptr)
            elif llvm_type == self.float_type:
                self.builder.store(ir.Constant(self.float_type, 0.0), ptr)

        return ptr

    def visitVarArrayDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        exprs = ctx.arrayLiteral().expr()
        size = len(exprs)
        
        array_type = ir.ArrayType(self.int_type, size)
        ptr = self.builder.alloca(array_type, name=nombre)
        self.variables[nombre] = { 'ptr': ptr, 'type_str': 'int[]' }

        for i, e in enumerate(exprs):
            val = self.visit(e)
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
        val = ctx.getText()[1:-1] + "\0"
        ptr = self.add_global_string(val, "str_lit")
        # cast array pointer to i8*
        return self.builder.bitcast(ptr, ir.IntType(8).as_pointer())

    def visitExprLiteralBoolG4(self, ctx):
        val = ctx.getText().lower()
        return ir.Constant(self.bool_type, 1 if val == "true" else 0)

    def visitExprReferenciaVariableG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        ptr = self.variables[nombre]['ptr']
        return self.builder.load(ptr, name=nombre)

    def visitExprArrayAccessG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        ptr = self.variables[nombre]['ptr']
        idx = self.visit(ctx.expr())
        idx_ptr = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), idx])
        return self.builder.load(idx_ptr)

    def get_struct_field_ptr(self, ctx, lvalue_ctx):
        ids = lvalue_ctx.TK_ID()
        base_name = ids[0].getText()
        var_info = self.variables[base_name]
        ptr = var_info['ptr']
        current_type_str = var_info['type_str']
        
        for i in range(1, len(ids)):
            field_name = ids[i].getText()
            struct_info = self.struct_defs[current_type_str]
            field_idx = struct_info['fields'][field_name]
            
            ptr = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), ir.Constant(self.int_type, field_idx)])
            
            # En v4 simplificado no soportamos structs anidados en la semántica, 
            # pero aquí se podría actualizar current_type_str si lo hiciéramos.
            
        return ptr

    def visitExprAccesoCampoG4(self, ctx):
        base_expr = ctx.expr()
        if hasattr(base_expr, 'TK_ID') and len(base_expr.TK_ID()) > 0:
            pass # No manejado dinámicamente, requiere parser de lvalue
            
        # Simplificación: si es un acceso p.x, ctx.expr() es una ReferenciaVariable
        # En la gramática: expr TK_PUNTO TK_ID
        if base_expr.__class__.__name__ == "ExprReferenciaVariableG4Context":
            base_name = base_expr.TK_ID().getText()
            var_info = self.variables[base_name]
            ptr = var_info['ptr']
            struct_info = self.struct_defs[var_info['type_str']]
            field_name = ctx.TK_ID().getText()
            field_idx = struct_info['fields'][field_name]
            
            idx_ptr = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), ir.Constant(self.int_type, field_idx)])
            return self.builder.load(idx_ptr)
        
        return ir.Constant(self.int_type, 0) # Fallback seguro

    def visitExprCastingG4(self, ctx):
        target_type_str = ctx.type_().getText()
        val = self.visit(ctx.expr())
        
        if target_type_str in ["float", "FLOAT"]:
            if val.type == self.int_type:
                return self.builder.sitofp(val, self.float_type)
        elif target_type_str in ["int", "INT"]:
            if val.type == self.float_type:
                return self.builder.fptosi(val, self.int_type)
        return val

    def visitExprTernarioG4(self, ctx):
        cond = self.visit(ctx.expr(0))
        true_val = self.visit(ctx.expr(1))
        false_val = self.visit(ctx.expr(2))
        
        # Casting automático en ternario si difieren
        if true_val.type == self.float_type and false_val.type == self.int_type:
            false_val = self.builder.sitofp(false_val, self.float_type)
        elif true_val.type == self.int_type and false_val.type == self.float_type:
            true_val = self.builder.sitofp(true_val, self.float_type)
            
        return self.builder.select(cond, true_val, false_val)

    # =====================================================
    # OPERACIONES
    # =====================================================
    def visitExprAritmeticaSumaResG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        
        # Auto-cast
        is_float = (l.type == self.float_type or r.type == self.float_type)
        if is_float:
            if l.type == self.int_type: l = self.builder.sitofp(l, self.float_type)
            if r.type == self.int_type: r = self.builder.sitofp(r, self.float_type)

        if ctx.TK_SUMA():
            return self.builder.fadd(l, r) if is_float else self.builder.add(l, r)
        return self.builder.fsub(l, r) if is_float else self.builder.sub(l, r)

    def visitExprAritmeticaMultDivModG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        texto = ctx.getText()

        is_float = (l.type == self.float_type or r.type == self.float_type)
        if is_float:
            if l.type == self.int_type: l = self.builder.sitofp(l, self.float_type)
            if r.type == self.int_type: r = self.builder.sitofp(r, self.float_type)

        if "*" in texto:
            return self.builder.fmul(l, r) if is_float else self.builder.mul(l, r)
        if "/" in texto:
            return self.builder.fdiv(l, r) if is_float else self.builder.sdiv(l, r)
        if "%" in texto:
            return self.builder.frem(l, r) if is_float else self.builder.srem(l, r)

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

    def visitSentenciaSwitchG4(self, ctx):
        cond_val = self.visit(ctx.switchStatement().expr())
        
        end_block = self.builder.append_basic_block("switch_end")
        
        has_default = ctx.switchStatement().defaultStatement() is not None
        default_block = self.builder.append_basic_block("switch_default") if has_default else end_block
        
        switch_inst = self.builder.switch(cond_val, default_block)
        
        self.loop_stack.append((None, end_block))
        
        # Collect and add cases
        for case in ctx.switchStatement().caseStatement():
            case_val = self.visit(case.expr())
            case_block = self.builder.append_basic_block("switch_case")
            switch_inst.add_case(case_val, case_block)
            
            self.builder.position_at_end(case_block)
            for inst in case.instruccion():
                self.visit(inst)
            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)
                
        if has_default:
            self.builder.position_at_end(default_block)
            for inst in ctx.switchStatement().defaultStatement().instruccion():
                self.visit(inst)
            if not self.builder.block.is_terminated:
                self.builder.branch(end_block)
                
        self.builder.position_at_end(end_block)
        self.loop_stack.pop()

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

    def visitSentenciaForG4(self, ctx):
        if ctx.bucle_for().init_var:
            self.visit(ctx.bucle_for().init_var)
        elif ctx.bucle_for().init_assign:
            self.visit(ctx.bucle_for().init_assign)

        cond_block = self.builder.append_basic_block("for_cond")
        body_block = self.builder.append_basic_block("for_body")
        update_block = self.builder.append_basic_block("for_update")
        end_block = self.builder.append_basic_block("for_end")

        self.loop_stack.append((update_block, end_block))

        self.builder.branch(cond_block)
        self.builder.position_at_start(cond_block)
        
        if ctx.bucle_for().cond:
            cond = self.visit(ctx.bucle_for().cond)
            self.builder.cbranch(cond, body_block, end_block)
        else:
            self.builder.branch(body_block)

        self.builder.position_at_start(body_block)
        self.visit(ctx.bucle_for().bloque())
        if not self.builder.block.is_terminated:
            self.builder.branch(update_block)

        self.builder.position_at_start(update_block)
        if ctx.bucle_for().update_assign:
            self.visit(ctx.bucle_for().update_assign)
        elif ctx.bucle_for().update_expr:
            self.visit(ctx.bucle_for().update_expr)
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
            if cond_block: # for switch, cond_block is None
                self.builder.branch(cond_block)

    # =====================================================
    # COMPARACIONES
    # =====================================================
    def visitExprRelacionalCompG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        is_float = (l.type == self.float_type or r.type == self.float_type)
        if is_float:
            if l.type == self.int_type: l = self.builder.sitofp(l, self.float_type)
            if r.type == self.int_type: r = self.builder.sitofp(r, self.float_type)
            return self.builder.fcmp_ordered(op, l, r)
        return self.builder.icmp_signed(op, l, r)

    def visitExprRelacionalIgualdadG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        
        is_float = (l.type == self.float_type or r.type == self.float_type)
        if is_float:
            if l.type == self.int_type: l = self.builder.sitofp(l, self.float_type)
            if r.type == self.int_type: r = self.builder.sitofp(r, self.float_type)
            if op == "==": return self.builder.fcmp_ordered("==", l, r)
            return self.builder.fcmp_ordered("!=", l, r)

        if op == "==": op = "=="
        elif op == "!=" or op == "<>": op = "!="
        return self.builder.icmp_signed(op, l, r)

    # =====================================================
    # IMPRIMIR
    # =====================================================
    def visitSentenciaImprimirG4(self, ctx):
        val = self.visit(ctx.impresion().expr())
        
        voidptr_ty = ir.IntType(8).as_pointer()
        if val.type == self.float_type:
            # llvm printf for float uses double
            val_double = self.builder.fpext(val, ir.DoubleType())
            fmt_ptr = self.builder.bitcast(self.fmt_float, voidptr_ty)
            self.builder.call(self.printf, [fmt_ptr, val_double])
        elif val.type == self.int_type:
            fmt_ptr = self.builder.bitcast(self.fmt_int, voidptr_ty)
            self.builder.call(self.printf, [fmt_ptr, val])
        else: # string
            self.builder.call(self.printf, [self.fmt_str, val])

    def visitAsignacionVariableG4(self, ctx):
        self.visit(ctx.asignacion_core())

    def visitAsignacionCoreG4(self, ctx):
        lvalue = ctx.lvalue()
        val = self.visit(ctx.expr())
        
        # resolver ptr del lvalue
        ptr = self.get_lvalue_ptr(ctx, lvalue)
        
        if ptr.type.pointee == self.float_type and val.type == self.int_type:
            val = self.builder.sitofp(val, self.float_type)
            
        self.builder.store(val, ptr)
        return val

    def get_lvalue_ptr(self, ctx, lvalue_ctx):
        ids = lvalue_ctx.TK_ID()
        base_name = ids[0].getText()
        var_info = self.variables[base_name]
        ptr = var_info['ptr']
        current_type_str = var_info['type_str']
        
        for i in range(1, len(ids)):
            field_name = ids[i].getText()
            struct_info = self.struct_defs[current_type_str]
            field_idx = struct_info['fields'][field_name]
            ptr = self.builder.gep(ptr, [ir.Constant(self.int_type, 0), ir.Constant(self.int_type, field_idx)])
            
        return ptr

    def visitSentenciaReturnG4(self, ctx):
        if ctx.expr():
            val = self.visit(ctx.expr())
            self.builder.ret(val)
        else:
            self.builder.ret_void()
