# Generated from gramatica_v4.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramatica_v4Parser import gramatica_v4Parser
else:
    from gramatica_v4Parser import gramatica_v4Parser

# This class defines a complete generic visitor for a parse tree produced by gramatica_v4Parser.

class gramatica_v4Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramatica_v4Parser#ProgramG4.
    def visitProgramG4(self, ctx:gramatica_v4Parser.ProgramG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#DeclVariableG4.
    def visitDeclVariableG4(self, ctx:gramatica_v4Parser.DeclVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#DeclFuncionG4.
    def visitDeclFuncionG4(self, ctx:gramatica_v4Parser.DeclFuncionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#DeclStructG4.
    def visitDeclStructG4(self, ctx:gramatica_v4Parser.DeclStructG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#DeclImportG4.
    def visitDeclImportG4(self, ctx:gramatica_v4Parser.DeclImportG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#DeclInstruccionG4.
    def visitDeclInstruccionG4(self, ctx:gramatica_v4Parser.DeclInstruccionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structDeclaration.
    def visitStructDeclaration(self, ctx:gramatica_v4Parser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#structField.
    def visitStructField(self, ctx:gramatica_v4Parser.StructFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#importacion.
    def visitImportacion(self, ctx:gramatica_v4Parser.ImportacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#VarDeclarationG4.
    def visitVarDeclarationG4(self, ctx:gramatica_v4Parser.VarDeclarationG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#VarArrayDeclarationG4.
    def visitVarArrayDeclarationG4(self, ctx:gramatica_v4Parser.VarArrayDeclarationG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#arrayLiteral.
    def visitArrayLiteral(self, ctx:gramatica_v4Parser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#FuncDeclarationG4.
    def visitFuncDeclarationG4(self, ctx:gramatica_v4Parser.FuncDeclarationG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#params.
    def visitParams(self, ctx:gramatica_v4Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#param.
    def visitParam(self, ctx:gramatica_v4Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#TypeIntG4.
    def visitTypeIntG4(self, ctx:gramatica_v4Parser.TypeIntG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#TypeFloatG4.
    def visitTypeFloatG4(self, ctx:gramatica_v4Parser.TypeFloatG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#TypeStringG4.
    def visitTypeStringG4(self, ctx:gramatica_v4Parser.TypeStringG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#TypeBoolG4.
    def visitTypeBoolG4(self, ctx:gramatica_v4Parser.TypeBoolG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#TypeVoidG4.
    def visitTypeVoidG4(self, ctx:gramatica_v4Parser.TypeVoidG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#TypeIntArrayG4.
    def visitTypeIntArrayG4(self, ctx:gramatica_v4Parser.TypeIntArrayG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#TypeStructG4.
    def visitTypeStructG4(self, ctx:gramatica_v4Parser.TypeStructG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#AsignacionVariableG4.
    def visitAsignacionVariableG4(self, ctx:gramatica_v4Parser.AsignacionVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaIfElseG4.
    def visitSentenciaIfElseG4(self, ctx:gramatica_v4Parser.SentenciaIfElseG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaSwitchG4.
    def visitSentenciaSwitchG4(self, ctx:gramatica_v4Parser.SentenciaSwitchG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaMientrasG4.
    def visitSentenciaMientrasG4(self, ctx:gramatica_v4Parser.SentenciaMientrasG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaForG4.
    def visitSentenciaForG4(self, ctx:gramatica_v4Parser.SentenciaForG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaImprimirG4.
    def visitSentenciaImprimirG4(self, ctx:gramatica_v4Parser.SentenciaImprimirG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaReturnG4.
    def visitSentenciaReturnG4(self, ctx:gramatica_v4Parser.SentenciaReturnG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaBreakG4.
    def visitSentenciaBreakG4(self, ctx:gramatica_v4Parser.SentenciaBreakG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaContinueG4.
    def visitSentenciaContinueG4(self, ctx:gramatica_v4Parser.SentenciaContinueG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#StatBloqueG4.
    def visitStatBloqueG4(self, ctx:gramatica_v4Parser.StatBloqueG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#SentenciaExpresionG4.
    def visitSentenciaExpresionG4(self, ctx:gramatica_v4Parser.SentenciaExpresionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#switchStatement.
    def visitSwitchStatement(self, ctx:gramatica_v4Parser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#caseStatement.
    def visitCaseStatement(self, ctx:gramatica_v4Parser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#defaultStatement.
    def visitDefaultStatement(self, ctx:gramatica_v4Parser.DefaultStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#bloque.
    def visitBloque(self, ctx:gramatica_v4Parser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#lvalue.
    def visitLvalue(self, ctx:gramatica_v4Parser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#AsignacionCoreG4.
    def visitAsignacionCoreG4(self, ctx:gramatica_v4Parser.AsignacionCoreG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#condicional.
    def visitCondicional(self, ctx:gramatica_v4Parser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#bucle_mientras.
    def visitBucle_mientras(self, ctx:gramatica_v4Parser.Bucle_mientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#bucle_for.
    def visitBucle_for(self, ctx:gramatica_v4Parser.Bucle_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#impresion.
    def visitImpresion(self, ctx:gramatica_v4Parser.ImpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#sentencia_return.
    def visitSentencia_return(self, ctx:gramatica_v4Parser.Sentencia_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprRelacionalCompG4.
    def visitExprRelacionalCompG4(self, ctx:gramatica_v4Parser.ExprRelacionalCompG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprPotenciaG4.
    def visitExprPotenciaG4(self, ctx:gramatica_v4Parser.ExprPotenciaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprLogicaOrG4.
    def visitExprLogicaOrG4(self, ctx:gramatica_v4Parser.ExprLogicaOrG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprTernarioG4.
    def visitExprTernarioG4(self, ctx:gramatica_v4Parser.ExprTernarioG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprAritmeticaSumaResG4.
    def visitExprAritmeticaSumaResG4(self, ctx:gramatica_v4Parser.ExprAritmeticaSumaResG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprLlamadaFuncionG4.
    def visitExprLlamadaFuncionG4(self, ctx:gramatica_v4Parser.ExprLlamadaFuncionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprArrayAccessG4.
    def visitExprArrayAccessG4(self, ctx:gramatica_v4Parser.ExprArrayAccessG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprLogicaAndG4.
    def visitExprLogicaAndG4(self, ctx:gramatica_v4Parser.ExprLogicaAndG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprAritmeticaMultDivModG4.
    def visitExprAritmeticaMultDivModG4(self, ctx:gramatica_v4Parser.ExprAritmeticaMultDivModG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprAccesoCampoG4.
    def visitExprAccesoCampoG4(self, ctx:gramatica_v4Parser.ExprAccesoCampoG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprLogicaNotG4.
    def visitExprLogicaNotG4(self, ctx:gramatica_v4Parser.ExprLogicaNotG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprAgrupacionG4.
    def visitExprAgrupacionG4(self, ctx:gramatica_v4Parser.ExprAgrupacionG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprLiteralBoolG4.
    def visitExprLiteralBoolG4(self, ctx:gramatica_v4Parser.ExprLiteralBoolG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprCastingG4.
    def visitExprCastingG4(self, ctx:gramatica_v4Parser.ExprCastingG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprLiteralCadenaG4.
    def visitExprLiteralCadenaG4(self, ctx:gramatica_v4Parser.ExprLiteralCadenaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprRelacionalIgualdadG4.
    def visitExprRelacionalIgualdadG4(self, ctx:gramatica_v4Parser.ExprRelacionalIgualdadG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprReferenciaVariableG4.
    def visitExprReferenciaVariableG4(self, ctx:gramatica_v4Parser.ExprReferenciaVariableG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#ExprLiteralNumericaG4.
    def visitExprLiteralNumericaG4(self, ctx:gramatica_v4Parser.ExprLiteralNumericaG4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramatica_v4Parser#args.
    def visitArgs(self, ctx:gramatica_v4Parser.ArgsContext):
        return self.visitChildren(ctx)



del gramatica_v4Parser