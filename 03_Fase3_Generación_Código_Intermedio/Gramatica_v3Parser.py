# Generated from Gramatica_v3.g4 by ANTLR 4.13.1
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
        4,1,50,259,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,1,0,1,0,1,
        0,5,0,43,8,0,10,0,12,0,46,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,55,
        8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,65,8,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,77,8,3,1,4,1,4,1,4,1,4,5,4,83,8,4,10,4,
        12,4,86,9,4,3,4,88,8,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,96,8,5,1,5,1,
        5,1,5,1,6,1,6,1,6,5,6,104,8,6,10,6,12,6,107,9,6,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,120,8,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,138,8,9,1,10,1,10,5,
        10,142,8,10,10,10,12,10,145,9,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,161,8,12,1,13,1,13,1,
        13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,176,8,
        14,1,14,3,14,179,8,14,1,14,1,14,1,14,3,14,184,8,14,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,3,16,197,8,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        3,17,214,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,223,8,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,
        17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,5,17,246,8,17,10,17,12,17,
        249,9,17,1,18,1,18,1,18,5,18,254,8,18,10,18,12,18,257,9,18,1,18,
        0,1,34,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,
        5,1,0,43,44,1,0,3,5,1,0,1,2,1,0,9,12,1,0,7,8,287,0,38,1,0,0,0,2,
        54,1,0,0,0,4,56,1,0,0,0,6,76,1,0,0,0,8,78,1,0,0,0,10,91,1,0,0,0,
        12,100,1,0,0,0,14,108,1,0,0,0,16,119,1,0,0,0,18,137,1,0,0,0,20,139,
        1,0,0,0,22,148,1,0,0,0,24,152,1,0,0,0,26,162,1,0,0,0,28,168,1,0,
        0,0,30,188,1,0,0,0,32,194,1,0,0,0,34,222,1,0,0,0,36,250,1,0,0,0,
        38,39,5,25,0,0,39,40,5,47,0,0,40,44,5,26,0,0,41,43,3,2,1,0,42,41,
        1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,
        46,44,1,0,0,0,47,48,5,27,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,55,3,
        6,3,0,51,55,3,10,5,0,52,55,3,4,2,0,53,55,3,18,9,0,54,50,1,0,0,0,
        54,51,1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,3,1,0,0,0,56,57,5,35,
        0,0,57,58,5,47,0,0,58,59,5,17,0,0,59,5,1,0,0,0,60,61,3,16,8,0,61,
        64,5,47,0,0,62,63,5,16,0,0,63,65,3,34,17,0,64,62,1,0,0,0,64,65,1,
        0,0,0,65,66,1,0,0,0,66,67,5,17,0,0,67,77,1,0,0,0,68,69,5,38,0,0,
        69,70,5,23,0,0,70,71,5,24,0,0,71,72,5,47,0,0,72,73,5,16,0,0,73,74,
        3,8,4,0,74,75,5,17,0,0,75,77,1,0,0,0,76,60,1,0,0,0,76,68,1,0,0,0,
        77,7,1,0,0,0,78,87,5,23,0,0,79,84,3,34,17,0,80,81,5,18,0,0,81,83,
        3,34,17,0,82,80,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,
        0,85,88,1,0,0,0,86,84,1,0,0,0,87,79,1,0,0,0,87,88,1,0,0,0,88,89,
        1,0,0,0,89,90,5,24,0,0,90,9,1,0,0,0,91,92,3,16,8,0,92,93,5,47,0,
        0,93,95,5,19,0,0,94,96,3,12,6,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,
        1,0,0,0,97,98,5,20,0,0,98,99,3,20,10,0,99,11,1,0,0,0,100,105,3,14,
        7,0,101,102,5,18,0,0,102,104,3,14,7,0,103,101,1,0,0,0,104,107,1,
        0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,13,1,0,0,0,107,105,1,0,
        0,0,108,109,3,16,8,0,109,110,5,47,0,0,110,15,1,0,0,0,111,120,5,38,
        0,0,112,120,5,39,0,0,113,120,5,40,0,0,114,120,5,41,0,0,115,120,5,
        42,0,0,116,117,5,38,0,0,117,118,5,23,0,0,118,120,5,24,0,0,119,111,
        1,0,0,0,119,112,1,0,0,0,119,113,1,0,0,0,119,114,1,0,0,0,119,115,
        1,0,0,0,119,116,1,0,0,0,120,17,1,0,0,0,121,122,3,22,11,0,122,123,
        5,17,0,0,123,138,1,0,0,0,124,138,3,24,12,0,125,138,3,26,13,0,126,
        138,3,28,14,0,127,138,3,30,15,0,128,138,3,32,16,0,129,130,5,36,0,
        0,130,138,5,17,0,0,131,132,5,37,0,0,132,138,5,17,0,0,133,138,3,20,
        10,0,134,135,3,34,17,0,135,136,5,17,0,0,136,138,1,0,0,0,137,121,
        1,0,0,0,137,124,1,0,0,0,137,125,1,0,0,0,137,126,1,0,0,0,137,127,
        1,0,0,0,137,128,1,0,0,0,137,129,1,0,0,0,137,131,1,0,0,0,137,133,
        1,0,0,0,137,134,1,0,0,0,138,19,1,0,0,0,139,143,5,21,0,0,140,142,
        3,18,9,0,141,140,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,
        1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,5,22,0,0,147,21,
        1,0,0,0,148,149,5,47,0,0,149,150,5,16,0,0,150,151,3,34,17,0,151,
        23,1,0,0,0,152,153,5,28,0,0,153,154,5,19,0,0,154,155,3,34,17,0,155,
        156,5,20,0,0,156,157,5,29,0,0,157,160,3,20,10,0,158,159,5,30,0,0,
        159,161,3,20,10,0,160,158,1,0,0,0,160,161,1,0,0,0,161,25,1,0,0,0,
        162,163,5,31,0,0,163,164,5,19,0,0,164,165,3,34,17,0,165,166,5,20,
        0,0,166,167,3,20,10,0,167,27,1,0,0,0,168,169,5,32,0,0,169,175,5,
        19,0,0,170,176,3,6,3,0,171,172,3,22,11,0,172,173,5,17,0,0,173,176,
        1,0,0,0,174,176,5,17,0,0,175,170,1,0,0,0,175,171,1,0,0,0,175,174,
        1,0,0,0,176,178,1,0,0,0,177,179,3,34,17,0,178,177,1,0,0,0,178,179,
        1,0,0,0,179,180,1,0,0,0,180,183,5,17,0,0,181,184,3,22,11,0,182,184,
        3,34,17,0,183,181,1,0,0,0,183,182,1,0,0,0,183,184,1,0,0,0,184,185,
        1,0,0,0,185,186,5,20,0,0,186,187,3,20,10,0,187,29,1,0,0,0,188,189,
        5,33,0,0,189,190,5,19,0,0,190,191,3,34,17,0,191,192,5,20,0,0,192,
        193,5,17,0,0,193,31,1,0,0,0,194,196,5,34,0,0,195,197,3,34,17,0,196,
        195,1,0,0,0,196,197,1,0,0,0,197,198,1,0,0,0,198,199,5,17,0,0,199,
        33,1,0,0,0,200,201,6,17,-1,0,201,202,5,15,0,0,202,223,3,34,17,15,
        203,204,5,19,0,0,204,205,3,34,17,0,205,206,5,20,0,0,206,223,1,0,
        0,0,207,223,5,45,0,0,208,223,5,46,0,0,209,223,7,0,0,0,210,211,5,
        47,0,0,211,213,5,19,0,0,212,214,3,36,18,0,213,212,1,0,0,0,213,214,
        1,0,0,0,214,215,1,0,0,0,215,223,5,20,0,0,216,217,5,47,0,0,217,218,
        5,23,0,0,218,219,3,34,17,0,219,220,5,24,0,0,220,223,1,0,0,0,221,
        223,5,47,0,0,222,200,1,0,0,0,222,203,1,0,0,0,222,207,1,0,0,0,222,
        208,1,0,0,0,222,209,1,0,0,0,222,210,1,0,0,0,222,216,1,0,0,0,222,
        221,1,0,0,0,223,247,1,0,0,0,224,225,10,14,0,0,225,226,5,6,0,0,226,
        246,3,34,17,14,227,228,10,13,0,0,228,229,7,1,0,0,229,246,3,34,17,
        14,230,231,10,12,0,0,231,232,7,2,0,0,232,246,3,34,17,13,233,234,
        10,11,0,0,234,235,7,3,0,0,235,246,3,34,17,12,236,237,10,10,0,0,237,
        238,7,4,0,0,238,246,3,34,17,11,239,240,10,9,0,0,240,241,5,13,0,0,
        241,246,3,34,17,10,242,243,10,8,0,0,243,244,5,14,0,0,244,246,3,34,
        17,9,245,224,1,0,0,0,245,227,1,0,0,0,245,230,1,0,0,0,245,233,1,0,
        0,0,245,236,1,0,0,0,245,239,1,0,0,0,245,242,1,0,0,0,246,249,1,0,
        0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,35,1,0,0,0,249,247,1,0,0,
        0,250,255,3,34,17,0,251,252,5,18,0,0,252,254,3,34,17,0,253,251,1,
        0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,37,1,0,
        0,0,257,255,1,0,0,0,21,44,54,64,76,84,87,95,105,119,137,143,160,
        175,178,183,196,213,222,245,247,255
    ]

