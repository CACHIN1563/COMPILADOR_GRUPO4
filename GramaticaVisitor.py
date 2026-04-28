# Generated from Gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#ProgramG4.
    def visitProgramG4(self, ctx:GramaticaParser.ProgramG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#DeclVariableG4.
    def visitDeclVariableG4(self, ctx:GramaticaParser.DeclVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#DeclFuncionG4.
    def visitDeclFuncionG4(self, ctx:GramaticaParser.DeclFuncionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#DeclInstruccionG4.
    def visitDeclInstruccionG4(self, ctx:GramaticaParser.DeclInstruccionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#VarDeclarationG4.
    def visitVarDeclarationG4(self, ctx:GramaticaParser.VarDeclarationG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#FuncDeclarationG4.
    def visitFuncDeclarationG4(self, ctx:GramaticaParser.FuncDeclarationG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#params.
    def visitParams(self, ctx:GramaticaParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#param.
    def visitParam(self, ctx:GramaticaParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#TypeIntG4.
    def visitTypeIntG4(self, ctx:GramaticaParser.TypeIntG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#TypeFloatG4.
    def visitTypeFloatG4(self, ctx:GramaticaParser.TypeFloatG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#TypeStringG4.
    def visitTypeStringG4(self, ctx:GramaticaParser.TypeStringG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#TypeBoolG4.
    def visitTypeBoolG4(self, ctx:GramaticaParser.TypeBoolG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#TypeVoidG4.
    def visitTypeVoidG4(self, ctx:GramaticaParser.TypeVoidG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#AsignacionVariableG4.
    def visitAsignacionVariableG4(self, ctx:GramaticaParser.AsignacionVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#SentenciaIfElseG4.
    def visitSentenciaIfElseG4(self, ctx:GramaticaParser.SentenciaIfElseG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#SentenciaMientrasG4.
    def visitSentenciaMientrasG4(self, ctx:GramaticaParser.SentenciaMientrasG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#SentenciaForG4.
    def visitSentenciaForG4(self, ctx:GramaticaParser.SentenciaForG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#SentenciaImprimirG4.
    def visitSentenciaImprimirG4(self, ctx:GramaticaParser.SentenciaImprimirG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#SentenciaReturnG4.
    def visitSentenciaReturnG4(self, ctx:GramaticaParser.SentenciaReturnG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#StatBloqueG4.
    def visitStatBloqueG4(self, ctx:GramaticaParser.StatBloqueG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#SentenciaExpresionG4.
    def visitSentenciaExpresionG4(self, ctx:GramaticaParser.SentenciaExpresionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#bloque.
    def visitBloque(self, ctx:GramaticaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#AsignacionCoreG4.
    def visitAsignacionCoreG4(self, ctx:GramaticaParser.AsignacionCoreG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#condicional.
    def visitCondicional(self, ctx:GramaticaParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#bucle_mientras.
    def visitBucle_mientras(self, ctx:GramaticaParser.Bucle_mientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#bucle_for.
    def visitBucle_for(self, ctx:GramaticaParser.Bucle_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#impresion.
    def visitImpresion(self, ctx:GramaticaParser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#sentencia_return.
    def visitSentencia_return(self, ctx:GramaticaParser.Sentencia_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprRelacionalCompG4.
    def visitExprRelacionalCompG4(self, ctx:GramaticaParser.ExprRelacionalCompG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprPotenciaG4.
    def visitExprPotenciaG4(self, ctx:GramaticaParser.ExprPotenciaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprLogicaOrG4.
    def visitExprLogicaOrG4(self, ctx:GramaticaParser.ExprLogicaOrG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprAritmeticaMultDivG4.
    def visitExprAritmeticaMultDivG4(self, ctx:GramaticaParser.ExprAritmeticaMultDivG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprAritmeticaSumaResG4.
    def visitExprAritmeticaSumaResG4(self, ctx:GramaticaParser.ExprAritmeticaSumaResG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprLlamadaFuncionG4.
    def visitExprLlamadaFuncionG4(self, ctx:GramaticaParser.ExprLlamadaFuncionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprLogicaAndG4.
    def visitExprLogicaAndG4(self, ctx:GramaticaParser.ExprLogicaAndG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprLogicaNotG4.
    def visitExprLogicaNotG4(self, ctx:GramaticaParser.ExprLogicaNotG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprAgrupacionG4.
    def visitExprAgrupacionG4(self, ctx:GramaticaParser.ExprAgrupacionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprLiteralBoolG4.
    def visitExprLiteralBoolG4(self, ctx:GramaticaParser.ExprLiteralBoolG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprLiteralCadenaG4.
    def visitExprLiteralCadenaG4(self, ctx:GramaticaParser.ExprLiteralCadenaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprRelacionalIgualdadG4.
    def visitExprRelacionalIgualdadG4(self, ctx:GramaticaParser.ExprRelacionalIgualdadG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprReferenciaVariableG4.
    def visitExprReferenciaVariableG4(self, ctx:GramaticaParser.ExprReferenciaVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#ExprLiteralNumericaG4.
    def visitExprLiteralNumericaG4(self, ctx:GramaticaParser.ExprLiteralNumericaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#args.
    def visitArgs(self, ctx:GramaticaParser.ArgsContext):
        return self.visitChildren(ctx)



del GramaticaParser