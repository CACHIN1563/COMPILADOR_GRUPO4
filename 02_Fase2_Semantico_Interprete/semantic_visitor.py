# =================================================================
# UNIVERSIDAD MARIANO GÁLVEZ - GRUPO 4
# ANALIZADOR SEMÁNTICO (VISTOR) - PROYECTO 2
# =================================================================
# Este componente valida que la lógica del programa sea correcta
# (tipos, declaraciones, ámbitos) antes de ejecutar el código.

from GramaticaVisitor import GramaticaVisitor
from GramaticaParser import GramaticaParser
from symbol_table import SymbolTable

class SemanticVisitor(GramaticaVisitor):
    def __init__(self):
        # Iniciamos la tabla y el contador de errores
        self.tabla_simbolos = SymbolTable()
        self.errores = []
        self.tipo_retorno_actual = None

    def reportar_error(self, ctx, mensaje):
        """Formatea el error para que sea amigable al programador."""
        linea = ctx.start.line
        columna = ctx.start.column
        self.errores.append(f"* Semántico: [Error Semántico] Línea {linea}, Columna {columna}: {mensaje}")

    def obtener_tipo(self, ctx_tipo):
        """Auxiliar para obtener el string del tipo de dato del nodo."""
        if isinstance(ctx_tipo, GramaticaParser.TypeIntG4Context): return "int"
        if isinstance(ctx_tipo, GramaticaParser.TypeFloatG4Context): return "float"
        if isinstance(ctx_tipo, GramaticaParser.TypeStringG4Context): return "string"
        if isinstance(ctx_tipo, GramaticaParser.TypeBoolG4Context): return "bool"
        if isinstance(ctx_tipo, GramaticaParser.TypeVoidG4Context): return "void"
        return "desconocido"

    # --- Puntos de Entrada y Declaraciones ---

    def visitProgramG4(self, ctx:GramaticaParser.ProgramG4Context):
        # El punto de entrada principal del compilador
        return self.visitChildren(ctx)

    def visitVarDeclarationG4(self, ctx:GramaticaParser.VarDeclarationG4Context):
        # Manejo de la declaración de variables (int x = 10;)
        t_dato = self.obtener_tipo(ctx.type_())
        id_var = ctx.TK_ID().getText()
        
        if ctx.expr():
            # Si hay una expresión inicial, validamos su tipo
            t_expr = self.visit(ctx.expr())
            if not self.tipos_compatibles(t_dato, t_expr):
                self.reportar_error(ctx, f"Error: No puedes asignar '{t_expr}' a '{t_dato}'.")
        
        # Guardamos en la tabla de simbolos local
        exito, msg_error = self.tabla_simbolos.declare(id_var, t_dato)
        if not exito:
            self.reportar_error(ctx, msg_error) # Ya existe en el mismo scope
        return t_dato

    def visitFuncDeclarationG4(self, ctx:GramaticaParser.FuncDeclarationG4Context):
        # Registro de funciones y sus parámetros
        t_ret = self.obtener_tipo(ctx.type_())
        nombre_f = ctx.TK_ID().getText()
        
        args_lista = []
        if ctx.params():
            ctx_params = ctx.params()
            for p_nodo in ctx_params.param():
                p_tipo = self.obtener_tipo(p_nodo.type_())
                p_nombre = p_nodo.TK_ID().getText()
                args_lista.append((p_tipo, p_nombre))

        # Registrar la firma de la función (globalmente)
        exito, msg_error = self.tabla_simbolos.declare(nombre_f, t_ret, es_funcion=True, parametros=args_lista)
        if not exito:
            self.reportar_error(ctx, msg_error)
        
        # Crear un nuevo ámbito para el cuerpo de la función
        self.tabla_simbolos.push_scope()
        self.tipo_retorno_actual = t_ret # Guardamos para validar el 'return'
        
        # Declarar parámetros dentro del nuevo scope
        for t_p, n_p in args_lista:
            self.tabla_simbolos.declare(n_p, t_p)
            
        self.visit(ctx.bloque()) # Validar el bloque de código
        
        self.tabla_simbolos.pop_scope()
        self.tipo_retorno_actual = None
        return t_ret

    # --- Sentencias y Asignaciones ---

    def visitAsignacionCoreG4(self, ctx:GramaticaParser.AsignacionCoreG4Context):
        # Valida que la variable exista y coincida el tipo
        nombre_id = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(nombre_id)
        
        if simbolo is None:
            self.reportar_error(ctx, f"La variable '{nombre_id}' no ha sido declarada.")
            return "desconocido"
        
        if simbolo['is_func']:
            self.reportar_error(ctx, f"'{nombre_id}' es una función, no le puedes asignar valores.")
            return "desconocido"
            
        t_actual_expr = self.visit(ctx.expr())
        if not self.tipos_compatibles(simbolo['type'], t_actual_expr):
            self.reportar_error(ctx, f"No se puede asignar '{t_actual_expr}' a '{simbolo['type']}' (Incompatibilidad).")
            
        return simbolo['type']

    def visitAsignacionVariableG4(self, ctx:GramaticaParser.AsignacionVariableG4Context):
        return self.visit(ctx.asignacion_core())

    def visitSentenciaIfElseG4(self, ctx:GramaticaParser.SentenciaIfElseG4Context):
        # Obligatorio que el 'if' sea booleano
        t_condicion = self.visit(ctx.expr())
        if t_condicion != "bool":
            self.reportar_error(ctx, f"El 'if' requiere una expresión booleana, no un '{t_condicion}'.")
        
        self.visit(ctx.bloque(0))
        if ctx.TK_ELSE():
            self.visit(ctx.bloque(1))
        return None

    def visitSentenciaMientrasG4(self, ctx:GramaticaParser.SentenciaMientrasG4Context):
        # El 'while' también requiere booleanos
        t_c = self.visit(ctx.expr())
        if t_c != "bool":
            self.reportar_error(ctx, f"Condición de 'while' inválida: se esperaba bool, no '{t_c}'.")
        
        self.tabla_simbolos.push_scope() # Un while genera su propio ámbito local
        self.visit(ctx.bloque())
        self.tabla_simbolos.pop_scope()
        return None

    def visitSentenciaForG4(self, ctx:GramaticaParser.SentenciaForG4Context):
        # Manejo de Scopes en el ciclo FOR
        self.tabla_simbolos.push_scope()
        
        if ctx.init_var: self.visit(ctx.init_var)
        elif ctx.init_assign: self.visit(ctx.init_assign)
        
        if ctx.cond:
            t_cond = self.visit(ctx.cond)
            if t_cond != "bool":
                self.reportar_error(ctx, f"Condición de 'for' debe ser booleana.")
        
        if ctx.update_assign: self.visit(ctx.update_assign)
        elif ctx.update_expr: self.visit(ctx.update_expr)

        self.visit(ctx.bloque())
        self.tabla_simbolos.pop_scope() # Limpiamos memoria del ciclo
        return None

    def visitSentenciaReturnG4(self, ctx:GramaticaParser.SentenciaReturnG4Context):
        # Validación crítica del tipo de retorno
        if self.tipo_retorno_actual is None:
            self.reportar_error(ctx, "Error: Usaste 'return' fuera de una función.")
            return None
            
        t_ret_expr = "void"
        if ctx.expr():
            t_ret_expr = self.visit(ctx.expr())
            
        if not self.tipos_compatibles(self.tipo_retorno_actual, t_ret_expr):
            self.reportar_error(ctx, f"El 'return' no coincide. Se esperaba '{self.tipo_retorno_actual}' pero intentas devolver '{t_ret_expr}'.")
        
        return t_ret_expr

    def visitSentenciaImprimirG4(self, ctx:GramaticaParser.SentenciaImprimirG4Context):
        self.visit(ctx.expr()) # Solo validamos que la expresión sea correcta
        return None

    def visitStatBloqueG4(self, ctx:GramaticaParser.StatBloqueG4Context):
        # Bloques aislados con {}
        self.tabla_simbolos.push_scope()
        self.visitChildren(ctx)
        self.tabla_simbolos.pop_scope()
        return None

    # --- Evaluación de Expresiones Literales ---

    def visitExprLiteralNumericaG4(self, ctx:GramaticaParser.ExprLiteralNumericaG4Context):
        texto = ctx.getText()
        return "float" if "." in texto else "int"

    def visitExprLiteralCadenaG4(self, ctx:GramaticaParser.ExprLiteralCadenaG4Context):
        return "string"

    def visitExprLiteralBoolG4(self, ctx:GramaticaParser.ExprLiteralBoolG4Context):
        return "bool"

    def visitExprReferenciaVariableG4(self, ctx:GramaticaParser.ExprReferenciaVariableG4Context):
        id_ref = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(id_ref)
        if simbolo is None:
            self.reportar_error(ctx, f"Variable '{id_ref}' no ha sido declarada.")
            return "desconocido"
        return simbolo['type']

    # --- Operaciones Aritméticas/Lógicas ---

    def visitExprAritmeticaSumaResG4(self, ctx:GramaticaParser.ExprAritmeticaSumaResG4Context):
        # Soporte para int, float y concatenación de strings (+)
        l_side = self.visit(ctx.expr(0))
        r_side = self.visit(ctx.expr(1))
        
        # Aritmética básica
        if l_side in ["int", "float"] and r_side in ["int", "float"]:
            return "float" if (l_side == "float" or r_side == "float") else "int"
        
        # Concatenación (solo con +)
        if l_side == "string" and r_side == "string" and ctx.TK_SUMA():
            return "string"
            
        self.reportar_error(ctx, f"Operación matemática inválida entre '{l_side}' y '{r_side}'.")
        return "desconocido"

    def visitExprAritmeticaMultDivG4(self, ctx:GramaticaParser.ExprAritmeticaMultDivG4Context):
        l_side = self.visit(ctx.expr(0))
        r_side = self.visit(ctx.expr(1))
        
        if l_side in ["int", "float"] and r_side in ["int", "float"]:
            if ctx.TK_DIV(): return "float" # La división en G4 siempre es float
            return "float" if (l_side == "float" or r_side == "float") else "int"
            
        self.reportar_error(ctx, f"No se puede multiplicar/dividir '{l_side}' con '{r_side}'.")
        return "desconocido"

    def visitExprPotenciaG4(self, ctx:GramaticaParser.ExprPotenciaG4Context):
        # Exponentes
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if l in ["int", "float"] and r in ["int", "float"]:
            return "float"
        self.reportar_error(ctx, f"Potencia requiere números, no '{l}' y '{r}'.")
        return "desconocido"

    def visitExprRelacionalCompG4(self, ctx:GramaticaParser.ExprRelacionalCompG4Context):
        # Comparaciones relacionales (>, <, >=, <=)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if l in ["int", "float"] and r in ["int", "float"]:
            return "bool"
        self.reportar_error(ctx, f"Relacionales solo para números: '{l}' vs '{r}'.")
        return "bool"

    def visitExprRelacionalIgualdadG4(self, ctx:GramaticaParser.ExprRelacionalIgualdadG4Context):
        # Igualdad (==, !=)
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if l == r or (l in ["int", "float"] and r in ["int", "float"]):
            return "bool"
        self.reportar_error(ctx, f"Incompatibilidad en igualdad: '{l}' vs '{r}'.")
        return "bool"

    def visitExprLogicaAndG4(self, ctx:GramaticaParser.ExprLogicaAndG4Context):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if l == "bool" and r == "bool": return "bool"
        self.reportar_error(ctx, f"AND requiere booleanos.")
        return "bool"

    def visitExprLogicaOrG4(self, ctx:GramaticaParser.ExprLogicaOrG4Context):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if l == "bool" and r == "bool": return "bool"
        self.reportar_error(ctx, f"OR requiere booleanos.")
        return "bool"

    def visitExprLogicaNotG4(self, ctx:GramaticaParser.ExprLogicaNotG4Context):
        v = self.visit(ctx.expr())
        if v == "bool": return "bool"
        self.reportar_error(ctx, f"NOT requiere booleano, no '{v}'.")
        return "bool"

    def visitExprAgrupacionG4(self, ctx:GramaticaParser.ExprAgrupacionG4Context):
        return self.visit(ctx.expr())

    def visitExprLlamadaFuncionG4(self, ctx:GramaticaParser.ExprLlamadaFuncionG4Context):
        # Verificación de llamadas (firma vs argumentos)
        f_id = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(f_id)
        
        if simbolo is None:
            self.reportar_error(ctx, f"La función '{f_id}' no existe.")
            return "desconocido"
        
        if not simbolo['is_func']:
            self.reportar_error(ctx, f"'{f_id}' no se puede llamar como función.")
            return "desconocido"
            
        args_evaluados = []
        if ctx.args():
            for e_nodo in ctx.args().expr():
                args_evaluados.append(self.visit(e_nodo))
                
        params_esperados = simbolo['params']
        if len(args_evaluados) != len(params_esperados):
            self.reportar_error(ctx, f"Función '{f_id}' requiere {len(params_esperados)} argumentos, pero enviaste {len(args_evaluados)}.")
        else:
            for i in range(len(args_evaluados)):
                if not self.tipos_compatibles(params_esperados[i][0], args_evaluados[i]):
                    self.reportar_error(ctx, f"Argumento #{i+1} de '{f_id}' tiene tipo incorrecto (se esperaba {params_esperados[i][0]}).")
                    
        return simbolo['type']

    def tipos_compatibles(self, t_esperado, t_obtenido):
        """Lógica de compatibilidad y promoción automática."""
        if t_esperado == t_obtenido: return True
        if t_esperado == "float" and t_obtenido == "int": return True # Un int cabe en un float
        if t_esperado == "desconocido" or t_obtenido == "desconocido": return True # No propagar errores
        return False
