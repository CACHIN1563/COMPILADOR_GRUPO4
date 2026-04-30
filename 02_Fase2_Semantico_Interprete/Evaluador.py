import math
from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser

class Evaluador(GramaticaVisitor):
    """
    Clase Evaluador: Implementa la lógica de ejecución del lenguaje G4.
    Desarrollado por el Grupo 4 .
    """

    def __init__(self):
        # Diccionario para persistir las variables en memoria durante la ejecución
        self.memoria_variables = {}
        self.debug_mode = False

    # --- Estructura del Programa ---
    
    def visitProgramaCompletoG4(self, ctx: GramaticaParser.ProgramaCompletoG4Context):
        # El programa comienza su ejecución secuencial de instrucciones
        for instruccion in ctx.instruccion():
            self.visit(instruccion)
        return None

    # --- Instrucciones y Sentencias ---

    def visitAsignacionVariableG4(self, ctx: GramaticaParser.AsignacionVariableG4Context):
        nombre_var = ctx.TK_ID().getText()
        valor_final = self.visit(ctx.expr())
        self.memoria_variables[nombre_var] = valor_final
        return valor_final

    def visitSentenciaImprimirG4(self, ctx: GramaticaParser.SentenciaImprimirG4Context):
        resultado = self.visit(ctx.expr())
        print(f">> [G4-OUTPUT]: {resultado}")
        return resultado

    def visitSentenciaIfElseG4(self, ctx: GramaticaParser.SentenciaIfElseG4Context):
        condicion = self.visit(ctx.expr())
        if condicion:
            # Ejecutar bloque del 'SI'
            return self.visit(ctx.bloque(0))
        elif ctx.TK_SINO():
            # Ejecutar bloque del 'SINO' si existe
            return self.visit(ctx.bloque(1))
        return None

    def visitSentenciaMientrasG4(self, ctx: GramaticaParser.SentenciaMientrasG4Context):
        # Bucle WHILE: Se ejecuta mientras la condición sea verdadera
        while self.visit(ctx.expr()):
            self.visit(ctx.bloque())
        return None

    def visitBloqueCodigoG4(self, ctx: GramaticaParser.BloqueCodigoG4Context):
        # Ejecución de múltiples instrucciones dentro de llaves {}
        for instruccion in ctx.instruccion():
            self.visit(instruccion)
        return None

    # --- Evaluación de Expresiones (Lógica, Relacional, Aritmética) ---

    def visitExprAgrupacionG4(self, ctx: GramaticaParser.ExprAgrupacionG4Context):
        return self.visit(ctx.expr())

    def visitExprLiteralNumericaG4(self, ctx: GramaticaParser.ExprLiteralNumericaG4Context):
        num_str = ctx.TK_NUMERO().getText()
        return float(num_str) if '.' in num_str else int(num_str)

    def visitExprLiteralCadenaG4(self, ctx: GramaticaParser.ExprLiteralCadenaG4Context):
        # Retornar la cadena eliminando las comillas iniciales y finales
        cadena = ctx.TK_CADENA().getText()
        return cadena[1:-1]

    def visitExprReferenciaVariableG4(self, ctx: GramaticaParser.ExprReferenciaVariableG4Context):
        nombre = ctx.TK_ID().getText()
        if nombre in self.memoria_variables:
            return self.memoria_variables[nombre]
        print(f"[!] Error de Ejecución: La variable '{nombre}' no ha sido definida.")
        return 0

    def visitExprAritmeticaSumaResG4(self, ctx: GramaticaParser.ExprAritmeticaSumaResG4Context):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        if ctx.TK_SUMA():
            return izq + der
        return izq - der

    def visitExprAritmeticaMultDivG4(self, ctx: GramaticaParser.ExprAritmeticaMultDivG4Context):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        if ctx.TK_MULT():
            return izq * der
        if der == 0:
            print("[!] Error: División por cero detectada.")
            return 0
        return izq / der

    def visitExprPotenciaG4(self, ctx: GramaticaParser.ExprPotenciaG4Context):
        base = self.visit(ctx.expr(0))
        exponente = self.visit(ctx.expr(1))
        return math.pow(base, exponente)

    def visitExprRelacionalCompG4(self, ctx: GramaticaParser.ExprRelacionalCompG4Context):
        v1 = self.visit(ctx.expr(0))
        v2 = self.visit(ctx.expr(1))
        if ctx.TK_MAYOR(): return v1 > v2
        if ctx.TK_MENOR(): return v1 < v2
        if ctx.TK_MAYOREQ(): return v1 >= v2
        if ctx.TK_MENOREQ(): return v1 <= v2
        return False

    def visitExprRelacionalIgualdadG4(self, ctx: GramaticaParser.ExprRelacionalIgualdadG4Context):
        v1 = self.visit(ctx.expr(0))
        v2 = self.visit(ctx.expr(1))
        if ctx.TK_IGUAL(): return v1 == v2
        if ctx.TK_DIFERENTE(): return v1 != v2
        return False

    def visitExprLogicaAndG4(self, ctx: GramaticaParser.ExprLogicaAndG4Context):
        return bool(self.visit(ctx.expr(0))) and bool(self.visit(ctx.expr(1)))

    def visitExprLogicaOrG4(self, ctx: GramaticaParser.ExprLogicaOrG4Context):
        return bool(self.visit(ctx.expr(0))) or bool(self.visit(ctx.expr(1)))

    def visitExprLogicaNotG4(self, ctx: GramaticaParser.ExprLogicaNotG4Context):
        return not bool(self.visit(ctx.expr()))
