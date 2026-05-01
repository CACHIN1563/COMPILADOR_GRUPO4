# =================================================================
# UNIVERSIDAD MARIANO GÁLVEZ - GRUPO 4
# INTÉRPRETE DE EJECUCIÓN (VISITOR) - PROYECTO 2
# =================================================================
# Este motor recorre el AST y ejecuta las instrucciones reales.
# Solo se llama si la fase semántica terminó sin errores.

from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser
from symbol_table import SymbolTable
import math

class ExcepcionRetorno(Exception):
    """Excepción para manejar el 'return' en funciones recursivas."""
    def __init__(self, valor):
        self.valor = valor

class InterpreterVisitor(GramaticaVisitor):
    def __init__(self):
        # Iniciamos la tabla de símbolos para la ejecución real
        self.tabla_simbolos = SymbolTable()

    def visitProgramG4(self, ctx:GramaticaParser.ProgramG4Context):
        # Fase A: Registrar todas las funciones (Hoisting manual para recursividad)
        for d in ctx.declaration():
            if isinstance(d, GramaticaParser.DeclFuncionG4Context):
                self.visit(d)
        
        # Fase B: Ejecutar declaraciones de variables y sentencias globales
        for d in ctx.declaration():
            if not isinstance(d, GramaticaParser.DeclFuncionG4Context):
                self.visit(d)
        return None

    def visitVarDeclarationG4(self, ctx:GramaticaParser.VarDeclarationG4Context):
        # Creación de variable física en memoria
        id_v = ctx.TK_ID().getText()
        valor_inicial = None
        if ctx.expr():
            valor_inicial = self.visit(ctx.expr())
        
        # Guardamos en la memoria de ejecución
        self.tabla_simbolos.declare(id_v, "dynamic", valor=valor_inicial)
        return valor_inicial

    def visitFuncDeclarationG4(self, ctx:GramaticaParser.FuncDeclarationG4Context):
        # Guardamos el cuerpo de la función para usarlo después (Lazy Evaluation)
        nombre_f = ctx.TK_ID().getText()
        self.tabla_simbolos.declare(nombre_f, "func_ptr", valor=ctx, es_funcion=True)
        return None

    def visitAsignacionCoreG4(self, ctx:GramaticaParser.AsignacionCoreG4Context):
        # Actualización de valor en memoria
        id_a = ctx.TK_ID().getText()
        v_a = self.visit(ctx.expr())
        self.tabla_simbolos.update_value(id_a, v_a)
        return v_a

    def visitAsignacionVariableG4(self, ctx:GramaticaParser.AsignacionVariableG4Context):
        return self.visit(ctx.asignacion_core())

    def visitSentenciaIfElseG4(self, ctx:GramaticaParser.SentenciaIfElseG4Context):
        # Lógica del IF real
        c = ctx.condicional()
        cond_bool = self.visit(c.expr())
        if cond_bool:
            self.visit(c.bloque(0))
        elif c.TK_SINO():
            self.visit(c.bloque(1))
        return None

    def visitSentenciaMientrasG4(self, ctx:GramaticaParser.SentenciaMientrasG4Context):
        # Bucle WHILE
        m = ctx.bucle_mientras()
        while self.visit(m.expr()):
            self.visit(m.bloque())
        return None

    def visitSentenciaForG4(self, ctx:GramaticaParser.SentenciaForG4Context):
        # Ejecución del Ciclo FOR
        f = ctx.bucle_for()
        self.tabla_simbolos.push_scope()
        
        # 1. Inicialización
        if f.init_var: self.visit(f.init_var)
        elif f.init_assign: self.visit(f.init_assign)
        
        # 2. Bucle de ejecución
        while True:
            if f.cond:
                if not self.visit(f.cond): break
            
            self.visit(f.bloque())
            
            # 3. Actualización (update)
            if f.update_assign: self.visit(f.update_assign)
            elif f.update_expr: self.visit(f.update_expr)
                
        self.tabla_simbolos.pop_scope()
        return None

    def visitSentenciaImprimirG4(self, ctx:GramaticaParser.SentenciaImprimirG4Context):
        # La salida estándar nativa del lenguaje G4
        valor_final = self.visit(ctx.impresion().expr())
        # Manejo bonito de booleanos en terminal
        if valor_final is True: print("true")
        elif valor_final is False: print("false")
        else: print(valor_final)
        return None

    def visitSentenciaReturnG4(self, ctx:GramaticaParser.SentenciaReturnG4Context):
        # Interrumpe la ejecución del bloque lanzando el valor
        r = ctx.sentencia_return()
        res = None
        if r.expr():
            res = self.visit(r.expr())
        raise ExcepcionRetorno(res)

    def visitStatBloqueG4(self, ctx:GramaticaParser.StatBloqueG4Context):
        self.tabla_simbolos.push_scope()
        self.visitChildren(ctx.bloque())
        self.tabla_simbolos.pop_scope()
        return None

    # --- Evaluación Real de Valores ---

    def visitExprLiteralNumericaG4(self, ctx:GramaticaParser.ExprLiteralNumericaG4Context):
        v_str = ctx.getText()
        return float(v_str) if "." in v_str else int(v_str)

    def visitExprLiteralCadenaG4(self, ctx:GramaticaParser.ExprLiteralCadenaG4Context):
        return ctx.getText()[1:-1] # Quitamos las comillas

    def visitExprLiteralBoolG4(self, ctx:GramaticaParser.ExprLiteralBoolG4Context):
        return ctx.getText() == "true"

    def visitExprReferenciaVariableG4(self, ctx:GramaticaParser.ExprReferenciaVariableG4Context):
        id_ref = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(id_ref)
        return simbolo['value']

    def visitExprAritmeticaSumaResG4(self, ctx:GramaticaParser.ExprAritmeticaSumaResG4Context):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        return (l + r) if ctx.TK_SUMA() else (l - r)

    def visitExprAritmeticaMultDivG4(self, ctx:GramaticaParser.ExprAritmeticaMultDivG4Context):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if ctx.TK_MULT(): return l * r
        if r == 0: raise Exception("Error Fatal: ¡No se puede dividir por cero!")
        return l / r

    def visitExprPotenciaG4(self, ctx:GramaticaParser.ExprPotenciaG4Context):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        return math.pow(l, r)

    def visitExprRelacionalCompG4(self, ctx:GramaticaParser.ExprRelacionalCompG4Context):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if ctx.TK_MAYOR(): return l > r
        if ctx.TK_MENOR(): return l < r
        if ctx.TK_MAYOREQ(): return l >= r
        if ctx.TK_MENOREQ(): return l <= r
        return False

    def visitExprRelacionalIgualdadG4(self, ctx:GramaticaParser.ExprRelacionalIgualdadG4Context):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        return (l == r) if ctx.TK_IGUAL() else (l != r)

    def visitExprLogicaAndG4(self, ctx:GramaticaParser.ExprLogicaAndG4Context):
        return self.visit(ctx.expr(0)) and self.visit(ctx.expr(1))

    def visitExprLogicaOrG4(self, ctx:GramaticaParser.ExprLogicaOrG4Context):
        return self.visit(ctx.expr(0)) or self.visit(ctx.expr(1))

    def visitExprLogicaNotG4(self, ctx:GramaticaParser.ExprLogicaNotG4Context):
        return not self.visit(ctx.expr())

    def visitExprAgrupacionG4(self, ctx:GramaticaParser.ExprAgrupacionG4Context):
        return self.visit(ctx.expr())

    def visitExprLlamadaFuncionG4(self, ctx:GramaticaParser.ExprLlamadaFuncionG4Context):
        # Gestión de la pila de llamadas real
        id_f = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(id_f)
        ctx_func = simbolo['value'] 
        
        # Evaluamos argumentos antes de entrar a la función
        args_reales = []
        if ctx.args():
            for e_nodo in ctx.args().expr():
                args_reales.append(self.visit(e_nodo))
                
        # Nuevo ámbito para la ejecución de la función
        self.tabla_simbolos.push_scope()
        
        # Mapeamos argumentos a los parámetros declarados
        nodo_params = ctx_func.params()
        if nodo_params:
            for i in range(len(nodo_params.param())):
                p_nombre = nodo_params.param(i).TK_ID().getText()
                self.tabla_simbolos.declare(p_nombre, "auto", valor=args_reales[i])
                
        # Ejecución y captura del retorno
        valor_retornado = None
        try:
            self.visit(ctx_func.bloque())
        except ExcepcionRetorno as er:
            valor_retornado = er.valor
            
        self.tabla_simbolos.pop_scope()
        return valor_retornado
