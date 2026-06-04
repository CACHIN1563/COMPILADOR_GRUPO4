from gramatica_v4Visitor import gramatica_v4Visitor
from symbol_table import SymbolTable
import math

class InterpreterVisitorV4(gramatica_v4Visitor):

    def __init__(self):
        self.tabla_simbolos = SymbolTable()

    def visitProgramG4(self, ctx):
        for d in ctx.declaration():
            self.visit(d)
        return None

    def visitDeclStructG4(self, ctx):
        # En el intérprete, no necesitamos guardar la definición del struct
        # pues la semántica ya la validó.
        return None

    def visitVarDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        tipo_str = ctx.type_().getText()
        valor = None

        if ctx.expr():
            valor = self.visit(ctx.expr())
        else:
            if tipo_str.startswith("struct:") or tipo_str == "struct":
                # Fallback genérico para instanciar structs
                valor = {}
            elif tipo_str in ["int", "float"]:
                valor = 0
            
        self.tabla_simbolos.declare(nombre, tipo_str, valor=valor)
        return valor

    def visitVarArrayDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        valores = []

        if ctx.arrayLiteral():
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

    def visitExprAccesoCampoG4(self, ctx):
        base_val = self.visit(ctx.expr())
        campo = ctx.TK_ID().getText()
        if type(base_val) is dict and campo in base_val:
            return base_val[campo]
        # Auto-initialize dict Si venía en None
        if base_val is None:
            raise Exception("Struct no inicializado")
        return base_val.get(campo, 0) # default a 0

    def visitExprCastingG4(self, ctx):
        tipo_str = ctx.type_().getText()
        val = self.visit(ctx.expr())
        if tipo_str in ["int", "INT"]:
            return int(val)
        if tipo_str in ["float", "FLOAT"]:
            return float(val)
        return val

    def visitExprTernarioG4(self, ctx):
        cond = self.visit(ctx.expr(0))
        if cond:
            return self.visit(ctx.expr(1))
        else:
            return self.visit(ctx.expr(2))

    def get_lvalue_name_and_ref(self, ctx, lvalue_ctx):
        ids = lvalue_ctx.TK_ID()
        base_name = ids[0].getText()
        simbolo = self.tabla_simbolos.lookup(base_name)
        
        if len(ids) == 1:
            return base_name, simbolo, None
            
        # Struct
        ref = simbolo['value']
        if ref is None:
            ref = {}
            self.tabla_simbolos.update_value(base_name, ref)
            
        for i in range(1, len(ids) - 1):
            f_name = ids[i].getText()
            if f_name not in ref: ref[f_name] = {}
            ref = ref[f_name]
            
        last_field = ids[-1].getText()
        return base_name, ref, last_field

    def visitAsignacionCoreG4(self, ctx):
        lvalue = ctx.lvalue()
        valor = self.visit(ctx.expr())
        
        base_name, ref, field = self.get_lvalue_name_and_ref(ctx, lvalue)
        if field is None:
            self.tabla_simbolos.update_value(base_name, valor)
        else:
            ref[field] = valor
            
        return valor

    def visitAsignacionVariableG4(self, ctx):
        return self.visit(ctx.asignacion_core())

    def visitSentenciaSwitchG4(self, ctx):
        cond_val = self.visit(ctx.switchStatement().expr())
        
        executed = False
        for case in ctx.switchStatement().caseStatement():
            case_val = self.visit(case.expr())
            if case_val == cond_val:
                for inst in case.instruccion():
                    self.visit(inst)
                executed = True
                break # Simple implicit break
                
        if not executed and ctx.switchStatement().defaultStatement():
            for inst in ctx.switchStatement().defaultStatement().instruccion():
                self.visit(inst)

    def visitSentenciaIfElseG4(self, ctx):
        cond = self.visit(ctx.condicional().expr())
        if cond:
            self.visit(ctx.condicional().bloque(0))
        elif ctx.condicional().bloque(1):
            self.visit(ctx.condicional().bloque(1))

    def visitSentenciaMientrasG4(self, ctx):
        while self.visit(ctx.bucle_mientras().expr()):
            try:
                self.visit(ctx.bucle_mientras().bloque())
            except StopIteration: # para break
                break

    def visitSentenciaForG4(self, ctx):
        bucle = ctx.bucle_for()
        if bucle.init_var: self.visit(bucle.init_var)
        elif bucle.init_assign: self.visit(bucle.init_assign)
        
        while True:
            if bucle.cond:
                if not self.visit(bucle.cond):
                    break
            
            try:
                self.visit(bucle.bloque())
            except StopIteration:
                break
                
            if bucle.update_assign: self.visit(bucle.update_assign)
            elif bucle.update_expr: self.visit(bucle.update_expr)

    def visitSentenciaBreakG4(self, ctx):
        raise StopIteration()

    def visitSentenciaImprimirG4(self, ctx):
        valor = self.visit(ctx.impresion().expr())
        if valor is True: print("true")
        elif valor is False: print("false")
        else: print(valor)
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
        if simbolo is None: raise Exception(f"Variable '{nombre}' no existe")
        return simbolo["value"]

    def visitExprAritmeticaSumaResG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        if ctx.TK_SUMA(): return l + r
        return l - r

    def visitExprAritmeticaMultDivModG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        texto = ctx.getText()
        if "*" in texto: return l * r
        if "/" in texto: return l / r
        if "%" in texto: return l % r
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
        if "==" in texto: return l == r
        return l != r

    def visitExprLogicaAndG4(self, ctx):
        return self.visit(ctx.expr(0)) and self.visit(ctx.expr(1))

    def visitExprLogicaOrG4(self, ctx):
        return self.visit(ctx.expr(0)) or self.visit(ctx.expr(1))

    def visitExprLogicaNotG4(self, ctx):
        return not self.visit(ctx.expr())

    def visitExprAgrupacionG4(self, ctx):
        return self.visit(ctx.expr())
