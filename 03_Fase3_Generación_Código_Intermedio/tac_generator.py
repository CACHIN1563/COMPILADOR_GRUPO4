# =================================================================
# GENERADOR DE CÓDIGO INTERMEDIO (TAC) - FASE 3
# =================================================================

from Gramatica_v3Visitor import Gramatica_v3Visitor

class TACGenerator(Gramatica_v3Visitor):

    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.code = []
        self.loop_stack = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

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

        if ctx.arrayLiteral():
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

    # =====================================================
    # ASIGNACIÓN
    # =====================================================
    def visitAsignacionVariableG4(self, ctx):
        return self.visit(ctx.asignacion_core())

    def visitAsignacionCoreG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        val = self.visit(ctx.expr())
        self.emit(f"{nombre} = {val}")
        return nombre

    # =====================================================
    # CONTROL DE FLUJO
    # =====================================================
    def visitSentenciaIfElseG4(self, ctx):
        cond = self.visit(ctx.condicional().expr())
        label_else = self.new_label()
        label_end = self.new_label()

        self.emit(f"if not {cond} goto {label_else}")
        self.visit(ctx.condicional().bloque(0))
        self.emit(f"goto {label_end}")
        
        self.emit(f"{label_else}:")
        if ctx.condicional().bloque(1):
            self.visit(ctx.condicional().bloque(1))
        
        self.emit(f"{label_end}:")

    def visitSentenciaMientrasG4(self, ctx):
        label_start = self.new_label()
        label_end = self.new_label()

        self.loop_stack.append((label_start, label_end))

        self.emit(f"{label_start}:")
        cond = self.visit(ctx.bucle_mientras().expr())
        self.emit(f"if not {cond} goto {label_end}")
        
        self.visit(ctx.bucle_mientras().bloque())
        self.emit(f"goto {label_start}")
        
        self.emit(f"{label_end}:")
        self.loop_stack.pop()

    def visitSentenciaForG4(self, ctx):
        # for (init; cond; update)
        if ctx.bucle_for().init_var:
            self.visit(ctx.bucle_for().init_var)
        elif ctx.bucle_for().init_assign:
            self.visit(ctx.bucle_for().init_assign)

        label_start = self.new_label()
        label_update = self.new_label()
        label_end = self.new_label()

        self.loop_stack.append((label_update, label_end))

        self.emit(f"{label_start}:")
        if ctx.bucle_for().cond:
            cond = self.visit(ctx.bucle_for().cond)
            self.emit(f"if not {cond} goto {label_end}")

        self.visit(ctx.bucle_for().bloque())

        self.emit(f"{label_update}:")
        if ctx.bucle_for().update_assign:
            self.visit(ctx.bucle_for().update_assign)
        elif ctx.bucle_for().update_expr:
            self.visit(ctx.bucle_for().update_expr)

        self.emit(f"goto {label_start}")
        self.emit(f"{label_end}:")
        self.loop_stack.pop()

    def visitSentenciaBreakG4(self, ctx):
        if self.loop_stack:
            _, end_label = self.loop_stack[-1]
            self.emit(f"goto {end_label}")

    def visitSentenciaContinueG4(self, ctx):
        if self.loop_stack:
            start_label, _ = self.loop_stack[-1]
            self.emit(f"goto {start_label}")

    def visitSentenciaReturnG4(self, ctx):
        if ctx.expr():
            val = self.visit(ctx.expr())
            self.emit(f"return {val}")
        else:
            self.emit("return")

    # =====================================================
    # FUNCIONES
    # =====================================================
    def visitFuncDeclarationG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        self.emit(f"begin_func {nombre}")
        self.visit(ctx.bloque())
        self.emit(f"end_func {nombre}")

    def visitExprLlamadaFuncionG4(self, ctx):
        nombre = ctx.TK_ID().getText()
        params = []
        if ctx.args():
            for e in ctx.args().expr():
                p = self.visit(e)
                params.append(p)
                self.emit(f"param {p}")
        
        temp = self.new_temp()
        self.emit(f"{temp} = call {nombre}, {len(params)}")
        return temp

    # =====================================================
    # COMPARACIONES
    # =====================================================
    def visitExprRelacionalCompG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        temp = self.new_temp()
        self.emit(f"{temp} = {l} {op} {r}")
        return temp

    def visitExprRelacionalIgualdadG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()
        temp = self.new_temp()
        self.emit(f"{temp} = {l} {op} {r}")
        return temp

    def visitExprLogicaAndG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        temp = self.new_temp()
        self.emit(f"{temp} = {l} && {r}")
        return temp

    def visitExprLogicaOrG4(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
        temp = self.new_temp()
        self.emit(f"{temp} = {l} || {r}")
        return temp

    def visitExprLogicaNotG4(self, ctx):
        val = self.visit(ctx.expr())
        temp = self.new_temp()
        self.emit(f"{temp} = !{val}")
        return temp