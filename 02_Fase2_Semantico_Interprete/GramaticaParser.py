# Generated from Gramatica.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


# Módulo de Árbol Sintáctico - Lógica de Estructura G4

def serializedATN():
    return [
        4,1,44,215,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,1,0,5,0,39,8,0,10,0,12,
        0,42,9,0,1,0,1,0,1,0,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,3,2,
        56,8,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,64,8,3,1,3,1,3,1,3,1,4,1,4,1,
        4,5,4,72,8,4,10,4,12,4,75,9,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,
        6,85,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,99,
        8,7,1,8,1,8,5,8,103,8,8,10,8,12,8,106,9,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,122,8,10,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,137,
        8,12,1,12,3,12,140,8,12,1,12,1,12,1,12,3,12,145,8,12,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,3,14,158,8,14,1,14,1,
        14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,
        15,3,15,175,8,15,1,15,1,15,3,15,179,8,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,5,15,202,8,15,10,15,12,15,205,9,15,1,16,1,16,1,16,
        5,16,210,8,16,10,16,12,16,213,9,16,1,16,0,1,30,17,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,0,5,1,0,37,38,1,0,3,4,1,0,1,2,1,0,
        8,11,1,0,6,7,237,0,34,1,0,0,0,2,49,1,0,0,0,4,51,1,0,0,0,6,59,1,0,
        0,0,8,68,1,0,0,0,10,76,1,0,0,0,12,84,1,0,0,0,14,98,1,0,0,0,16,100,
        1,0,0,0,18,109,1,0,0,0,20,113,1,0,0,0,22,123,1,0,0,0,24,129,1,0,
        0,0,26,149,1,0,0,0,28,155,1,0,0,0,30,178,1,0,0,0,32,206,1,0,0,0,
        34,35,5,22,0,0,35,36,5,41,0,0,36,40,5,23,0,0,37,39,3,2,1,0,38,37,
        1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,
        42,40,1,0,0,0,43,44,5,24,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,50,3,
        4,2,0,47,50,3,6,3,0,48,50,3,14,7,0,49,46,1,0,0,0,49,47,1,0,0,0,49,
        48,1,0,0,0,50,3,1,0,0,0,51,52,3,12,6,0,52,55,5,41,0,0,53,54,5,15,
        0,0,54,56,3,30,15,0,55,53,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,
        58,5,16,0,0,58,5,1,0,0,0,59,60,3,12,6,0,60,61,5,41,0,0,61,63,5,18,
        0,0,62,64,3,8,4,0,63,62,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,
        5,19,0,0,66,67,3,16,8,0,67,7,1,0,0,0,68,73,3,10,5,0,69,70,5,17,0,
        0,70,72,3,10,5,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,
        1,0,0,0,74,9,1,0,0,0,75,73,1,0,0,0,76,77,3,12,6,0,77,78,5,41,0,0,
        78,11,1,0,0,0,79,85,5,32,0,0,80,85,5,33,0,0,81,85,5,34,0,0,82,85,
        5,35,0,0,83,85,5,36,0,0,84,79,1,0,0,0,84,80,1,0,0,0,84,81,1,0,0,
        0,84,82,1,0,0,0,84,83,1,0,0,0,85,13,1,0,0,0,86,87,3,18,9,0,87,88,
        5,16,0,0,88,99,1,0,0,0,89,99,3,20,10,0,90,99,3,22,11,0,91,99,3,24,
        12,0,92,99,3,26,13,0,93,99,3,28,14,0,94,99,3,16,8,0,95,96,3,30,15,
        0,96,97,5,16,0,0,97,99,1,0,0,0,98,86,1,0,0,0,98,89,1,0,0,0,98,90,
        1,0,0,0,98,91,1,0,0,0,98,92,1,0,0,0,98,93,1,0,0,0,98,94,1,0,0,0,
        98,95,1,0,0,0,99,15,1,0,0,0,100,104,5,20,0,0,101,103,3,14,7,0,102,
        101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,
        107,1,0,0,0,106,104,1,0,0,0,107,108,5,21,0,0,108,17,1,0,0,0,109,
        110,5,41,0,0,110,111,5,15,0,0,111,112,3,30,15,0,112,19,1,0,0,0,113,
        114,5,25,0,0,114,115,5,18,0,0,115,116,3,30,15,0,116,117,5,19,0,0,
        117,118,5,26,0,0,118,121,3,16,8,0,119,120,5,27,0,0,120,122,3,16,
        8,0,121,119,1,0,0,0,121,122,1,0,0,0,122,21,1,0,0,0,123,124,5,28,
        0,0,124,125,5,18,0,0,125,126,3,30,15,0,126,127,5,19,0,0,127,128,
        3,16,8,0,128,23,1,0,0,0,129,130,5,29,0,0,130,136,5,18,0,0,131,137,
        3,4,2,0,132,133,3,18,9,0,133,134,5,16,0,0,134,137,1,0,0,0,135,137,
        5,16,0,0,136,131,1,0,0,0,136,132,1,0,0,0,136,135,1,0,0,0,137,139,
        1,0,0,0,138,140,3,30,15,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,
        1,0,0,0,141,144,5,16,0,0,142,145,3,18,9,0,143,145,3,30,15,0,144,
        142,1,0,0,0,144,143,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,
        147,5,19,0,0,147,148,3,16,8,0,148,25,1,0,0,0,149,150,5,30,0,0,150,
        151,5,18,0,0,151,152,3,30,15,0,152,153,5,19,0,0,153,154,5,16,0,0,
        154,27,1,0,0,0,155,157,5,31,0,0,156,158,3,30,15,0,157,156,1,0,0,
        0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,16,0,0,160,29,1,0,0,
        0,161,162,6,15,-1,0,162,163,5,14,0,0,163,179,3,30,15,14,164,165,
        5,18,0,0,165,166,3,30,15,0,166,167,5,19,0,0,167,179,1,0,0,0,168,
        179,5,39,0,0,169,179,5,40,0,0,170,179,7,0,0,0,171,172,5,41,0,0,172,
        174,5,18,0,0,173,175,3,32,16,0,174,173,1,0,0,0,174,175,1,0,0,0,175,
        176,1,0,0,0,176,179,5,19,0,0,177,179,5,41,0,0,178,161,1,0,0,0,178,
        164,1,0,0,0,178,168,1,0,0,0,178,169,1,0,0,0,178,170,1,0,0,0,178,
        171,1,0,0,0,178,177,1,0,0,0,179,203,1,0,0,0,180,181,10,13,0,0,181,
        182,5,5,0,0,182,202,3,30,15,13,183,184,10,12,0,0,184,185,7,1,0,0,
        185,202,3,30,15,13,186,187,10,11,0,0,187,188,7,2,0,0,188,202,3,30,
        15,12,189,190,10,10,0,0,190,191,7,3,0,0,191,202,3,30,15,11,192,193,
        10,9,0,0,193,194,7,4,0,0,194,202,3,30,15,10,195,196,10,8,0,0,196,
        197,5,12,0,0,197,202,3,30,15,9,198,199,10,7,0,0,199,200,5,13,0,0,
        200,202,3,30,15,8,201,180,1,0,0,0,201,183,1,0,0,0,201,186,1,0,0,
        0,201,189,1,0,0,0,201,192,1,0,0,0,201,195,1,0,0,0,201,198,1,0,0,
        0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,31,1,0,0,0,
        205,203,1,0,0,0,206,211,3,30,15,0,207,208,5,17,0,0,208,210,3,30,
        15,0,209,207,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,1,0,
        0,0,212,33,1,0,0,0,213,211,1,0,0,0,18,40,49,55,63,73,84,98,104,121,
        136,139,144,157,174,178,201,203,211
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'^'", "'=='", 
                     "<INVALID>", "'>'", "'<'", "'>='", "'<='", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "';'", "','", "'('", 
                     "')'", "'{'", "'}'", "'PROGRAMA'", "'INICIO'", "'FIN'", 
                     "'SI'", "'ENTONCES'", "'SINO'", "'MIENTRAS'", "'FOR'", 
                     "'IMPRIMIR'", "'RETORNAR'", "'INT'", "'FLOAT'", "'STRING'", 
                     "'BOOL'", "'VOID'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "TK_SUMA", "TK_RESTA", "TK_MULT", "TK_DIV", 
                      "TK_POTENCIA", "TK_IGUAL", "TK_DIFERENTE", "TK_MAYOR", 
                      "TK_MENOR", "TK_MAYOREQ", "TK_MENOREQ", "TK_Y", "TK_O", 
                      "TK_NOT", "ASSIGN", "SEMICOLON", "TK_COMA", "TK_PAR_IZQ", 
                      "TK_PAR_DER", "TK_LLA_IZQ", "TK_LLA_DER", "TK_PROGRAMA", 
                      "TK_INICIO", "TK_FIN", "TK_SI", "TK_ENTONCES", "TK_SINO", 
                      "TK_MIENTRAS", "TK_FOR", "TK_IMPRIMIR", "TK_RETURN", 
                      "TK_INT", "TK_FLOAT", "TK_STRING", "TK_BOOL", "TK_VOID", 
                      "TK_TRUE", "TK_FALSE", "TK_NUMERO", "TK_CADENA", "TK_ID", 
                      "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_varDeclaration = 2
    RULE_funcDeclaration = 3
    RULE_params = 4
    RULE_param = 5
    RULE_type_ = 6
    RULE_instruccion = 7
    RULE_bloque = 8
    RULE_asignacion_core = 9
    RULE_condicional = 10
    RULE_bucle_mientras = 11
    RULE_bucle_for = 12
    RULE_impresion = 13
    RULE_sentencia_return = 14
    RULE_expr = 15
    RULE_args = 16

    ruleNames =  [ "program", "declaration", "varDeclaration", "funcDeclaration", 
                   "params", "param", "type_", "instruccion", "bloque", 
                   "asignacion_core", "condicional", "bucle_mientras", "bucle_for", 
                   "impresion", "sentencia_return", "expr", "args" ]

    EOF = Token.EOF
    TK_SUMA=1
    TK_RESTA=2
    TK_MULT=3
    TK_DIV=4
    TK_POTENCIA=5
    TK_IGUAL=6
    TK_DIFERENTE=7
    TK_MAYOR=8
    TK_MENOR=9
    TK_MAYOREQ=10
    TK_MENOREQ=11
    TK_Y=12
    TK_O=13
    TK_NOT=14
    ASSIGN=15
    SEMICOLON=16
    TK_COMA=17
    TK_PAR_IZQ=18
    TK_PAR_DER=19
    TK_LLA_IZQ=20
    TK_LLA_DER=21
    TK_PROGRAMA=22
    TK_INICIO=23
    TK_FIN=24
    TK_SI=25
    TK_ENTONCES=26
    TK_SINO=27
    TK_MIENTRAS=28
    TK_FOR=29
    TK_IMPRIMIR=30
    TK_RETURN=31
    TK_INT=32
    TK_FLOAT=33
    TK_STRING=34
    TK_BOOL=35
    TK_VOID=36
    TK_TRUE=37
    TK_FALSE=38
    TK_NUMERO=39
    TK_CADENA=40
    TK_ID=41
    WS=42
    COMMENT=43
    BLOCK_COMMENT=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramG4Context(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_PROGRAMA(self):
            return self.getToken(GramaticaParser.TK_PROGRAMA, 0)
        def TK_ID(self):
            return self.getToken(GramaticaParser.TK_ID, 0)
        def TK_INICIO(self):
            return self.getToken(GramaticaParser.TK_INICIO, 0)
        def TK_FIN(self):
            return self.getToken(GramaticaParser.TK_FIN, 0)
        def EOF(self):
            return self.getToken(GramaticaParser.EOF, 0)
        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.DeclarationContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramG4" ):
                listener.enterProgramG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramG4" ):
                listener.exitProgramG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramG4" ):
                return visitor.visitProgramG4(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = GramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = GramaticaParser.ProgramG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(GramaticaParser.TK_PROGRAMA)
            self.state = 35
            self.match(GramaticaParser.TK_ID)
            self.state = 36
            self.match(GramaticaParser.TK_INICIO)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4397812957184) != 0):
                self.state = 37
                self.declaration()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(GramaticaParser.TK_FIN)
            self.state = 44
            self.match(GramaticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclInstruccionG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instruccion(self):
            return self.getTypedRuleContext(GramaticaParser.InstruccionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclInstruccionG4" ):
                listener.enterDeclInstruccionG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclInstruccionG4" ):
                listener.exitDeclInstruccionG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclInstruccionG4" ):
                return visitor.visitDeclInstruccionG4(self)
            else:
                return visitor.visitChildren(self)


    class DeclVariableG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDeclaration(self):
            return self.getTypedRuleContext(GramaticaParser.VarDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclVariableG4" ):
                listener.enterDeclVariableG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclVariableG4" ):
                listener.exitDeclVariableG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclVariableG4" ):
                return visitor.visitDeclVariableG4(self)
            else:
                return visitor.visitChildren(self)


    class DeclFuncionG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcDeclaration(self):
            return self.getTypedRuleContext(GramaticaParser.FuncDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclFuncionG4" ):
                listener.enterDeclFuncionG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclFuncionG4" ):
                listener.exitDeclFuncionG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclFuncionG4" ):
                return visitor.visitDeclFuncionG4(self)
            else:
                return visitor.visitChildren(self)



    def declaration(self):

        localctx = GramaticaParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = GramaticaParser.DeclVariableG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.varDeclaration()
                pass

            elif la_ == 2:
                localctx = GramaticaParser.DeclFuncionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.funcDeclaration()
                pass

            elif la_ == 3:
                localctx = GramaticaParser.DeclInstruccionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_varDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarDeclarationG4Context(VarDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.VarDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(GramaticaParser.Type_Context,0)

        def TK_ID(self):
            return self.getToken(GramaticaParser.TK_ID, 0)
        def SEMICOLON(self):
            return self.getToken(GramaticaParser.SEMICOLON, 0)
        def ASSIGN(self):
            return self.getToken(GramaticaParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclarationG4" ):
                listener.enterVarDeclarationG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclarationG4" ):
                listener.exitVarDeclarationG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclarationG4" ):
                return visitor.visitVarDeclarationG4(self)
            else:
                return visitor.visitChildren(self)



    def varDeclaration(self):

        localctx = GramaticaParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            localctx = GramaticaParser.VarDeclarationG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.type_()
            self.state = 52
            self.match(GramaticaParser.TK_ID)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 53
                self.match(GramaticaParser.ASSIGN)
                self.state = 54
                self.expr(0)


            self.state = 57
            self.match(GramaticaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_funcDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncDeclarationG4Context(FuncDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.FuncDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(GramaticaParser.Type_Context,0)

        def TK_ID(self):
            return self.getToken(GramaticaParser.TK_ID, 0)
        def TK_PAR_IZQ(self):
            return self.getToken(GramaticaParser.TK_PAR_IZQ, 0)
        def TK_PAR_DER(self):
            return self.getToken(GramaticaParser.TK_PAR_DER, 0)
        def bloque(self):
            return self.getTypedRuleContext(GramaticaParser.BloqueContext,0)

        def params(self):
            return self.getTypedRuleContext(GramaticaParser.ParamsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDeclarationG4" ):
                listener.enterFuncDeclarationG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDeclarationG4" ):
                listener.exitFuncDeclarationG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclarationG4" ):
                return visitor.visitFuncDeclarationG4(self)
            else:
                return visitor.visitChildren(self)



    def funcDeclaration(self):

        localctx = GramaticaParser.FuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcDeclaration)
        self._la = 0 # Token type
        try:
            localctx = GramaticaParser.FuncDeclarationG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.type_()
            self.state = 60
            self.match(GramaticaParser.TK_ID)
            self.state = 61
            self.match(GramaticaParser.TK_PAR_IZQ)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 133143986176) != 0):
                self.state = 62
                self.params()


            self.state = 65
            self.match(GramaticaParser.TK_PAR_DER)
            self.state = 66
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ParamContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ParamContext,i)


        def TK_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.TK_COMA)
            else:
                return self.getToken(GramaticaParser.TK_COMA, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = GramaticaParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.param()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 69
                self.match(GramaticaParser.TK_COMA)
                self.state = 70
                self.param()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GramaticaParser.Type_Context,0)


        def TK_ID(self):
            return self.getToken(GramaticaParser.TK_ID, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = GramaticaParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.type_()
            self.state = 77
            self.match(GramaticaParser.TK_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_type_

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeVoidG4Context(Type_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.Type_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_VOID(self):
            return self.getToken(GramaticaParser.TK_VOID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeVoidG4" ):
                listener.enterTypeVoidG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeVoidG4" ):
                listener.exitTypeVoidG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVoidG4" ):
                return visitor.visitTypeVoidG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeStringG4Context(Type_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.Type_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_STRING(self):
            return self.getToken(GramaticaParser.TK_STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeStringG4" ):
                listener.enterTypeStringG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeStringG4" ):
                listener.exitTypeStringG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeStringG4" ):
                return visitor.visitTypeStringG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeBoolG4Context(Type_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.Type_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_BOOL(self):
            return self.getToken(GramaticaParser.TK_BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeBoolG4" ):
                listener.enterTypeBoolG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeBoolG4" ):
                listener.exitTypeBoolG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBoolG4" ):
                return visitor.visitTypeBoolG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeIntG4Context(Type_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.Type_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_INT(self):
            return self.getToken(GramaticaParser.TK_INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeIntG4" ):
                listener.enterTypeIntG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeIntG4" ):
                listener.exitTypeIntG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeIntG4" ):
                return visitor.visitTypeIntG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeFloatG4Context(Type_Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.Type_Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_FLOAT(self):
            return self.getToken(GramaticaParser.TK_FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeFloatG4" ):
                listener.enterTypeFloatG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeFloatG4" ):
                listener.exitTypeFloatG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeFloatG4" ):
                return visitor.visitTypeFloatG4(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = GramaticaParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type_)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                localctx = GramaticaParser.TypeIntG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(GramaticaParser.TK_INT)
                pass
            elif token in [33]:
                localctx = GramaticaParser.TypeFloatG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.match(GramaticaParser.TK_FLOAT)
                pass
            elif token in [34]:
                localctx = GramaticaParser.TypeStringG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.match(GramaticaParser.TK_STRING)
                pass
            elif token in [35]:
                localctx = GramaticaParser.TypeBoolG4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.match(GramaticaParser.TK_BOOL)
                pass
            elif token in [36]:
                localctx = GramaticaParser.TypeVoidG4Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 83
                self.match(GramaticaParser.TK_VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_instruccion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SentenciaForG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bucle_for(self):
            return self.getTypedRuleContext(GramaticaParser.Bucle_forContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaForG4" ):
                listener.enterSentenciaForG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaForG4" ):
                listener.exitSentenciaForG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaForG4" ):
                return visitor.visitSentenciaForG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaImprimirG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def impresion(self):
            return self.getTypedRuleContext(GramaticaParser.ImpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaImprimirG4" ):
                listener.enterSentenciaImprimirG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaImprimirG4" ):
                listener.exitSentenciaImprimirG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaImprimirG4" ):
                return visitor.visitSentenciaImprimirG4(self)
            else:
                return visitor.visitChildren(self)


    class StatBloqueG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bloque(self):
            return self.getTypedRuleContext(GramaticaParser.BloqueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatBloqueG4" ):
                listener.enterStatBloqueG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatBloqueG4" ):
                listener.exitStatBloqueG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatBloqueG4" ):
                return visitor.visitStatBloqueG4(self)
            else:
                return visitor.visitChildren(self)


    class AsignacionVariableG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asignacion_core(self):
            return self.getTypedRuleContext(GramaticaParser.Asignacion_coreContext,0)

        def SEMICOLON(self):
            return self.getToken(GramaticaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionVariableG4" ):
                listener.enterAsignacionVariableG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionVariableG4" ):
                listener.exitAsignacionVariableG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionVariableG4" ):
                return visitor.visitAsignacionVariableG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaExpresionG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)

        def SEMICOLON(self):
            return self.getToken(GramaticaParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaExpresionG4" ):
                listener.enterSentenciaExpresionG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaExpresionG4" ):
                listener.exitSentenciaExpresionG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaExpresionG4" ):
                return visitor.visitSentenciaExpresionG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaIfElseG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicional(self):
            return self.getTypedRuleContext(GramaticaParser.CondicionalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaIfElseG4" ):
                listener.enterSentenciaIfElseG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaIfElseG4" ):
                listener.exitSentenciaIfElseG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaIfElseG4" ):
                return visitor.visitSentenciaIfElseG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaMientrasG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bucle_mientras(self):
            return self.getTypedRuleContext(GramaticaParser.Bucle_mientrasContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaMientrasG4" ):
                listener.enterSentenciaMientrasG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaMientrasG4" ):
                listener.exitSentenciaMientrasG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaMientrasG4" ):
                return visitor.visitSentenciaMientrasG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaReturnG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sentencia_return(self):
            return self.getTypedRuleContext(GramaticaParser.Sentencia_returnContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaReturnG4" ):
                listener.enterSentenciaReturnG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaReturnG4" ):
                listener.exitSentenciaReturnG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaReturnG4" ):
                return visitor.visitSentenciaReturnG4(self)
            else:
                return visitor.visitChildren(self)



    def instruccion(self):

        localctx = GramaticaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instruccion)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = GramaticaParser.AsignacionVariableG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.asignacion_core()
                self.state = 87
                self.match(GramaticaParser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = GramaticaParser.SentenciaIfElseG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.condicional()
                pass

            elif la_ == 3:
                localctx = GramaticaParser.SentenciaMientrasG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.bucle_mientras()
                pass

            elif la_ == 4:
                localctx = GramaticaParser.SentenciaForG4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.bucle_for()
                pass

            elif la_ == 5:
                localctx = GramaticaParser.SentenciaImprimirG4Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.impresion()
                pass

            elif la_ == 6:
                localctx = GramaticaParser.SentenciaReturnG4Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.sentencia_return()
                pass

            elif la_ == 7:
                localctx = GramaticaParser.StatBloqueG4Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 94
                self.bloque()
                pass

            elif la_ == 8:
                localctx = GramaticaParser.SentenciaExpresionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 95
                self.expr(0)
                self.state = 96
                self.match(GramaticaParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_LLA_IZQ(self):
            return self.getToken(GramaticaParser.TK_LLA_IZQ, 0)

        def TK_LLA_DER(self):
            return self.getToken(GramaticaParser.TK_LLA_DER, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = GramaticaParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(GramaticaParser.TK_LLA_IZQ)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4264668971008) != 0):
                self.state = 101
                self.instruccion()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(GramaticaParser.TK_LLA_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Asignacion_coreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_asignacion_core

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionCoreG4Context(Asignacion_coreContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.Asignacion_coreContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(GramaticaParser.TK_ID, 0)
        def ASSIGN(self):
            return self.getToken(GramaticaParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacionCoreG4" ):
                listener.enterAsignacionCoreG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacionCoreG4" ):
                listener.exitAsignacionCoreG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionCoreG4" ):
                return visitor.visitAsignacionCoreG4(self)
            else:
                return visitor.visitChildren(self)



    def asignacion_core(self):

        localctx = GramaticaParser.Asignacion_coreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_asignacion_core)
        try:
            localctx = GramaticaParser.AsignacionCoreG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(GramaticaParser.TK_ID)
            self.state = 110
            self.match(GramaticaParser.ASSIGN)
            self.state = 111
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_SI(self):
            return self.getToken(GramaticaParser.TK_SI, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(GramaticaParser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(GramaticaParser.TK_PAR_DER, 0)

        def TK_ENTONCES(self):
            return self.getToken(GramaticaParser.TK_ENTONCES, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.BloqueContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.BloqueContext,i)


        def TK_SINO(self):
            return self.getToken(GramaticaParser.TK_SINO, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = GramaticaParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(GramaticaParser.TK_SI)
            self.state = 114
            self.match(GramaticaParser.TK_PAR_IZQ)
            self.state = 115
            self.expr(0)
            self.state = 116
            self.match(GramaticaParser.TK_PAR_DER)
            self.state = 117
            self.match(GramaticaParser.TK_ENTONCES)
            self.state = 118
            self.bloque()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 119
                self.match(GramaticaParser.TK_SINO)
                self.state = 120
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bucle_mientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_MIENTRAS(self):
            return self.getToken(GramaticaParser.TK_MIENTRAS, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(GramaticaParser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(GramaticaParser.TK_PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(GramaticaParser.BloqueContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_bucle_mientras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBucle_mientras" ):
                listener.enterBucle_mientras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBucle_mientras" ):
                listener.exitBucle_mientras(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBucle_mientras" ):
                return visitor.visitBucle_mientras(self)
            else:
                return visitor.visitChildren(self)




    def bucle_mientras(self):

        localctx = GramaticaParser.Bucle_mientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_bucle_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(GramaticaParser.TK_MIENTRAS)
            self.state = 124
            self.match(GramaticaParser.TK_PAR_IZQ)
            self.state = 125
            self.expr(0)
            self.state = 126
            self.match(GramaticaParser.TK_PAR_DER)
            self.state = 127
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bucle_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.init_var = None # VarDeclarationContext
            self.init_assign = None # Asignacion_coreContext
            self.cond = None # ExprContext
            self.update_assign = None # Asignacion_coreContext
            self.update_expr = None # ExprContext

        def TK_FOR(self):
            return self.getToken(GramaticaParser.TK_FOR, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(GramaticaParser.TK_PAR_IZQ, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.SEMICOLON)
            else:
                return self.getToken(GramaticaParser.SEMICOLON, i)

        def TK_PAR_DER(self):
            return self.getToken(GramaticaParser.TK_PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(GramaticaParser.BloqueContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(GramaticaParser.VarDeclarationContext,0)


        def asignacion_core(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.Asignacion_coreContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.Asignacion_coreContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def getRuleIndex(self):
            return GramaticaParser.RULE_bucle_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBucle_for" ):
                listener.enterBucle_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBucle_for" ):
                listener.exitBucle_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBucle_for" ):
                return visitor.visitBucle_for(self)
            else:
                return visitor.visitChildren(self)




    def bucle_for(self):

        localctx = GramaticaParser.Bucle_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_bucle_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(GramaticaParser.TK_FOR)
            self.state = 130
            self.match(GramaticaParser.TK_PAR_IZQ)
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 33, 34, 35, 36]:
                self.state = 131
                localctx.init_var = self.varDeclaration()
                pass
            elif token in [41]:
                self.state = 132
                localctx.init_assign = self.asignacion_core()
                self.state = 133
                self.match(GramaticaParser.SEMICOLON)
                pass
            elif token in [16]:
                self.state = 135
                self.match(GramaticaParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4260607836160) != 0):
                self.state = 138
                localctx.cond = self.expr(0)


            self.state = 141
            self.match(GramaticaParser.SEMICOLON)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 142
                localctx.update_assign = self.asignacion_core()

            elif la_ == 2:
                self.state = 143
                localctx.update_expr = self.expr(0)


            self.state = 146
            self.match(GramaticaParser.TK_PAR_DER)
            self.state = 147
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_IMPRIMIR(self):
            return self.getToken(GramaticaParser.TK_IMPRIMIR, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(GramaticaParser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(GramaticaParser.TK_PAR_DER, 0)

        def SEMICOLON(self):
            return self.getToken(GramaticaParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_impresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpresion" ):
                listener.enterImpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpresion" ):
                listener.exitImpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpresion" ):
                return visitor.visitImpresion(self)
            else:
                return visitor.visitChildren(self)




    def impresion(self):

        localctx = GramaticaParser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(GramaticaParser.TK_IMPRIMIR)
            self.state = 150
            self.match(GramaticaParser.TK_PAR_IZQ)
            self.state = 151
            self.expr(0)
            self.state = 152
            self.match(GramaticaParser.TK_PAR_DER)
            self.state = 153
            self.match(GramaticaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sentencia_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_RETURN(self):
            return self.getToken(GramaticaParser.TK_RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(GramaticaParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_sentencia_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia_return" ):
                listener.enterSentencia_return(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia_return" ):
                listener.exitSentencia_return(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_return" ):
                return visitor.visitSentencia_return(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_return(self):

        localctx = GramaticaParser.Sentencia_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sentencia_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(GramaticaParser.TK_RETURN)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4260607836160) != 0):
                self.state = 156
                self.expr(0)


            self.state = 159
            self.match(GramaticaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramaticaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprRelacionalCompG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)

        def TK_MAYOR(self):
            return self.getToken(GramaticaParser.TK_MAYOR, 0)
        def TK_MENOR(self):
            return self.getToken(GramaticaParser.TK_MENOR, 0)
        def TK_MAYOREQ(self):
            return self.getToken(GramaticaParser.TK_MAYOREQ, 0)
        def TK_MENOREQ(self):
            return self.getToken(GramaticaParser.TK_MENOREQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRelacionalCompG4" ):
                listener.enterExprRelacionalCompG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRelacionalCompG4" ):
                listener.exitExprRelacionalCompG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelacionalCompG4" ):
                return visitor.visitExprRelacionalCompG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprPotenciaG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)

        def TK_POTENCIA(self):
            return self.getToken(GramaticaParser.TK_POTENCIA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPotenciaG4" ):
                listener.enterExprPotenciaG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPotenciaG4" ):
                listener.exitExprPotenciaG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPotenciaG4" ):
                return visitor.visitExprPotenciaG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicaOrG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)

        def TK_O(self):
            return self.getToken(GramaticaParser.TK_O, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogicaOrG4" ):
                listener.enterExprLogicaOrG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogicaOrG4" ):
                listener.exitExprLogicaOrG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicaOrG4" ):
                return visitor.visitExprLogicaOrG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprAritmeticaMultDivG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)

        def TK_MULT(self):
            return self.getToken(GramaticaParser.TK_MULT, 0)
        def TK_DIV(self):
            return self.getToken(GramaticaParser.TK_DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritmeticaMultDivG4" ):
                listener.enterExprAritmeticaMultDivG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritmeticaMultDivG4" ):
                listener.exitExprAritmeticaMultDivG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritmeticaMultDivG4" ):
                return visitor.visitExprAritmeticaMultDivG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprAritmeticaSumaResG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)

        def TK_SUMA(self):
            return self.getToken(GramaticaParser.TK_SUMA, 0)
        def TK_RESTA(self):
            return self.getToken(GramaticaParser.TK_RESTA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritmeticaSumaResG4" ):
                listener.enterExprAritmeticaSumaResG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritmeticaSumaResG4" ):
                listener.exitExprAritmeticaSumaResG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritmeticaSumaResG4" ):
                return visitor.visitExprAritmeticaSumaResG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLlamadaFuncionG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(GramaticaParser.TK_ID, 0)
        def TK_PAR_IZQ(self):
            return self.getToken(GramaticaParser.TK_PAR_IZQ, 0)
        def TK_PAR_DER(self):
            return self.getToken(GramaticaParser.TK_PAR_DER, 0)
        def args(self):
            return self.getTypedRuleContext(GramaticaParser.ArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLlamadaFuncionG4" ):
                listener.enterExprLlamadaFuncionG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLlamadaFuncionG4" ):
                listener.exitExprLlamadaFuncionG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLlamadaFuncionG4" ):
                return visitor.visitExprLlamadaFuncionG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicaAndG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)

        def TK_Y(self):
            return self.getToken(GramaticaParser.TK_Y, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogicaAndG4" ):
                listener.enterExprLogicaAndG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogicaAndG4" ):
                listener.exitExprLogicaAndG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicaAndG4" ):
                return visitor.visitExprLogicaAndG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicaNotG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_NOT(self):
            return self.getToken(GramaticaParser.TK_NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogicaNotG4" ):
                listener.enterExprLogicaNotG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogicaNotG4" ):
                listener.exitExprLogicaNotG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicaNotG4" ):
                return visitor.visitExprLogicaNotG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprAgrupacionG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_PAR_IZQ(self):
            return self.getToken(GramaticaParser.TK_PAR_IZQ, 0)
        def expr(self):
            return self.getTypedRuleContext(GramaticaParser.ExprContext,0)

        def TK_PAR_DER(self):
            return self.getToken(GramaticaParser.TK_PAR_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAgrupacionG4" ):
                listener.enterExprAgrupacionG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAgrupacionG4" ):
                listener.exitExprAgrupacionG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAgrupacionG4" ):
                return visitor.visitExprAgrupacionG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralBoolG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_TRUE(self):
            return self.getToken(GramaticaParser.TK_TRUE, 0)
        def TK_FALSE(self):
            return self.getToken(GramaticaParser.TK_FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLiteralBoolG4" ):
                listener.enterExprLiteralBoolG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLiteralBoolG4" ):
                listener.exitExprLiteralBoolG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteralBoolG4" ):
                return visitor.visitExprLiteralBoolG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralCadenaG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_CADENA(self):
            return self.getToken(GramaticaParser.TK_CADENA, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLiteralCadenaG4" ):
                listener.enterExprLiteralCadenaG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLiteralCadenaG4" ):
                listener.exitExprLiteralCadenaG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteralCadenaG4" ):
                return visitor.visitExprLiteralCadenaG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprRelacionalIgualdadG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)

        def TK_IGUAL(self):
            return self.getToken(GramaticaParser.TK_IGUAL, 0)
        def TK_DIFERENTE(self):
            return self.getToken(GramaticaParser.TK_DIFERENTE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprRelacionalIgualdadG4" ):
                listener.enterExprRelacionalIgualdadG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprRelacionalIgualdadG4" ):
                listener.exitExprRelacionalIgualdadG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelacionalIgualdadG4" ):
                return visitor.visitExprRelacionalIgualdadG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprReferenciaVariableG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(GramaticaParser.TK_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprReferenciaVariableG4" ):
                listener.enterExprReferenciaVariableG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprReferenciaVariableG4" ):
                listener.exitExprReferenciaVariableG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprReferenciaVariableG4" ):
                return visitor.visitExprReferenciaVariableG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralNumericaG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramaticaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_NUMERO(self):
            return self.getToken(GramaticaParser.TK_NUMERO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLiteralNumericaG4" ):
                listener.enterExprLiteralNumericaG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLiteralNumericaG4" ):
                listener.exitExprLiteralNumericaG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteralNumericaG4" ):
                return visitor.visitExprLiteralNumericaG4(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GramaticaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = GramaticaParser.ExprLogicaNotG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 162
                self.match(GramaticaParser.TK_NOT)
                self.state = 163
                self.expr(14)
                pass

            elif la_ == 2:
                localctx = GramaticaParser.ExprAgrupacionG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 164
                self.match(GramaticaParser.TK_PAR_IZQ)
                self.state = 165
                self.expr(0)
                self.state = 166
                self.match(GramaticaParser.TK_PAR_DER)
                pass

            elif la_ == 3:
                localctx = GramaticaParser.ExprLiteralNumericaG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(GramaticaParser.TK_NUMERO)
                pass

            elif la_ == 4:
                localctx = GramaticaParser.ExprLiteralCadenaG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 169
                self.match(GramaticaParser.TK_CADENA)
                pass

            elif la_ == 5:
                localctx = GramaticaParser.ExprLiteralBoolG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                _la = self._input.LA(1)
                if not(_la==37 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                localctx = GramaticaParser.ExprLlamadaFuncionG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 171
                self.match(GramaticaParser.TK_ID)
                self.state = 172
                self.match(GramaticaParser.TK_PAR_IZQ)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4260607836160) != 0):
                    self.state = 173
                    self.args()


                self.state = 176
                self.match(GramaticaParser.TK_PAR_DER)
                pass

            elif la_ == 7:
                localctx = GramaticaParser.ExprReferenciaVariableG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.match(GramaticaParser.TK_ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 203
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 201
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = GramaticaParser.ExprPotenciaG4Context(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 180
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 181
                        self.match(GramaticaParser.TK_POTENCIA)
                        self.state = 182
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = GramaticaParser.ExprAritmeticaMultDivG4Context(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 183
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 184
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 185
                        self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = GramaticaParser.ExprAritmeticaSumaResG4Context(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 186
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 187
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 188
                        self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = GramaticaParser.ExprRelacionalCompG4Context(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 189
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 190
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = GramaticaParser.ExprRelacionalIgualdadG4Context(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 192
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 193
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 194
                        self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = GramaticaParser.ExprLogicaAndG4Context(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 195
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 196
                        self.match(GramaticaParser.TK_Y)
                        self.state = 197
                        self.expr(9)
                        pass

                    elif la_ == 7:
                        localctx = GramaticaParser.ExprLogicaOrG4Context(self, GramaticaParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 198
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 199
                        self.match(GramaticaParser.TK_O)
                        self.state = 200
                        self.expr(8)
                        pass

             
                self.state = 205
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramaticaParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramaticaParser.ExprContext,i)


        def TK_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.TK_COMA)
            else:
                return self.getToken(GramaticaParser.TK_COMA, i)

        def getRuleIndex(self):
            return GramaticaParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = GramaticaParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.expr(0)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 207
                self.match(GramaticaParser.TK_COMA)
                self.state = 208
                self.expr(0)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         