class Gramatica_v3Parser ( Parser ):

    grammarFileName = "Gramatica_v3.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
                     "'=='", "<INVALID>", "'>'", "'<'", "'>='", "'<='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "';'", 
                     "','", "'('", "')'", "'{'", "'}'", "'['", "']'", "'PROGRAMA'", 
                     "'INICIO'", "'FIN'", "'SI'", "'ENTONCES'", "'SINO'", 
                     "'MIENTRAS'", "'FOR'", "'IMPRIMIR'", "'RETORNAR'", 
                     "'IMPORT'", "'BREAK'", "'CONTINUE'", "'INT'", "'FLOAT'", 
                     "'STRING'", "'BOOL'", "'VOID'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "TK_SUMA", "TK_RESTA", "TK_MULT", "TK_DIV", 
                      "TK_MODULO", "TK_POTENCIA", "TK_IGUAL", "TK_DIFERENTE", 
                      "TK_MAYOR", "TK_MENOR", "TK_MAYOREQ", "TK_MENOREQ", 
                      "TK_Y", "TK_O", "TK_NOT", "ASSIGN", "SEMICOLON", "TK_COMA", 
                      "TK_PAR_IZQ", "TK_PAR_DER", "TK_LLA_IZQ", "TK_LLA_DER", 
                      "TK_COR_IZQ", "TK_COR_DER", "TK_PROGRAMA", "TK_INICIO", 
                      "TK_FIN", "TK_SI", "TK_ENTONCES", "TK_SINO", "TK_MIENTRAS", 
                      "TK_FOR", "TK_IMPRIMIR", "TK_RETURN", "TK_IMPORT", 
                      "TK_BREAK", "TK_CONTINUE", "TK_INT", "TK_FLOAT", "TK_STRING", 
                      "TK_BOOL", "TK_VOID", "TK_TRUE", "TK_FALSE", "TK_NUMERO", 
                      "TK_CADENA", "TK_ID", "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_importacion = 2
    RULE_varDeclaration = 3
    RULE_arrayLiteral = 4
    RULE_funcDeclaration = 5
    RULE_params = 6
    RULE_param = 7
    RULE_type = 8
    RULE_instruccion = 9
    RULE_bloque = 10
    RULE_asignacion_core = 11
    RULE_condicional = 12
    RULE_bucle_mientras = 13
    RULE_bucle_for = 14
    RULE_impresion = 15
    RULE_sentencia_return = 16
    RULE_expr = 17
    RULE_args = 18

    ruleNames =  [ "program", "declaration", "importacion", "varDeclaration", 
                   "arrayLiteral", "funcDeclaration", "params", "param", 
                   "type", "instruccion", "bloque", "asignacion_core", "condicional", 
                   "bucle_mientras", "bucle_for", "impresion", "sentencia_return", 
                   "expr", "args" ]

    EOF = Token.EOF
    TK_SUMA=1
    TK_RESTA=2
    TK_MULT=3
    TK_DIV=4
    TK_MODULO=5
    TK_POTENCIA=6
    TK_IGUAL=7
    TK_DIFERENTE=8
    TK_MAYOR=9
    TK_MENOR=10
    TK_MAYOREQ=11
    TK_MENOREQ=12
    TK_Y=13
    TK_O=14
    TK_NOT=15
    ASSIGN=16
    SEMICOLON=17
    TK_COMA=18
    TK_PAR_IZQ=19
    TK_PAR_DER=20
    TK_LLA_IZQ=21
    TK_LLA_DER=22
    TK_COR_IZQ=23
    TK_COR_DER=24
    TK_PROGRAMA=25
    TK_INICIO=26
    TK_FIN=27
    TK_SI=28
    TK_ENTONCES=29
    TK_SINO=30
    TK_MIENTRAS=31
    TK_FOR=32
    TK_IMPRIMIR=33
    TK_RETURN=34
    TK_IMPORT=35
    TK_BREAK=36
    TK_CONTINUE=37
    TK_INT=38
    TK_FLOAT=39
    TK_STRING=40
    TK_BOOL=41
    TK_VOID=42
    TK_TRUE=43
    TK_FALSE=44
    TK_NUMERO=45
    TK_CADENA=46
    TK_ID=47
    WS=48
    COMMENT=49
    BLOCK_COMMENT=50

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
            return Gramatica_v3Parser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramG4Context(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_PROGRAMA(self):
            return self.getToken(Gramatica_v3Parser.TK_PROGRAMA, 0)
        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)
        def TK_INICIO(self):
            return self.getToken(Gramatica_v3Parser.TK_INICIO, 0)
        def TK_FIN(self):
            return self.getToken(Gramatica_v3Parser.TK_FIN, 0)
        def EOF(self):
            return self.getToken(Gramatica_v3Parser.EOF, 0)
        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.DeclarationContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramG4" ):
                return visitor.visitProgramG4(self)
            else:
                return visitor.visitChildren(self)



    def program(self):

        localctx = Gramatica_v3Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = Gramatica_v3Parser.ProgramG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(Gramatica_v3Parser.TK_PROGRAMA)
            self.state = 39
            self.match(Gramatica_v3Parser.TK_ID)
            self.state = 40
            self.match(Gramatica_v3Parser.TK_INICIO)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 281473100316672) != 0):
                self.state = 41
                self.declaration()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 47
            self.match(Gramatica_v3Parser.TK_FIN)
            self.state = 48
            self.match(Gramatica_v3Parser.EOF)
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
            return Gramatica_v3Parser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclImportG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def importacion(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ImportacionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclImportG4" ):
                return visitor.visitDeclImportG4(self)
            else:
                return visitor.visitChildren(self)


    class DeclInstruccionG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instruccion(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.InstruccionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclInstruccionG4" ):
                return visitor.visitDeclInstruccionG4(self)
            else:
                return visitor.visitChildren(self)


    class DeclVariableG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDeclaration(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.VarDeclarationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclVariableG4" ):
                return visitor.visitDeclVariableG4(self)
            else:
                return visitor.visitChildren(self)


    class DeclFuncionG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcDeclaration(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.FuncDeclarationContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclFuncionG4" ):
                return visitor.visitDeclFuncionG4(self)
            else:
                return visitor.visitChildren(self)



    def declaration(self):

        localctx = Gramatica_v3Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = Gramatica_v3Parser.DeclVariableG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.varDeclaration()
                pass

            elif la_ == 2:
                localctx = Gramatica_v3Parser.DeclFuncionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.funcDeclaration()
                pass

            elif la_ == 3:
                localctx = Gramatica_v3Parser.DeclImportG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.importacion()
                pass

            elif la_ == 4:
                localctx = Gramatica_v3Parser.DeclInstruccionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_IMPORT(self):
            return self.getToken(Gramatica_v3Parser.TK_IMPORT, 0)

        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)

        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_importacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportacion" ):
                return visitor.visitImportacion(self)
            else:
                return visitor.visitChildren(self)




    def importacion(self):

        localctx = Gramatica_v3Parser.ImportacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(Gramatica_v3Parser.TK_IMPORT)
            self.state = 57
            self.match(Gramatica_v3Parser.TK_ID)
            self.state = 58
            self.match(Gramatica_v3Parser.SEMICOLON)
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
            return Gramatica_v3Parser.RULE_varDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarDeclarationG4Context(VarDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.VarDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.TypeContext,0)

        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)
        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)
        def ASSIGN(self):
            return self.getToken(Gramatica_v3Parser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclarationG4" ):
                return visitor.visitVarDeclarationG4(self)
            else:
                return visitor.visitChildren(self)


    class VarArrayDeclarationG4Context(VarDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.VarDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_INT(self):
            return self.getToken(Gramatica_v3Parser.TK_INT, 0)
        def TK_COR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_COR_IZQ, 0)
        def TK_COR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_COR_DER, 0)
        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)
        def ASSIGN(self):
            return self.getToken(Gramatica_v3Parser.ASSIGN, 0)
        def arrayLiteral(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ArrayLiteralContext,0)

        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarArrayDeclarationG4" ):
                return visitor.visitVarArrayDeclarationG4(self)
            else:
                return visitor.visitChildren(self)



    def varDeclaration(self):

        localctx = Gramatica_v3Parser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = Gramatica_v3Parser.VarDeclarationG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.type_()
                self.state = 61
                self.match(Gramatica_v3Parser.TK_ID)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 62
                    self.match(Gramatica_v3Parser.ASSIGN)
                    self.state = 63
                    self.expr(0)


                self.state = 66
                self.match(Gramatica_v3Parser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = Gramatica_v3Parser.VarArrayDeclarationG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(Gramatica_v3Parser.TK_INT)
                self.state = 69
                self.match(Gramatica_v3Parser.TK_COR_IZQ)
                self.state = 70
                self.match(Gramatica_v3Parser.TK_COR_DER)
                self.state = 71
                self.match(Gramatica_v3Parser.TK_ID)
                self.state = 72
                self.match(Gramatica_v3Parser.ASSIGN)
                self.state = 73
                self.arrayLiteral()
                self.state = 74
                self.match(Gramatica_v3Parser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_COR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_COR_IZQ, 0)

        def TK_COR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_COR_DER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)


        def TK_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(Gramatica_v3Parser.TK_COMA)
            else:
                return self.getToken(Gramatica_v3Parser.TK_COMA, i)

        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_arrayLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = Gramatica_v3Parser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(Gramatica_v3Parser.TK_COR_IZQ)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 272678884245504) != 0):
                self.state = 79
                self.expr(0)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 80
                    self.match(Gramatica_v3Parser.TK_COMA)
                    self.state = 81
                    self.expr(0)
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 89
            self.match(Gramatica_v3Parser.TK_COR_DER)
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
            return Gramatica_v3Parser.RULE_funcDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncDeclarationG4Context(FuncDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.FuncDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.TypeContext,0)

        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)
        def TK_PAR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_IZQ, 0)
        def TK_PAR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_DER, 0)
        def bloque(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.BloqueContext,0)

        def params(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ParamsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDeclarationG4" ):
                return visitor.visitFuncDeclarationG4(self)
            else:
                return visitor.visitChildren(self)



    def funcDeclaration(self):

        localctx = Gramatica_v3Parser.FuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcDeclaration)
        self._la = 0 # Token type
        try:
            localctx = Gramatica_v3Parser.FuncDeclarationG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.type_()
            self.state = 92
            self.match(Gramatica_v3Parser.TK_ID)
            self.state = 93
            self.match(Gramatica_v3Parser.TK_PAR_IZQ)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521215115264) != 0):
                self.state = 94
                self.params()


            self.state = 97
            self.match(Gramatica_v3Parser.TK_PAR_DER)
            self.state = 98
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
                return self.getTypedRuleContexts(Gramatica_v3Parser.ParamContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ParamContext,i)


        def TK_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(Gramatica_v3Parser.TK_COMA)
            else:
                return self.getToken(Gramatica_v3Parser.TK_COMA, i)

        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = Gramatica_v3Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.param()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 101
                self.match(Gramatica_v3Parser.TK_COMA)
                self.state = 102
                self.param()
                self.state = 107
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
            return self.getTypedRuleContext(Gramatica_v3Parser.TypeContext,0)


        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)

        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = Gramatica_v3Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.type_()
            self.state = 109
            self.match(Gramatica_v3Parser.TK_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeVoidG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_VOID(self):
            return self.getToken(Gramatica_v3Parser.TK_VOID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVoidG4" ):
                return visitor.visitTypeVoidG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeStringG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_STRING(self):
            return self.getToken(Gramatica_v3Parser.TK_STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeStringG4" ):
                return visitor.visitTypeStringG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeBoolG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_BOOL(self):
            return self.getToken(Gramatica_v3Parser.TK_BOOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBoolG4" ):
                return visitor.visitTypeBoolG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeIntArrayG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_INT(self):
            return self.getToken(Gramatica_v3Parser.TK_INT, 0)
        def TK_COR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_COR_IZQ, 0)
        def TK_COR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_COR_DER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeIntArrayG4" ):
                return visitor.visitTypeIntArrayG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeIntG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_INT(self):
            return self.getToken(Gramatica_v3Parser.TK_INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeIntG4" ):
                return visitor.visitTypeIntG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeFloatG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_FLOAT(self):
            return self.getToken(Gramatica_v3Parser.TK_FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeFloatG4" ):
                return visitor.visitTypeFloatG4(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = Gramatica_v3Parser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = Gramatica_v3Parser.TypeIntG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(Gramatica_v3Parser.TK_INT)
                pass

            elif la_ == 2:
                localctx = Gramatica_v3Parser.TypeFloatG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(Gramatica_v3Parser.TK_FLOAT)
                pass

            elif la_ == 3:
                localctx = Gramatica_v3Parser.TypeStringG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(Gramatica_v3Parser.TK_STRING)
                pass

            elif la_ == 4:
                localctx = Gramatica_v3Parser.TypeBoolG4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.match(Gramatica_v3Parser.TK_BOOL)
                pass

            elif la_ == 5:
                localctx = Gramatica_v3Parser.TypeVoidG4Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.match(Gramatica_v3Parser.TK_VOID)
                pass

            elif la_ == 6:
                localctx = Gramatica_v3Parser.TypeIntArrayG4Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self.match(Gramatica_v3Parser.TK_INT)
                self.state = 117
                self.match(Gramatica_v3Parser.TK_COR_IZQ)
                self.state = 118
                self.match(Gramatica_v3Parser.TK_COR_DER)
                pass


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
            return Gramatica_v3Parser.RULE_instruccion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SentenciaForG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bucle_for(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.Bucle_forContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaForG4" ):
                return visitor.visitSentenciaForG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaImprimirG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def impresion(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ImpresionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaImprimirG4" ):
                return visitor.visitSentenciaImprimirG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaContinueG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_CONTINUE(self):
            return self.getToken(Gramatica_v3Parser.TK_CONTINUE, 0)
        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaContinueG4" ):
                return visitor.visitSentenciaContinueG4(self)
            else:
                return visitor.visitChildren(self)


    class StatBloqueG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bloque(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.BloqueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatBloqueG4" ):
                return visitor.visitStatBloqueG4(self)
            else:
                return visitor.visitChildren(self)


    class AsignacionVariableG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asignacion_core(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.Asignacion_coreContext,0)

        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionVariableG4" ):
                return visitor.visitAsignacionVariableG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaExpresionG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)

        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaExpresionG4" ):
                return visitor.visitSentenciaExpresionG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaIfElseG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicional(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.CondicionalContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaIfElseG4" ):
                return visitor.visitSentenciaIfElseG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaMientrasG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bucle_mientras(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.Bucle_mientrasContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaMientrasG4" ):
                return visitor.visitSentenciaMientrasG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaReturnG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sentencia_return(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.Sentencia_returnContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaReturnG4" ):
                return visitor.visitSentenciaReturnG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaBreakG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_BREAK(self):
            return self.getToken(Gramatica_v3Parser.TK_BREAK, 0)
        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaBreakG4" ):
                return visitor.visitSentenciaBreakG4(self)
            else:
                return visitor.visitChildren(self)



    def instruccion(self):

        localctx = Gramatica_v3Parser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_instruccion)
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = Gramatica_v3Parser.AsignacionVariableG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.asignacion_core()
                self.state = 122
                self.match(Gramatica_v3Parser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = Gramatica_v3Parser.SentenciaIfElseG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.condicional()
                pass

            elif la_ == 3:
                localctx = Gramatica_v3Parser.SentenciaMientrasG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.bucle_mientras()
                pass

            elif la_ == 4:
                localctx = Gramatica_v3Parser.SentenciaForG4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.bucle_for()
                pass

            elif la_ == 5:
                localctx = Gramatica_v3Parser.SentenciaImprimirG4Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.impresion()
                pass

            elif la_ == 6:
                localctx = Gramatica_v3Parser.SentenciaReturnG4Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.sentencia_return()
                pass

            elif la_ == 7:
                localctx = Gramatica_v3Parser.SentenciaBreakG4Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 129
                self.match(Gramatica_v3Parser.TK_BREAK)
                self.state = 130
                self.match(Gramatica_v3Parser.SEMICOLON)
                pass

            elif la_ == 8:
                localctx = Gramatica_v3Parser.SentenciaContinueG4Context(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.match(Gramatica_v3Parser.TK_CONTINUE)
                self.state = 132
                self.match(Gramatica_v3Parser.SEMICOLON)
                pass

            elif la_ == 9:
                localctx = Gramatica_v3Parser.StatBloqueG4Context(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 133
                self.bloque()
                pass

            elif la_ == 10:
                localctx = Gramatica_v3Parser.SentenciaExpresionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 134
                self.expr(0)
                self.state = 135
                self.match(Gramatica_v3Parser.SEMICOLON)
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
            return self.getToken(Gramatica_v3Parser.TK_LLA_IZQ, 0)

        def TK_LLA_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_LLA_DER, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = Gramatica_v3Parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(Gramatica_v3Parser.TK_LLA_IZQ)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 272917525463040) != 0):
                self.state = 140
                self.instruccion()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(Gramatica_v3Parser.TK_LLA_DER)
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
            return Gramatica_v3Parser.RULE_asignacion_core

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionCoreG4Context(Asignacion_coreContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.Asignacion_coreContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)
        def ASSIGN(self):
            return self.getToken(Gramatica_v3Parser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacionCoreG4" ):
                return visitor.visitAsignacionCoreG4(self)
            else:
                return visitor.visitChildren(self)



    def asignacion_core(self):

        localctx = Gramatica_v3Parser.Asignacion_coreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_asignacion_core)
        try:
            localctx = Gramatica_v3Parser.AsignacionCoreG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(Gramatica_v3Parser.TK_ID)
            self.state = 149
            self.match(Gramatica_v3Parser.ASSIGN)
            self.state = 150
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
            return self.getToken(Gramatica_v3Parser.TK_SI, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_DER, 0)

        def TK_ENTONCES(self):
            return self.getToken(Gramatica_v3Parser.TK_ENTONCES, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.BloqueContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.BloqueContext,i)


        def TK_SINO(self):
            return self.getToken(Gramatica_v3Parser.TK_SINO, 0)

        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_condicional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = Gramatica_v3Parser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(Gramatica_v3Parser.TK_SI)
            self.state = 153
            self.match(Gramatica_v3Parser.TK_PAR_IZQ)
            self.state = 154
            self.expr(0)
            self.state = 155
            self.match(Gramatica_v3Parser.TK_PAR_DER)
            self.state = 156
            self.match(Gramatica_v3Parser.TK_ENTONCES)
            self.state = 157
            self.bloque()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 158
                self.match(Gramatica_v3Parser.TK_SINO)
                self.state = 159
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
            return self.getToken(Gramatica_v3Parser.TK_MIENTRAS, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.BloqueContext,0)


        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_bucle_mientras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBucle_mientras" ):
                return visitor.visitBucle_mientras(self)
            else:
                return visitor.visitChildren(self)




    def bucle_mientras(self):

        localctx = Gramatica_v3Parser.Bucle_mientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_bucle_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(Gramatica_v3Parser.TK_MIENTRAS)
            self.state = 163
            self.match(Gramatica_v3Parser.TK_PAR_IZQ)
            self.state = 164
            self.expr(0)
            self.state = 165
            self.match(Gramatica_v3Parser.TK_PAR_DER)
            self.state = 166
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
            return self.getToken(Gramatica_v3Parser.TK_FOR, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_IZQ, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(Gramatica_v3Parser.SEMICOLON)
            else:
                return self.getToken(Gramatica_v3Parser.SEMICOLON, i)

        def TK_PAR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.BloqueContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.VarDeclarationContext,0)


        def asignacion_core(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.Asignacion_coreContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.Asignacion_coreContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)


        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_bucle_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBucle_for" ):
                return visitor.visitBucle_for(self)
            else:
                return visitor.visitChildren(self)




    def bucle_for(self):

        localctx = Gramatica_v3Parser.Bucle_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_bucle_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(Gramatica_v3Parser.TK_FOR)
            self.state = 169
            self.match(Gramatica_v3Parser.TK_PAR_IZQ)
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38, 39, 40, 41, 42]:
                self.state = 170
                localctx.init_var = self.varDeclaration()
                pass
            elif token in [47]:
                self.state = 171
                localctx.init_assign = self.asignacion_core()
                self.state = 172
                self.match(Gramatica_v3Parser.SEMICOLON)
                pass
            elif token in [17]:
                self.state = 174
                self.match(Gramatica_v3Parser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 272678884245504) != 0):
                self.state = 177
                localctx.cond = self.expr(0)


            self.state = 180
            self.match(Gramatica_v3Parser.SEMICOLON)
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 181
                localctx.update_assign = self.asignacion_core()

            elif la_ == 2:
                self.state = 182
                localctx.update_expr = self.expr(0)


            self.state = 185
            self.match(Gramatica_v3Parser.TK_PAR_DER)
            self.state = 186
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
            return self.getToken(Gramatica_v3Parser.TK_IMPRIMIR, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_DER, 0)

        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_impresion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpresion" ):
                return visitor.visitImpresion(self)
            else:
                return visitor.visitChildren(self)




    def impresion(self):

        localctx = Gramatica_v3Parser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(Gramatica_v3Parser.TK_IMPRIMIR)
            self.state = 189
            self.match(Gramatica_v3Parser.TK_PAR_IZQ)
            self.state = 190
            self.expr(0)
            self.state = 191
            self.match(Gramatica_v3Parser.TK_PAR_DER)
            self.state = 192
            self.match(Gramatica_v3Parser.SEMICOLON)
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
            return self.getToken(Gramatica_v3Parser.TK_RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(Gramatica_v3Parser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)


        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_sentencia_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia_return" ):
                return visitor.visitSentencia_return(self)
            else:
                return visitor.visitChildren(self)




    def sentencia_return(self):

        localctx = Gramatica_v3Parser.Sentencia_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_sentencia_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(Gramatica_v3Parser.TK_RETURN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 272678884245504) != 0):
                self.state = 195
                self.expr(0)


            self.state = 198
            self.match(Gramatica_v3Parser.SEMICOLON)
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
            return Gramatica_v3Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprRelacionalCompG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)

        def TK_MAYOR(self):
            return self.getToken(Gramatica_v3Parser.TK_MAYOR, 0)
        def TK_MENOR(self):
            return self.getToken(Gramatica_v3Parser.TK_MENOR, 0)
        def TK_MAYOREQ(self):
            return self.getToken(Gramatica_v3Parser.TK_MAYOREQ, 0)
        def TK_MENOREQ(self):
            return self.getToken(Gramatica_v3Parser.TK_MENOREQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelacionalCompG4" ):
                return visitor.visitExprRelacionalCompG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprPotenciaG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)

        def TK_POTENCIA(self):
            return self.getToken(Gramatica_v3Parser.TK_POTENCIA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPotenciaG4" ):
                return visitor.visitExprPotenciaG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicaOrG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)

        def TK_O(self):
            return self.getToken(Gramatica_v3Parser.TK_O, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicaOrG4" ):
                return visitor.visitExprLogicaOrG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprAritmeticaSumaResG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)

        def TK_SUMA(self):
            return self.getToken(Gramatica_v3Parser.TK_SUMA, 0)
        def TK_RESTA(self):
            return self.getToken(Gramatica_v3Parser.TK_RESTA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritmeticaSumaResG4" ):
                return visitor.visitExprAritmeticaSumaResG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLlamadaFuncionG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)
        def TK_PAR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_IZQ, 0)
        def TK_PAR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_DER, 0)
        def args(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ArgsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLlamadaFuncionG4" ):
                return visitor.visitExprLlamadaFuncionG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprArrayAccessG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)
        def TK_COR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_COR_IZQ, 0)
        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)

        def TK_COR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_COR_DER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArrayAccessG4" ):
                return visitor.visitExprArrayAccessG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicaAndG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)

        def TK_Y(self):
            return self.getToken(Gramatica_v3Parser.TK_Y, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicaAndG4" ):
                return visitor.visitExprLogicaAndG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprAritmeticaMultDivModG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)

        def TK_MULT(self):
            return self.getToken(Gramatica_v3Parser.TK_MULT, 0)
        def TK_DIV(self):
            return self.getToken(Gramatica_v3Parser.TK_DIV, 0)
        def TK_MODULO(self):
            return self.getToken(Gramatica_v3Parser.TK_MODULO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritmeticaMultDivModG4" ):
                return visitor.visitExprAritmeticaMultDivModG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicaNotG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_NOT(self):
            return self.getToken(Gramatica_v3Parser.TK_NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicaNotG4" ):
                return visitor.visitExprLogicaNotG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprAgrupacionG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_PAR_IZQ(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_IZQ, 0)
        def expr(self):
            return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,0)

        def TK_PAR_DER(self):
            return self.getToken(Gramatica_v3Parser.TK_PAR_DER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAgrupacionG4" ):
                return visitor.visitExprAgrupacionG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralBoolG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_TRUE(self):
            return self.getToken(Gramatica_v3Parser.TK_TRUE, 0)
        def TK_FALSE(self):
            return self.getToken(Gramatica_v3Parser.TK_FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteralBoolG4" ):
                return visitor.visitExprLiteralBoolG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralCadenaG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_CADENA(self):
            return self.getToken(Gramatica_v3Parser.TK_CADENA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteralCadenaG4" ):
                return visitor.visitExprLiteralCadenaG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprRelacionalIgualdadG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)

        def TK_IGUAL(self):
            return self.getToken(Gramatica_v3Parser.TK_IGUAL, 0)
        def TK_DIFERENTE(self):
            return self.getToken(Gramatica_v3Parser.TK_DIFERENTE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprRelacionalIgualdadG4" ):
                return visitor.visitExprRelacionalIgualdadG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprReferenciaVariableG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(Gramatica_v3Parser.TK_ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprReferenciaVariableG4" ):
                return visitor.visitExprReferenciaVariableG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralNumericaG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a Gramatica_v3Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_NUMERO(self):
            return self.getToken(Gramatica_v3Parser.TK_NUMERO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteralNumericaG4" ):
                return visitor.visitExprLiteralNumericaG4(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Gramatica_v3Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = Gramatica_v3Parser.ExprLogicaNotG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 201
                self.match(Gramatica_v3Parser.TK_NOT)
                self.state = 202
                self.expr(15)
                pass

            elif la_ == 2:
                localctx = Gramatica_v3Parser.ExprAgrupacionG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 203
                self.match(Gramatica_v3Parser.TK_PAR_IZQ)
                self.state = 204
                self.expr(0)
                self.state = 205
                self.match(Gramatica_v3Parser.TK_PAR_DER)
                pass

            elif la_ == 3:
                localctx = Gramatica_v3Parser.ExprLiteralNumericaG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 207
                self.match(Gramatica_v3Parser.TK_NUMERO)
                pass

            elif la_ == 4:
                localctx = Gramatica_v3Parser.ExprLiteralCadenaG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 208
                self.match(Gramatica_v3Parser.TK_CADENA)
                pass

            elif la_ == 5:
                localctx = Gramatica_v3Parser.ExprLiteralBoolG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==43 or _la==44):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                localctx = Gramatica_v3Parser.ExprLlamadaFuncionG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 210
                self.match(Gramatica_v3Parser.TK_ID)
                self.state = 211
                self.match(Gramatica_v3Parser.TK_PAR_IZQ)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 272678884245504) != 0):
                    self.state = 212
                    self.args()


                self.state = 215
                self.match(Gramatica_v3Parser.TK_PAR_DER)
                pass

            elif la_ == 7:
                localctx = Gramatica_v3Parser.ExprArrayAccessG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 216
                self.match(Gramatica_v3Parser.TK_ID)
                self.state = 217
                self.match(Gramatica_v3Parser.TK_COR_IZQ)
                self.state = 218
                self.expr(0)
                self.state = 219
                self.match(Gramatica_v3Parser.TK_COR_DER)
                pass

            elif la_ == 8:
                localctx = Gramatica_v3Parser.ExprReferenciaVariableG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 221
                self.match(Gramatica_v3Parser.TK_ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 245
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                    if la_ == 1:
                        localctx = Gramatica_v3Parser.ExprPotenciaG4Context(self, Gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 224
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 225
                        self.match(Gramatica_v3Parser.TK_POTENCIA)
                        self.state = 226
                        self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = Gramatica_v3Parser.ExprAritmeticaMultDivModG4Context(self, Gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 227
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 228
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 229
                        self.expr(14)
                        pass

                    elif la_ == 3:
                        localctx = Gramatica_v3Parser.ExprAritmeticaSumaResG4Context(self, Gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 230
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 231
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 232
                        self.expr(13)
                        pass

                    elif la_ == 4:
                        localctx = Gramatica_v3Parser.ExprRelacionalCompG4Context(self, Gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 233
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 234
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 235
                        self.expr(12)
                        pass

                    elif la_ == 5:
                        localctx = Gramatica_v3Parser.ExprRelacionalIgualdadG4Context(self, Gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 236
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 237
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 238
                        self.expr(11)
                        pass

                    elif la_ == 6:
                        localctx = Gramatica_v3Parser.ExprLogicaAndG4Context(self, Gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 239
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 240
                        self.match(Gramatica_v3Parser.TK_Y)
                        self.state = 241
                        self.expr(10)
                        pass

                    elif la_ == 7:
                        localctx = Gramatica_v3Parser.ExprLogicaOrG4Context(self, Gramatica_v3Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 242
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 243
                        self.match(Gramatica_v3Parser.TK_O)
                        self.state = 244
                        self.expr(9)
                        pass

             
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
                return self.getTypedRuleContexts(Gramatica_v3Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Gramatica_v3Parser.ExprContext,i)


        def TK_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(Gramatica_v3Parser.TK_COMA)
            else:
                return self.getToken(Gramatica_v3Parser.TK_COMA, i)

        def getRuleIndex(self):
            return Gramatica_v3Parser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = Gramatica_v3Parser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.expr(0)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 251
                self.match(Gramatica_v3Parser.TK_COMA)
                self.state = 252
                self.expr(0)
                self.state = 257
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
        self._predicates[17] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




