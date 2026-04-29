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
        ptr = self.variables[nombre]
        return self.builder.load(ptr, name=nombre)

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