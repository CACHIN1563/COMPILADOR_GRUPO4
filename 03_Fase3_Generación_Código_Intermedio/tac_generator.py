# =================================================================
# GENERADOR DE CÓDIGO INTERMEDIO (TAC) - FASE 3
# =================================================================

from Gramatica_v3Visitor import Gramatica_v3Visitor

class TACGenerator(Gramatica_v3Visitor):

    def __init__(self):
        self.temp_count = 0
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def emit(self, instruccion):
        self.code.append(instruccion)

    def get_code(self):
        return self.code

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

        if ctx.expr():
            val = self.visit(ctx.expr())
            self.emit(f"{nombre} = {val}")
        else:
            self.emit(f"{nombre} = 0")

    def visitVarArrayDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        valores = []

        for e in ctx.arrayLiteral().expr():
            valores.append(str(self.visit(e)))

        self.emit(f"{nombre} = [{', '.join(valores)}]")

    # =====================================================
    # EXPRESIONES
    # =====================================================
    def visitExprLiteralNumericaG4(self, ctx):
        return ctx.getText()

    def visitExprLiteralCadenaG4(self, ctx):
        return ctx.getText()

    def visitExprLiteralBoolG4(self, ctx):
        return ctx.getText()

    def visitExprReferenciaVariableG4(self, ctx):
        return ctx.TK_ID().getText()

    def visitExprArrayAccessG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        idx = self.visit(ctx.expr())
        temp = self.new_temp()
        self.emit(f"{temp} = {nombre}[{idx}]")
        return temp

    # =====================================================
    # OPERACIONES
    # =====================================================
    def visitExprAritmeticaSumaResG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        temp = self.new_temp()

        if ctx.TK_SUMA():
            self.emit(f"{temp} = {l} + {r}")
        else:
            self.emit(f"{temp} = {l} - {r}")

        return temp

    def visitExprAritmeticaMultDivModG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        temp = self.new_temp()
        texto = ctx.getText()

        if "*" in texto:
            self.emit(f"{temp} = {l} * {r}")
        elif "/" in texto:
            self.emit(f"{temp} = {l} / {r}")
        elif "%" in texto:
            self.emit(f"{temp} = {l} % {r}")

        return temp

    # =====================================================
    # IMPRIMIR
    # =====================================================
    def visitSentenciaImprimirG4(self, ctx):
        val = self.visit(ctx.impresion().expr())
        self.emit(f"print {val}")