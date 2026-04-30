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
    # PROGRAMA
    # =====================================================
    def visitProgramG4(self, ctx):
        for d in ctx.declaration():
            self.visit(d)
        return None

    def visitDeclVariableG4(self, ctx):
        return self.visit(ctx.varDeclaration())

    def visitDeclFuncionG4(self, ctx):
        return self.visit(ctx.funcDeclaration())

    def visitDeclInstruccionG4(self, ctx):
        return self.visit(ctx.instruccion())

    def visitDeclImportG4(self, ctx):
        nombre_modulo = ctx.importacion().TK_ID().getText()
        # Registro básico del import
        self.tabla_simbolos.declare(nombre_modulo, "modulo")
        return "modulo"

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

        if ctx.expr():
            valor_tipo = self.visit(ctx.expr())
            if valor_tipo and valor_tipo != tipo:
                # Permitir int -> float
                if not (tipo == "float" and valor_tipo == "int"):
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

        if ctx.arrayLiteral():
            for e in ctx.arrayLiteral().expr():
                t = self.visit(e)
                if t != "int":
                    self.error(ctx, "Los arrays solo permiten enteros en este ejemplo")

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
    # CONTROL DE FLUJO
    # =====================================================
    def visitSentenciaIfElseG4(self, ctx):
        cond = self.visit(ctx.condicional().expr())
        if cond != "bool":
            self.error(ctx, "Condición del SI debe ser booleana")
        
        self.visit(ctx.condicional().bloque(0))
        if ctx.condicional().bloque(1):
            self.visit(ctx.condicional().bloque(1))

    def visitSentenciaMientrasG4(self, ctx):
        cond = self.visit(ctx.bucle_mientras().expr())
        if cond != "bool":
            self.error(ctx, "Condición del MIENTRAS debe ser booleana")
        self.visit(ctx.bucle_mientras().bloque())

    def visitSentenciaForG4(self, ctx):
        # Enter loop scope? Simbol table needs scopes
        self.visit(ctx.bucle_for().bloque())

    def visitSentenciaBreakG4(self, ctx): return None
    def visitSentenciaContinueG4(self, ctx): return None

    # =====================================================
    # FUNCIONES
    # =====================================================
    def visitFuncDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        tipo_ret = self.visit(ctx.type_())
        # En una tabla de símbolos real, registraríamos la firma
        self.tabla_simbolos.declare(nombre, f"func:{tipo_ret}")
        self.visit(ctx.bloque())
        return tipo_ret

    def visitExprLlamadaFuncionG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(nombre)
        if simbolo and simbolo['type'].startswith("func:"):
            return simbolo['type'].split(":")[1]
        return "desconocido"

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

    def visitAsignacionVariableG4(self, ctx):
        return self.visit(ctx.asignacion_core())

    def visitAsignacionCoreG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(nombre)
        tipo_expr = self.visit(ctx.expr())

        if simbolo:
            if simbolo['type'] != tipo_expr:
                if not (simbolo['type'] == "float" and tipo_expr == "int"):
                    self.error(ctx, f"Tipo incorrecto en asignación: {simbolo['type']} != {tipo_expr}")
        return tipo_expr

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

        return "desconocido"

    def visitExprRelacionalCompG4(self, ctx):
        return "bool"

    def visitExprRelacionalIgualdadG4(self, ctx):
        return "bool"

    def visitExprLogicaAndG4(self, ctx): return "bool"
    def visitExprLogicaOrG4(self, ctx): return "bool"
    def visitExprLogicaNotG4(self, ctx): return "bool"

    def visitStatBloqueG4(self, ctx):
        self.visit(ctx.bloque())
        return None

    def visitBloque(self, ctx):
        for i in ctx.instruccion():
            self.visit(i)
        return None