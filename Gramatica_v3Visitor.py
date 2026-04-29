# Generated from Gramatica_v3.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .Gramatica_v3Parser import Gramatica_v3Parser
else:
    from Gramatica_v3Parser import Gramatica_v3Parser

# This class defines a complete generic visitor for a parse tree produced by Gramatica_v3Parser.

class Gramatica_v3Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Gramatica_v3Parser#ProgramG4.
    def visitProgramG4(self, ctx:Gramatica_v3Parser.ProgramG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#DeclVariableG4.
    def visitDeclVariableG4(self, ctx:Gramatica_v3Parser.DeclVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#DeclFuncionG4.
    def visitDeclFuncionG4(self, ctx:Gramatica_v3Parser.DeclFuncionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#DeclInstruccionG4.
    def visitDeclInstruccionG4(self, ctx:Gramatica_v3Parser.DeclInstruccionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#VarDeclarationG4.
    def visitVarDeclarationG4(self, ctx:Gramatica_v3Parser.VarDeclarationG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#VarArrayDeclarationG4.
    def visitVarArrayDeclarationG4(self, ctx:Gramatica_v3Parser.VarArrayDeclarationG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:Gramatica_v3Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#FuncDeclarationG4.
    def visitFuncDeclarationG4(self, ctx:Gramatica_v3Parser.FuncDeclarationG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#params.
    def visitParams(self, ctx:Gramatica_v3Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#param.
    def visitParam(self, ctx:Gramatica_v3Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#TypeIntG4.
    def visitTypeIntG4(self, ctx:Gramatica_v3Parser.TypeIntG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#TypeFloatG4.
    def visitTypeFloatG4(self, ctx:Gramatica_v3Parser.TypeFloatG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#TypeStringG4.
    def visitTypeStringG4(self, ctx:Gramatica_v3Parser.TypeStringG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#TypeBoolG4.
    def visitTypeBoolG4(self, ctx:Gramatica_v3Parser.TypeBoolG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#TypeVoidG4.
    def visitTypeVoidG4(self, ctx:Gramatica_v3Parser.TypeVoidG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#TypeIntArrayG4.
    def visitTypeIntArrayG4(self, ctx:Gramatica_v3Parser.TypeIntArrayG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#AsignacionVariableG4.
    def visitAsignacionVariableG4(self, ctx:Gramatica_v3Parser.AsignacionVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#SentenciaIfElseG4.
    def visitSentenciaIfElseG4(self, ctx:Gramatica_v3Parser.SentenciaIfElseG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#SentenciaMientrasG4.
    def visitSentenciaMientrasG4(self, ctx:Gramatica_v3Parser.SentenciaMientrasG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#SentenciaForG4.
    def visitSentenciaForG4(self, ctx:Gramatica_v3Parser.SentenciaForG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#SentenciaImprimirG4.
    def visitSentenciaImprimirG4(self, ctx:Gramatica_v3Parser.SentenciaImprimirG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#SentenciaReturnG4.
    def visitSentenciaReturnG4(self, ctx:Gramatica_v3Parser.SentenciaReturnG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#SentenciaBreakG4.
    def visitSentenciaBreakG4(self, ctx:Gramatica_v3Parser.SentenciaBreakG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#SentenciaContinueG4.
    def visitSentenciaContinueG4(self, ctx:Gramatica_v3Parser.SentenciaContinueG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#StatBloqueG4.
    def visitStatBloqueG4(self, ctx:Gramatica_v3Parser.StatBloqueG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#SentenciaExpresionG4.
    def visitSentenciaExpresionG4(self, ctx:Gramatica_v3Parser.SentenciaExpresionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#bloque.
    def visitBloque(self, ctx:Gramatica_v3Parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#AsignacionCoreG4.
    def visitAsignacionCoreG4(self, ctx:Gramatica_v3Parser.AsignacionCoreG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#condicional.
    def visitCondicional(self, ctx:Gramatica_v3Parser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#bucle_mientras.
    def visitBucle_mientras(self, ctx:Gramatica_v3Parser.Bucle_mientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#bucle_for.
    def visitBucle_for(self, ctx:Gramatica_v3Parser.Bucle_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#impresion.
    def visitImpresion(self, ctx:Gramatica_v3Parser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#sentencia_return.
    def visitSentencia_return(self, ctx:Gramatica_v3Parser.Sentencia_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprRelacionalCompG4.
    def visitExprRelacionalCompG4(self, ctx:Gramatica_v3Parser.ExprRelacionalCompG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprPotenciaG4.
    def visitExprPotenciaG4(self, ctx:Gramatica_v3Parser.ExprPotenciaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprLogicaOrG4.
    def visitExprLogicaOrG4(self, ctx:Gramatica_v3Parser.ExprLogicaOrG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprAritmeticaSumaResG4.
    def visitExprAritmeticaSumaResG4(self, ctx:Gramatica_v3Parser.ExprAritmeticaSumaResG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprLlamadaFuncionG4.
    def visitExprLlamadaFuncionG4(self, ctx:Gramatica_v3Parser.ExprLlamadaFuncionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprArrayAccessG4.
    def visitExprArrayAccessG4(self, ctx:Gramatica_v3Parser.ExprArrayAccessG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprLogicaAndG4.
    def visitExprLogicaAndG4(self, ctx:Gramatica_v3Parser.ExprLogicaAndG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprAritmeticaMultDivModG4.
    def visitExprAritmeticaMultDivModG4(self, ctx:Gramatica_v3Parser.ExprAritmeticaMultDivModG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprLogicaNotG4.
    def visitExprLogicaNotG4(self, ctx:Gramatica_v3Parser.ExprLogicaNotG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprAgrupacionG4.
    def visitExprAgrupacionG4(self, ctx:Gramatica_v3Parser.ExprAgrupacionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprLiteralBoolG4.
    def visitExprLiteralBoolG4(self, ctx:Gramatica_v3Parser.ExprLiteralBoolG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprLiteralCadenaG4.
    def visitExprLiteralCadenaG4(self, ctx:Gramatica_v3Parser.ExprLiteralCadenaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprRelacionalIgualdadG4.
    def visitExprRelacionalIgualdadG4(self, ctx:Gramatica_v3Parser.ExprRelacionalIgualdadG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprReferenciaVariableG4.
    def visitExprReferenciaVariableG4(self, ctx:Gramatica_v3Parser.ExprReferenciaVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#ExprLiteralNumericaG4.
    def visitExprLiteralNumericaG4(self, ctx:Gramatica_v3Parser.ExprLiteralNumericaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Gramatica_v3Parser#args.
    def visitArgs(self, ctx:Gramatica_v3Parser.ArgsContext):
        return self.visitChildren(ctx)



del Gramatica_v3Parser