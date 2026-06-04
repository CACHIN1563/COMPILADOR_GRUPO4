# =================================================================
# UNIVERSIDAD MARIANO GÁLVEZ - GRUPO 4
# ANALIZADOR SEMÁNTICO V4 (PROYECTO FINAL)
# =================================================================

from gramatica_v4Visitor import gramatica_v4Visitor
from symbol_table import SymbolTable

class SemanticVisitorV4(gramatica_v4Visitor):

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
        self.tabla_simbolos.declare(nombre_modulo, "modulo")
        return "modulo"

    def visitDeclStructG4(self, ctx):
        struct_name = ctx.structDeclaration().TK_ID().getText()
        fields = {}
        for field in ctx.structDeclaration().structField():
            field_type = self.visit(field.type_())
            field_name = field.TK_ID().getText()
            fields[field_name] = field_type
        
        ok, err = self.tabla_simbolos.declare(struct_name, "struct_def", valor=fields)
        if not ok:
            self.error(ctx, f"Struct '{struct_name}' ya ha sido definido.")
        return "struct_def"

    # =====================================================
    # TIPOS
    # =====================================================
    def visitTypeIntG4(self, ctx): return "int"
    def visitTypeFloatG4(self, ctx): return "float"
    def visitTypeStringG4(self, ctx): return "string"
    def visitTypeBoolG4(self, ctx): return "bool"
    def visitTypeVoidG4(self, ctx): return "void"
    def visitTypeIntArrayG4(self, ctx): return "int[]"
    def visitTypeStructG4(self, ctx): return f"struct:{ctx.TK_ID().getText()}"

    # =====================================================
    # DECLARACIÓN VARIABLES
    # =====================================================
    def visitVarDeclarationG4(self, ctx):
        tipo = self.visit(ctx.type_())
        nombre = ctx.TK_ID().getText()

        if tipo.startswith("struct:"):
            struct_name = tipo.split(":")[1]
            if not self.tabla_simbolos.lookup(struct_name):
                self.error(ctx, f"El struct '{struct_name}' no está definido.")
                return "desconocido"

        if ctx.expr():
            valor_tipo = self.visit(ctx.expr())
            if valor_tipo and valor_tipo != tipo:
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

    def visitSentenciaSwitchG4(self, ctx):
        cond_type = self.visit(ctx.switchStatement().expr())
        for case in ctx.switchStatement().caseStatement():
            case_type = self.visit(case.expr())
            if case_type != cond_type:
                self.error(case, f"El tipo del 'case' ({case_type}) no coincide con la condición '{cond_type}'")
            for inst in case.instruccion():
                self.visit(inst)
                
        if ctx.switchStatement().defaultStatement():
            for inst in ctx.switchStatement().defaultStatement().instruccion():
                self.visit(inst)

    def visitSentenciaMientrasG4(self, ctx):
        cond = self.visit(ctx.bucle_mientras().expr())
        if cond != "bool":
            self.error(ctx, "Condición del MIENTRAS debe ser booleana")
        self.visit(ctx.bucle_mientras().bloque())

    def visitSentenciaForG4(self, ctx):
        self.tabla_simbolos.push_scope()
        bucle = ctx.bucle_for()
        if bucle.init_var: self.visit(bucle.init_var)
        elif bucle.init_assign: self.visit(bucle.init_assign)
        
        if bucle.cond:
            if self.visit(bucle.cond) != "bool":
                self.error(ctx, "Condición del FOR debe ser booleana")
                
        if bucle.update_assign: self.visit(bucle.update_assign)
        elif bucle.update_expr: self.visit(bucle.update_expr)
        
        self.visit(bucle.bloque())
        self.tabla_simbolos.pop_scope()

    def visitSentenciaBreakG4(self, ctx): return None
    def visitSentenciaContinueG4(self, ctx): return None

    # =====================================================
    # FUNCIONES
    # =====================================================
    def visitFuncDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        tipo_ret = self.visit(ctx.type_())
        self.tabla_simbolos.declare(nombre, f"func:{tipo_ret}")
        self.tabla_simbolos.push_scope()
        if ctx.params():
            for param in ctx.params().param():
                p_tipo = self.visit(param.type_())
                p_nombre = param.TK_ID().getText()
                self.tabla_simbolos.declare(p_nombre, p_tipo)
        self.visit(ctx.bloque())
        self.tabla_simbolos.pop_scope()
        return tipo_ret

    def visitExprLlamadaFuncionG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        simbolo = self.tabla_simbolos.lookup(nombre)
        if simbolo and simbolo['type'].startswith("func:"):
            return simbolo['type'].split(":")[1]
        self.error(ctx, f"Función '{nombre}' no definida")
        return "desconocido"

    # =====================================================
    # EXPRESIONES
    # =====================================================
    def visitExprCastingG4(self, ctx):
        target_type = self.visit(ctx.type_())
        expr_type = self.visit(ctx.expr())
        if (target_type in ["int", "float"] and expr_type in ["int", "float"]):
            return target_type
        self.error(ctx, f"No se puede castear explícitamente de {expr_type} a {target_type}")
        return target_type

    def visitExprTernarioG4(self, ctx):
        cond_type = self.visit(ctx.expr(0))
        if cond_type != "bool":
            self.error(ctx, "Condición de operador ternario debe ser bool")
        true_type = self.visit(ctx.expr(1))
        false_type = self.visit(ctx.expr(2))
        if true_type != false_type:
            if not (true_type in ["int", "float"] and false_type in ["int", "float"]):
                self.error(ctx, f"Los tipos del operador ternario no coinciden: {true_type} y {false_type}")
        return true_type if true_type == "float" else false_type

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

    def visitExprAccesoCampoG4(self, ctx):
        expr_type = self.visit(ctx.expr())
        field_name = ctx.TK_ID().getText()

        if expr_type.startswith("struct:"):
            struct_name = expr_type.split(":")[1]
            struct_def = self.tabla_simbolos.lookup(struct_name)
            if struct_def and struct_def['type'] == 'struct_def':
                fields = struct_def['value']
                if field_name in fields:
                    return fields[field_name]
                else:
                    self.error(ctx, f"Struct '{struct_name}' no tiene el campo '{field_name}'")
            else:
                self.error(ctx, f"'{struct_name}' no es un struct válido")
        else:
            self.error(ctx, f"No se puede acceder a campos en tipo '{expr_type}'")
        return "desconocido"

    def get_lvalue_type(self, ctx, lvalue_ctx):
        ids = lvalue_ctx.TK_ID()
        base_name = ids[0].getText()
        simbolo = self.tabla_simbolos.lookup(base_name)
        if not simbolo:
            self.error(ctx, f"Variable '{base_name}' no declarada")
            return "desconocido"
        
        current_type = simbolo['type']
        for i in range(1, len(ids)):
            field_name = ids[i].getText()
            if current_type.startswith("struct:"):
                struct_name = current_type.split(":")[1]
                struct_def = self.tabla_simbolos.lookup(struct_name)
                if struct_def and struct_def['type'] == 'struct_def':
                    fields = struct_def['value']
                    if field_name in fields:
                        current_type = fields[field_name]
                    else:
                        self.error(ctx, f"Struct '{struct_name}' no tiene el campo '{field_name}'")
                        return "desconocido"
            else:
                self.error(ctx, f"Acceso a campo '{field_name}' inválido en tipo '{current_type}'")
                return "desconocido"
                
        return current_type

    def visitAsignacionVariableG4(self, ctx):
        return self.visit(ctx.asignacion_core())

    def visitAsignacionCoreG4(self, ctx):
        lvalue_type = self.get_lvalue_type(ctx, ctx.lvalue())
        tipo_expr = self.visit(ctx.expr())

        if lvalue_type != "desconocido":
            if lvalue_type != tipo_expr:
                if not (lvalue_type == "float" and tipo_expr == "int"):
                    self.error(ctx, f"Tipo incorrecto en asignación: {lvalue_type} != {tipo_expr}")
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

    def visitExprAritmeticaMultDivModG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if l in ["int", "float"] and r in ["int", "float"]:
            return "float" if "float" in [l, r] else "int"
        return "desconocido"

    def visitExprRelacionalCompG4(self, ctx):
        return "bool"

    def visitExprRelacionalIgualdadG4(self, ctx):
        return "bool"

    def visitExprLogicaAndG4(self, ctx): return "bool"
    def visitExprLogicaOrG4(self, ctx): return "bool"
    def visitExprLogicaNotG4(self, ctx): return "bool"

    def visitStatBloqueG4(self, ctx):
        self.tabla_simbolos.push_scope()
        self.visit(ctx.bloque())
        self.tabla_simbolos.pop_scope()
        return None

    def visitBloque(self, ctx):
        for i in ctx.instruccion():
            self.visit(i)
        return None
