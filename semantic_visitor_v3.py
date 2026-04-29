# =================================================================
# UNIVERSIDAD MARIANO GÁLVEZ - GRUPO 4
# ANALIZADOR SEMÁNTICO V3 (FASE 3)
# =================================================================

from Gramatica_v3Visitor import Gramatica_v3Visitor
from Gramatica_v3Parser import Gramatica_v3Parser
from symbol_table import SymbolTable

class SemanticVisitorV3(Gramatica_v3Visitor):

    def __init__(self):
        self.tabla_simbolos = SymbolTable()
        self.errores = []

    def error(self, ctx, msg):
        linea = ctx.start.line
        col = ctx.start.column
        self.errores.append(f"[Semántico] Línea {linea}:{col} -> {msg}")

    # =====================================================
    # TIPOS
    # =====================================================
    def visitTypeIntG4(self, ctx): return "int"
    def visitTypeFloatG4(self, ctx): return "float"
    def visitTypeStringG4(self, ctx): return "string"
    def visitTypeBoolG4(self, ctx): return "bool"
    def visitTypeVoidG4(self, ctx): return "void"
    def visitTypeIntArrayG4(self, ctx): return "int[]"

    # =====================================================
    # DECLARACIÓN VARIABLES
    # =====================================================
    def visitVarDeclarationG4(self, ctx):
        tipo = self.visit(ctx.type_())
        nombre = ctx.TK_ID().getText()

        valor_tipo = None
        if ctx.expr():
            valor_tipo = self.visit(ctx.expr())

            if valor_tipo and valor_tipo != tipo:
                self.error(ctx, f"No puedes asignar {valor_tipo} a {tipo}")

        ok, err = self.tabla_simbolos.declare(nombre, tipo)
        if not ok:
            self.error(ctx, err)

        return tipo

    # =====================================================
    # ARRAYS
    # =====================================================
    def visitVarArrayDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()

        valores = []
        for e in ctx.arrayLiteral().expr():
            t = self.visit(e)
            if t != "int":
                self.error(ctx, "Los arrays solo permiten enteros")
            valores.append(t)

        ok, err = self.tabla_simbolos.declare(nombre, "int[]")
        if not ok:
            self.error(ctx, err)

        return "int[]"

    def visitExprArrayAccessG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(nombre)

        if simbolo is None:
            self.error(ctx, f"Array '{nombre}' no existe")
            return "desconocido"

        if simbolo['type'] != "int[]":
            self.error(ctx, f"'{nombre}' no es un array")
            return "desconocido"

        idx = self.visit(ctx.expr())
        if idx != "int":
            self.error(ctx, "Índice debe ser entero")

        return "int"

    # =====================================================
    # EXPRESIONES
    # =====================================================
    def visitExprLiteralNumericaG4(self, ctx):
        txt = ctx.getText()
        return "float" if "." in txt else "int"

    def visitExprLiteralCadenaG4(self, ctx):
        return "string"

    def visitExprLiteralBoolG4(self, ctx):
        return "bool"

    def visitExprReferenciaVariableG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(nombre)

        if simbolo is None:
            self.error(ctx, f"Variable '{nombre}' no existe")
            return "desconocido"

        return simbolo['type']

    # =====================================================
    # OPERACIONES
    # =====================================================
    def visitExprAritmeticaSumaResG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if l in ["int", "float"] and r in ["int", "float"]:
            return "float" if "float" in [l, r] else "int"

        if l == "string" and r == "string":
            return "string"

        self.error(ctx, f"Suma inválida {l} + {r}")
        return "desconocido"

    def visitExprAritmeticaMultDivModG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if l in ["int", "float"] and r in ["int", "float"]:
            return "float" if "float" in [l, r] else "int"

        self.error(ctx, f"Operación inválida {l} y {r}")
        return "desconocido"