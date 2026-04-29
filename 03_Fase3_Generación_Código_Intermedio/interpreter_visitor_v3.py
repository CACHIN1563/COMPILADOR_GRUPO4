from Gramatica_v3Visitor import Gramatica_v3Visitor
from Gramatica_v3Parser import Gramatica_v3Parser
from symbol_table import SymbolTable
import math

class InterpreterVisitorV3(Gramatica_v3Visitor):

    def __init__(self):
        self.tabla_simbolos = SymbolTable()

    def visitProgramG4(self, ctx):
        for d in ctx.declaration():
            self.visit(d)
        return None

    def visitVarDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        valor = None

        if ctx.expr():
            valor = self.visit(ctx.expr())

        self.tabla_simbolos.declare(nombre, "dynamic", valor=valor)
        return valor

    def visitVarArrayDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        valores = []

        for e in ctx.arrayLiteral().expr():
            valores.append(self.visit(e))

        self.tabla_simbolos.declare(nombre, "int[]", valor=valores)
        return valores

    def visitExprArrayAccessG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        indice = self.visit(ctx.expr())

        simbolo = self.tabla_simbolos.lookup(nombre)

        if simbolo is None:
            raise Exception(f"Array '{nombre}' no existe")

        valores = simbolo["value"]

        if indice < 0 or indice >= len(valores):
            raise Exception(f"Índice fuera de rango en array '{nombre}'")

        return valores[indice]

    def visitAsignacionCoreG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        valor = self.visit(ctx.expr())
        self.tabla_simbolos.update_value(nombre, valor)
        return valor

    def visitAsignacionVariableG4(self, ctx):
        return self.visit(ctx.asignacion_core())

    def visitSentenciaImprimirG4(self, ctx):
        valor = self.visit(ctx.impresion().expr())

        if valor is True:
            print("true")
        elif valor is False:
            print("false")
        else:
            print(valor)

        return None

    def visitExprLiteralNumericaG4(self, ctx):
        txt = ctx.getText()
        return float(txt) if "." in txt else int(txt)

    def visitExprLiteralCadenaG4(self, ctx):
        return ctx.getText()[1:-1]

    def visitExprLiteralBoolG4(self, ctx):
        return ctx.getText() == "true"

    def visitExprReferenciaVariableG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(nombre)

        if simbolo is None:
            raise Exception(f"Variable '{nombre}' no existe")

        return simbolo["value"]

    def visitExprAritmeticaSumaResG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if ctx.TK_SUMA():
            return l + r
        return l - r

    def visitExprAritmeticaMultDivModG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        texto = ctx.getText()

        if "*" in texto:
            return l * r
        if "/" in texto:
            if r == 0:
                raise Exception("No se puede dividir entre cero")
            return l / r
        if "%" in texto:
            if r == 0:
                raise Exception("No se puede usar módulo con cero")
            return l % r

        return None

    def visitExprRelacionalCompG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        texto = ctx.getText()

        if ">=" in texto: return l >= r
        if "<=" in texto: return l <= r
        if ">" in texto: return l > r
        if "<" in texto: return l < r

    def visitExprRelacionalIgualdadG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        texto = ctx.getText()

        if "==" in texto:
            return l == r
        return l != r

    def visitExprAgrupacionG4(self, ctx):
        return self.visit(ctx.expr())