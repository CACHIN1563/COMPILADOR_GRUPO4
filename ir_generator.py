from llvmlite import ir
from Gramatica_v3Visitor import Gramatica_v3Visitor

class IRGenerator(Gramatica_v3Visitor):

    def __init__(self):
        self.module = ir.Module(name="compilador_grupo4_v3")
        self.int_type = ir.IntType(32)
        self.void_type = ir.VoidType()

        func_type = ir.FunctionType(self.int_type, [])
        self.main_func = ir.Function(self.module, func_type, name="main")
        block = self.main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        self.variables = {}

        self.printf = ir.Function(
            self.module,
            ir.FunctionType(
                ir.IntType(32),
                [ir.PointerType(ir.IntType(8))],
                var_arg=True
            ),
            name="printf"
        )

        formato = "%d\n\0"
        self.formato_print = ir.GlobalVariable(
            self.module,
            ir.ArrayType(ir.IntType(8), len(formato)),
            name="formato_int"
        )
        self.formato_print.global_constant = True
        self.formato_print.initializer = ir.Constant(
            ir.ArrayType(ir.IntType(8), len(formato)),
            bytearray(formato.encode("utf8"))
        )

    def visitSentenciaImprimirG4(self, ctx):
        valor = self.visit(ctx.impresion().expr())

        formato_ptr = self.builder.bitcast(
            self.formato_print,
            ir.PointerType(ir.IntType(8))
        )

        self.builder.call(self.printf, [formato_ptr, valor])
        return None

    def visitVarArrayDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        valores = ctx.arrayLiteral().expr()
        size = len(valores)

        array_type = ir.ArrayType(self.int_type, size)
        ptr = self.builder.alloca(array_type, name=nombre)
        self.variables[nombre] = {
            "ptr": ptr,
            "size": size,
            "type": "array"
        }

        for i, expr in enumerate(valores):
            valor = self.visit(expr)
            elem_ptr = self.builder.gep(
                ptr,
                [
                    ir.Constant(self.int_type, 0),
                    ir.Constant(self.int_type, i)
                ],
                name=f"{nombre}_{i}_ptr"
            )
            self.builder.store(valor, elem_ptr)

        return ptr

    def visitExprArrayAccessG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        indice_texto = ctx.expr().getText()

        if not indice_texto.isdigit():
            return ir.Constant(self.int_type, 0)

        indice = int(indice_texto)
        info = self.variables[nombre]

        elem_ptr = self.builder.gep(
            info["ptr"],
            [
                ir.Constant(self.int_type, 0),
                ir.Constant(self.int_type, indice)
            ],
            name=f"{nombre}_{indice}_access"
        )

        return self.builder.load(elem_ptr, name=f"{nombre}_{indice}")

    def get_ir(self):
        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.int_type, 0))
        return str(self.module)

    def visitProgramG4(self, ctx):
        for d in ctx.declaration():
            self.visit(d)
        return None

    def visitVarDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        ptr = self.builder.alloca(self.int_type, name=nombre)
        self.variables[nombre] = ptr

        if ctx.expr():
            valor = self.visit(ctx.expr())
        else:
            valor = ir.Constant(self.int_type, 0)

        self.builder.store(valor, ptr)
        return ptr

    def visitExprLiteralNumericaG4(self, ctx):
        return ir.Constant(self.int_type, int(ctx.getText()))

    def visitExprReferenciaVariableG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        info = self.variables[nombre]

        if isinstance(info, dict):
            return ir.Constant(self.int_type, 0)

        return self.builder.load(info, name=nombre)

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