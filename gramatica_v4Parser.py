# Generated from gramatica_v4.g4 by ANTLR 4.13.1
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
        4,1,57,344,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,0,5,0,
        55,8,0,10,0,12,0,58,9,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,68,8,
        1,1,2,1,2,1,2,1,2,5,2,74,8,2,10,2,12,2,77,9,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,93,8,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,105,8,5,1,6,1,6,1,6,1,6,5,6,111,8,6,
        10,6,12,6,114,9,6,3,6,116,8,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,124,8,
        7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,132,8,8,10,8,12,8,135,9,8,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,149,8,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,3,11,168,8,11,1,12,1,12,1,12,1,12,1,12,1,12,5,
        12,176,8,12,10,12,12,12,179,9,12,1,12,3,12,182,8,12,1,12,1,12,1,
        13,1,13,1,13,1,13,5,13,190,8,13,10,13,12,13,193,9,13,1,14,1,14,1,
        14,5,14,198,8,14,10,14,12,14,201,9,14,1,15,1,15,5,15,205,8,15,10,
        15,12,15,208,9,15,1,15,1,15,1,16,1,16,1,16,5,16,215,8,16,10,16,12,
        16,218,9,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,
        18,1,18,3,18,232,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,3,20,247,8,20,1,20,3,20,250,8,20,1,20,1,20,
        1,20,3,20,255,8,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,
        1,22,1,22,3,22,268,8,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,
        290,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,299,8,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,5,23,331,8,23,10,23,12,23,334,9,23,1,24,1,24,1,24,5,
        24,339,8,24,10,24,12,24,342,9,24,1,24,0,1,46,25,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,5,1,0,50,
        51,1,0,3,5,1,0,1,2,1,0,9,12,1,0,7,8,378,0,50,1,0,0,0,2,67,1,0,0,
        0,4,69,1,0,0,0,6,80,1,0,0,0,8,84,1,0,0,0,10,104,1,0,0,0,12,106,1,
        0,0,0,14,119,1,0,0,0,16,128,1,0,0,0,18,136,1,0,0,0,20,148,1,0,0,
        0,22,167,1,0,0,0,24,169,1,0,0,0,26,185,1,0,0,0,28,194,1,0,0,0,30,
        202,1,0,0,0,32,211,1,0,0,0,34,219,1,0,0,0,36,223,1,0,0,0,38,233,
        1,0,0,0,40,239,1,0,0,0,42,259,1,0,0,0,44,265,1,0,0,0,46,298,1,0,
        0,0,48,335,1,0,0,0,50,51,5,28,0,0,51,52,5,54,0,0,52,56,5,29,0,0,
        53,55,3,2,1,0,54,53,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,
        0,0,0,57,59,1,0,0,0,58,56,1,0,0,0,59,60,5,30,0,0,60,61,5,0,0,1,61,
        1,1,0,0,0,62,68,3,10,5,0,63,68,3,14,7,0,64,68,3,4,2,0,65,68,3,8,
        4,0,66,68,3,22,11,0,67,62,1,0,0,0,67,63,1,0,0,0,67,64,1,0,0,0,67,
        65,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,70,5,44,0,0,70,71,5,54,
        0,0,71,75,5,21,0,0,72,74,3,6,3,0,73,72,1,0,0,0,74,77,1,0,0,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,22,
        0,0,79,5,1,0,0,0,80,81,3,20,10,0,81,82,5,54,0,0,82,83,5,17,0,0,83,
        7,1,0,0,0,84,85,5,38,0,0,85,86,5,54,0,0,86,87,5,17,0,0,87,9,1,0,
        0,0,88,89,3,20,10,0,89,92,5,54,0,0,90,91,5,16,0,0,91,93,3,46,23,
        0,92,90,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,95,5,17,0,0,95,105,
        1,0,0,0,96,97,3,20,10,0,97,98,5,23,0,0,98,99,5,24,0,0,99,100,5,54,
        0,0,100,101,5,16,0,0,101,102,3,12,6,0,102,103,5,17,0,0,103,105,1,
        0,0,0,104,88,1,0,0,0,104,96,1,0,0,0,105,11,1,0,0,0,106,115,5,23,
        0,0,107,112,3,46,23,0,108,109,5,18,0,0,109,111,3,46,23,0,110,108,
        1,0,0,0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,116,
        1,0,0,0,114,112,1,0,0,0,115,107,1,0,0,0,115,116,1,0,0,0,116,117,
        1,0,0,0,117,118,5,24,0,0,118,13,1,0,0,0,119,120,3,20,10,0,120,121,
        5,54,0,0,121,123,5,19,0,0,122,124,3,16,8,0,123,122,1,0,0,0,123,124,
        1,0,0,0,124,125,1,0,0,0,125,126,5,20,0,0,126,127,3,30,15,0,127,15,
        1,0,0,0,128,133,3,18,9,0,129,130,5,18,0,0,130,132,3,18,9,0,131,129,
        1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,17,1,
        0,0,0,135,133,1,0,0,0,136,137,3,20,10,0,137,138,5,54,0,0,138,19,
        1,0,0,0,139,149,5,45,0,0,140,149,5,46,0,0,141,149,5,47,0,0,142,149,
        5,48,0,0,143,149,5,49,0,0,144,145,5,45,0,0,145,146,5,23,0,0,146,
        149,5,24,0,0,147,149,5,54,0,0,148,139,1,0,0,0,148,140,1,0,0,0,148,
        141,1,0,0,0,148,142,1,0,0,0,148,143,1,0,0,0,148,144,1,0,0,0,148,
        147,1,0,0,0,149,21,1,0,0,0,150,151,3,34,17,0,151,152,5,17,0,0,152,
        168,1,0,0,0,153,168,3,36,18,0,154,168,3,24,12,0,155,168,3,38,19,
        0,156,168,3,40,20,0,157,168,3,42,21,0,158,168,3,44,22,0,159,160,
        5,39,0,0,160,168,5,17,0,0,161,162,5,40,0,0,162,168,5,17,0,0,163,
        168,3,30,15,0,164,165,3,46,23,0,165,166,5,17,0,0,166,168,1,0,0,0,
        167,150,1,0,0,0,167,153,1,0,0,0,167,154,1,0,0,0,167,155,1,0,0,0,
        167,156,1,0,0,0,167,157,1,0,0,0,167,158,1,0,0,0,167,159,1,0,0,0,
        167,161,1,0,0,0,167,163,1,0,0,0,167,164,1,0,0,0,168,23,1,0,0,0,169,
        170,5,41,0,0,170,171,5,19,0,0,171,172,3,46,23,0,172,173,5,20,0,0,
        173,177,5,21,0,0,174,176,3,26,13,0,175,174,1,0,0,0,176,179,1,0,0,
        0,177,175,1,0,0,0,177,178,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,
        0,180,182,3,28,14,0,181,180,1,0,0,0,181,182,1,0,0,0,182,183,1,0,
        0,0,183,184,5,22,0,0,184,25,1,0,0,0,185,186,5,42,0,0,186,187,3,46,
        23,0,187,191,5,25,0,0,188,190,3,22,11,0,189,188,1,0,0,0,190,193,
        1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,27,1,0,0,0,193,191,1,
        0,0,0,194,195,5,43,0,0,195,199,5,25,0,0,196,198,3,22,11,0,197,196,
        1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,29,1,
        0,0,0,201,199,1,0,0,0,202,206,5,21,0,0,203,205,3,22,11,0,204,203,
        1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,209,
        1,0,0,0,208,206,1,0,0,0,209,210,5,22,0,0,210,31,1,0,0,0,211,216,
        5,54,0,0,212,213,5,27,0,0,213,215,5,54,0,0,214,212,1,0,0,0,215,218,
        1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,33,1,0,0,0,218,216,1,
        0,0,0,219,220,3,32,16,0,220,221,5,16,0,0,221,222,3,46,23,0,222,35,
        1,0,0,0,223,224,5,31,0,0,224,225,5,19,0,0,225,226,3,46,23,0,226,
        227,5,20,0,0,227,228,5,32,0,0,228,231,3,30,15,0,229,230,5,33,0,0,
        230,232,3,30,15,0,231,229,1,0,0,0,231,232,1,0,0,0,232,37,1,0,0,0,
        233,234,5,34,0,0,234,235,5,19,0,0,235,236,3,46,23,0,236,237,5,20,
        0,0,237,238,3,30,15,0,238,39,1,0,0,0,239,240,5,35,0,0,240,246,5,
        19,0,0,241,247,3,10,5,0,242,243,3,34,17,0,243,244,5,17,0,0,244,247,
        1,0,0,0,245,247,5,17,0,0,246,241,1,0,0,0,246,242,1,0,0,0,246,245,
        1,0,0,0,247,249,1,0,0,0,248,250,3,46,23,0,249,248,1,0,0,0,249,250,
        1,0,0,0,250,251,1,0,0,0,251,254,5,17,0,0,252,255,3,34,17,0,253,255,
        3,46,23,0,254,252,1,0,0,0,254,253,1,0,0,0,254,255,1,0,0,0,255,256,
        1,0,0,0,256,257,5,20,0,0,257,258,3,30,15,0,258,41,1,0,0,0,259,260,
        5,36,0,0,260,261,5,19,0,0,261,262,3,46,23,0,262,263,5,20,0,0,263,
        264,5,17,0,0,264,43,1,0,0,0,265,267,5,37,0,0,266,268,3,46,23,0,267,
        266,1,0,0,0,267,268,1,0,0,0,268,269,1,0,0,0,269,270,5,17,0,0,270,
        45,1,0,0,0,271,272,6,23,-1,0,272,273,5,15,0,0,273,299,3,46,23,18,
        274,275,5,19,0,0,275,276,3,20,10,0,276,277,5,20,0,0,277,278,3,46,
        23,17,278,299,1,0,0,0,279,280,5,19,0,0,280,281,3,46,23,0,281,282,
        5,20,0,0,282,299,1,0,0,0,283,299,5,52,0,0,284,299,5,53,0,0,285,299,
        7,0,0,0,286,287,5,54,0,0,287,289,5,19,0,0,288,290,3,48,24,0,289,
        288,1,0,0,0,289,290,1,0,0,0,290,291,1,0,0,0,291,299,5,20,0,0,292,
        293,5,54,0,0,293,294,5,23,0,0,294,295,3,46,23,0,295,296,5,24,0,0,
        296,299,1,0,0,0,297,299,5,54,0,0,298,271,1,0,0,0,298,274,1,0,0,0,
        298,279,1,0,0,0,298,283,1,0,0,0,298,284,1,0,0,0,298,285,1,0,0,0,
        298,286,1,0,0,0,298,292,1,0,0,0,298,297,1,0,0,0,299,332,1,0,0,0,
        300,301,10,16,0,0,301,302,5,6,0,0,302,331,3,46,23,16,303,304,10,
        15,0,0,304,305,7,1,0,0,305,331,3,46,23,16,306,307,10,14,0,0,307,
        308,7,2,0,0,308,331,3,46,23,15,309,310,10,13,0,0,310,311,7,3,0,0,
        311,331,3,46,23,14,312,313,10,12,0,0,313,314,7,4,0,0,314,331,3,46,
        23,13,315,316,10,11,0,0,316,317,5,13,0,0,317,331,3,46,23,12,318,
        319,10,10,0,0,319,320,5,14,0,0,320,331,3,46,23,11,321,322,10,9,0,
        0,322,323,5,26,0,0,323,324,3,46,23,0,324,325,5,25,0,0,325,326,3,
        46,23,10,326,331,1,0,0,0,327,328,10,7,0,0,328,329,5,27,0,0,329,331,
        5,54,0,0,330,300,1,0,0,0,330,303,1,0,0,0,330,306,1,0,0,0,330,309,
        1,0,0,0,330,312,1,0,0,0,330,315,1,0,0,0,330,318,1,0,0,0,330,321,
        1,0,0,0,330,327,1,0,0,0,331,334,1,0,0,0,332,330,1,0,0,0,332,333,
        1,0,0,0,333,47,1,0,0,0,334,332,1,0,0,0,335,340,3,46,23,0,336,337,
        5,18,0,0,337,339,3,46,23,0,338,336,1,0,0,0,339,342,1,0,0,0,340,338,
        1,0,0,0,340,341,1,0,0,0,341,49,1,0,0,0,342,340,1,0,0,0,27,56,67,
        75,92,104,112,115,123,133,148,167,177,181,191,199,206,216,231,246,
        249,254,267,289,298,330,332,340
    ]

class gramatica_v4Parser ( Parser ):

    grammarFileName = "gramatica_v4.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
                     "'=='", "<INVALID>", "'>'", "'<'", "'>='", "'<='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "';'", 
                     "','", "'('", "')'", "'{'", "'}'", "'['", "']'", "':'", 
                     "'?'", "'.'", "<INVALID>", "'INICIO'", "'FIN'", "<INVALID>", 
                     "'ENTONCES'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'IMPORT'", "<INVALID>", 
                     "<INVALID>", "'switch'", "'case'", "'default'", "'struct'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "TK_SUMA", "TK_RESTA", "TK_MULT", "TK_DIV", 
                      "TK_MODULO", "TK_POTENCIA", "TK_IGUAL", "TK_DIFERENTE", 
                      "TK_MAYOR", "TK_MENOR", "TK_MAYOREQ", "TK_MENOREQ", 
                      "TK_Y", "TK_O", "TK_NOT", "ASSIGN", "SEMICOLON", "TK_COMA", 
                      "TK_PAR_IZQ", "TK_PAR_DER", "TK_LLA_IZQ", "TK_LLA_DER", 
                      "TK_COR_IZQ", "TK_COR_DER", "TK_DOS_PUNTOS", "TK_INTERROGACION", 
                      "TK_PUNTO", "TK_PROGRAMA", "TK_INICIO", "TK_FIN", 
                      "TK_SI", "TK_ENTONCES", "TK_SINO", "TK_MIENTRAS", 
                      "TK_FOR", "TK_IMPRIMIR", "TK_RETURN", "TK_IMPORT", 
                      "TK_BREAK", "TK_CONTINUE", "TK_SWITCH", "TK_CASE", 
                      "TK_DEFAULT", "TK_STRUCT", "TK_INT", "TK_FLOAT", "TK_STRING", 
                      "TK_BOOL", "TK_VOID", "TK_TRUE", "TK_FALSE", "TK_NUMERO", 
                      "TK_CADENA", "TK_ID", "WS", "COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_structDeclaration = 2
    RULE_structField = 3
    RULE_importacion = 4
    RULE_varDeclaration = 5
    RULE_arrayLiteral = 6
    RULE_funcDeclaration = 7
    RULE_params = 8
    RULE_param = 9
    RULE_type = 10
    RULE_instruccion = 11
    RULE_switchStatement = 12
    RULE_caseStatement = 13
    RULE_defaultStatement = 14
    RULE_bloque = 15
    RULE_lvalue = 16
    RULE_asignacion_core = 17
    RULE_condicional = 18
    RULE_bucle_mientras = 19
    RULE_bucle_for = 20
    RULE_impresion = 21
    RULE_sentencia_return = 22
    RULE_expr = 23
    RULE_args = 24

    ruleNames =  [ "program", "declaration", "structDeclaration", "structField", 
                   "importacion", "varDeclaration", "arrayLiteral", "funcDeclaration", 
                   "params", "param", "type", "instruccion", "switchStatement", 
                   "caseStatement", "defaultStatement", "bloque", "lvalue", 
                   "asignacion_core", "condicional", "bucle_mientras", "bucle_for", 
                   "impresion", "sentencia_return", "expr", "args" ]

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
    TK_DOS_PUNTOS=25
    TK_INTERROGACION=26
    TK_PUNTO=27
    TK_PROGRAMA=28
    TK_INICIO=29
    TK_FIN=30
    TK_SI=31
    TK_ENTONCES=32
    TK_SINO=33
    TK_MIENTRAS=34
    TK_FOR=35
    TK_IMPRIMIR=36
    TK_RETURN=37
    TK_IMPORT=38
    TK_BREAK=39
    TK_CONTINUE=40
    TK_SWITCH=41
    TK_CASE=42
    TK_DEFAULT=43
    TK_STRUCT=44
    TK_INT=45
    TK_FLOAT=46
    TK_STRING=47
    TK_BOOL=48
    TK_VOID=49
    TK_TRUE=50
    TK_FALSE=51
    TK_NUMERO=52
    TK_CADENA=53
    TK_ID=54
    WS=55
    COMMENT=56
    BLOCK_COMMENT=57

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
            return gramatica_v4Parser.RULE_program

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramG4Context(ProgramContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ProgramContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_PROGRAMA(self):
            return self.getToken(gramatica_v4Parser.TK_PROGRAMA, 0)
        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)
        def TK_INICIO(self):
            return self.getToken(gramatica_v4Parser.TK_INICIO, 0)
        def TK_FIN(self):
            return self.getToken(gramatica_v4Parser.TK_FIN, 0)
        def EOF(self):
            return self.getToken(gramatica_v4Parser.EOF, 0)
        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.DeclarationContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.DeclarationContext,i)


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

        localctx = gramatica_v4Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            localctx = gramatica_v4Parser.ProgramG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(gramatica_v4Parser.TK_PROGRAMA)
            self.state = 51
            self.match(gramatica_v4Parser.TK_ID)
            self.state = 52
            self.match(gramatica_v4Parser.TK_INICIO)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36015587849699328) != 0):
                self.state = 53
                self.declaration()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(gramatica_v4Parser.TK_FIN)
            self.state = 60
            self.match(gramatica_v4Parser.EOF)
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
            return gramatica_v4Parser.RULE_declaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclStructG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def structDeclaration(self):
            return self.getTypedRuleContext(gramatica_v4Parser.StructDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclStructG4" ):
                listener.enterDeclStructG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclStructG4" ):
                listener.exitDeclStructG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclStructG4" ):
                return visitor.visitDeclStructG4(self)
            else:
                return visitor.visitChildren(self)


    class DeclImportG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def importacion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ImportacionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclImportG4" ):
                listener.enterDeclImportG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclImportG4" ):
                listener.exitDeclImportG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclImportG4" ):
                return visitor.visitDeclImportG4(self)
            else:
                return visitor.visitChildren(self)


    class DeclInstruccionG4Context(DeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instruccion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.InstruccionContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDeclaration(self):
            return self.getTypedRuleContext(gramatica_v4Parser.VarDeclarationContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.DeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcDeclaration(self):
            return self.getTypedRuleContext(gramatica_v4Parser.FuncDeclarationContext,0)


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

        localctx = gramatica_v4Parser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = gramatica_v4Parser.DeclVariableG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.varDeclaration()
                pass

            elif la_ == 2:
                localctx = gramatica_v4Parser.DeclFuncionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.funcDeclaration()
                pass

            elif la_ == 3:
                localctx = gramatica_v4Parser.DeclStructG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.structDeclaration()
                pass

            elif la_ == 4:
                localctx = gramatica_v4Parser.DeclImportG4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.importacion()
                pass

            elif la_ == 5:
                localctx = gramatica_v4Parser.DeclInstruccionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.instruccion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_STRUCT(self):
            return self.getToken(gramatica_v4Parser.TK_STRUCT, 0)

        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)

        def TK_LLA_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_LLA_IZQ, 0)

        def TK_LLA_DER(self):
            return self.getToken(gramatica_v4Parser.TK_LLA_DER, 0)

        def structField(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.StructFieldContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.StructFieldContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_structDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDeclaration" ):
                listener.enterStructDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDeclaration" ):
                listener.exitStructDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDeclaration" ):
                return visitor.visitStructDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def structDeclaration(self):

        localctx = gramatica_v4Parser.StructDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_structDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(gramatica_v4Parser.TK_STRUCT)
            self.state = 70
            self.match(gramatica_v4Parser.TK_ID)
            self.state = 71
            self.match(gramatica_v4Parser.TK_LLA_IZQ)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 19105114044235776) != 0):
                self.state = 72
                self.structField()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(gramatica_v4Parser.TK_LLA_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(gramatica_v4Parser.TypeContext,0)


        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)

        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_structField

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructField" ):
                listener.enterStructField(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructField" ):
                listener.exitStructField(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructField" ):
                return visitor.visitStructField(self)
            else:
                return visitor.visitChildren(self)




    def structField(self):

        localctx = gramatica_v4Parser.StructFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_structField)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.type_()
            self.state = 81
            self.match(gramatica_v4Parser.TK_ID)
            self.state = 82
            self.match(gramatica_v4Parser.SEMICOLON)
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
            return self.getToken(gramatica_v4Parser.TK_IMPORT, 0)

        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)

        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_importacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportacion" ):
                listener.enterImportacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportacion" ):
                listener.exitImportacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportacion" ):
                return visitor.visitImportacion(self)
            else:
                return visitor.visitChildren(self)




    def importacion(self):

        localctx = gramatica_v4Parser.ImportacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_importacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(gramatica_v4Parser.TK_IMPORT)
            self.state = 85
            self.match(gramatica_v4Parser.TK_ID)
            self.state = 86
            self.match(gramatica_v4Parser.SEMICOLON)
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
            return gramatica_v4Parser.RULE_varDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarDeclarationG4Context(VarDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.VarDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(gramatica_v4Parser.TypeContext,0)

        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)
        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)
        def ASSIGN(self):
            return self.getToken(gramatica_v4Parser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


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


    class VarArrayDeclarationG4Context(VarDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.VarDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(gramatica_v4Parser.TypeContext,0)

        def TK_COR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_COR_IZQ, 0)
        def TK_COR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_COR_DER, 0)
        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)
        def ASSIGN(self):
            return self.getToken(gramatica_v4Parser.ASSIGN, 0)
        def arrayLiteral(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ArrayLiteralContext,0)

        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarArrayDeclarationG4" ):
                listener.enterVarArrayDeclarationG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarArrayDeclarationG4" ):
                listener.exitVarArrayDeclarationG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarArrayDeclarationG4" ):
                return visitor.visitVarArrayDeclarationG4(self)
            else:
                return visitor.visitChildren(self)



    def varDeclaration(self):

        localctx = gramatica_v4Parser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = gramatica_v4Parser.VarDeclarationG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.type_()
                self.state = 89
                self.match(gramatica_v4Parser.TK_ID)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 90
                    self.match(gramatica_v4Parser.ASSIGN)
                    self.state = 91
                    self.expr(0)


                self.state = 94
                self.match(gramatica_v4Parser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = gramatica_v4Parser.VarArrayDeclarationG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.type_()
                self.state = 97
                self.match(gramatica_v4Parser.TK_COR_IZQ)
                self.state = 98
                self.match(gramatica_v4Parser.TK_COR_DER)
                self.state = 99
                self.match(gramatica_v4Parser.TK_ID)
                self.state = 100
                self.match(gramatica_v4Parser.ASSIGN)
                self.state = 101
                self.arrayLiteral()
                self.state = 102
                self.match(gramatica_v4Parser.SEMICOLON)
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
            return self.getToken(gramatica_v4Parser.TK_COR_IZQ, 0)

        def TK_COR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_COR_DER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)


        def TK_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.TK_COMA)
            else:
                return self.getToken(gramatica_v4Parser.TK_COMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_arrayLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayLiteral" ):
                listener.enterArrayLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayLiteral" ):
                listener.exitArrayLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayLiteral" ):
                return visitor.visitArrayLiteral(self)
            else:
                return visitor.visitChildren(self)




    def arrayLiteral(self):

        localctx = gramatica_v4Parser.ArrayLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arrayLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(gramatica_v4Parser.TK_COR_IZQ)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34902897112678400) != 0):
                self.state = 107
                self.expr(0)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 108
                    self.match(gramatica_v4Parser.TK_COMA)
                    self.state = 109
                    self.expr(0)
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 117
            self.match(gramatica_v4Parser.TK_COR_DER)
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
            return gramatica_v4Parser.RULE_funcDeclaration

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncDeclarationG4Context(FuncDeclarationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.FuncDeclarationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(gramatica_v4Parser.TypeContext,0)

        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)
        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)
        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)
        def bloque(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BloqueContext,0)

        def params(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ParamsContext,0)


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

        localctx = gramatica_v4Parser.FuncDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcDeclaration)
        self._la = 0 # Token type
        try:
            localctx = gramatica_v4Parser.FuncDeclarationG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.type_()
            self.state = 120
            self.match(gramatica_v4Parser.TK_ID)
            self.state = 121
            self.match(gramatica_v4Parser.TK_PAR_IZQ)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 19105114044235776) != 0):
                self.state = 122
                self.params()


            self.state = 125
            self.match(gramatica_v4Parser.TK_PAR_DER)
            self.state = 126
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
                return self.getTypedRuleContexts(gramatica_v4Parser.ParamContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ParamContext,i)


        def TK_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.TK_COMA)
            else:
                return self.getToken(gramatica_v4Parser.TK_COMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_params

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

        localctx = gramatica_v4Parser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.param()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 129
                self.match(gramatica_v4Parser.TK_COMA)
                self.state = 130
                self.param()
                self.state = 135
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
            return self.getTypedRuleContext(gramatica_v4Parser.TypeContext,0)


        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_param

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

        localctx = gramatica_v4Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.type_()
            self.state = 137
            self.match(gramatica_v4Parser.TK_ID)
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
            return gramatica_v4Parser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeVoidG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_VOID(self):
            return self.getToken(gramatica_v4Parser.TK_VOID, 0)

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


    class TypeStringG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_STRING(self):
            return self.getToken(gramatica_v4Parser.TK_STRING, 0)

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


    class TypeBoolG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_BOOL(self):
            return self.getToken(gramatica_v4Parser.TK_BOOL, 0)

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


    class TypeIntArrayG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_INT(self):
            return self.getToken(gramatica_v4Parser.TK_INT, 0)
        def TK_COR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_COR_IZQ, 0)
        def TK_COR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_COR_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeIntArrayG4" ):
                listener.enterTypeIntArrayG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeIntArrayG4" ):
                listener.exitTypeIntArrayG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeIntArrayG4" ):
                return visitor.visitTypeIntArrayG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeIntG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_INT(self):
            return self.getToken(gramatica_v4Parser.TK_INT, 0)

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


    class TypeStructG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeStructG4" ):
                listener.enterTypeStructG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeStructG4" ):
                listener.exitTypeStructG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeStructG4" ):
                return visitor.visitTypeStructG4(self)
            else:
                return visitor.visitChildren(self)


    class TypeFloatG4Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_FLOAT(self):
            return self.getToken(gramatica_v4Parser.TK_FLOAT, 0)

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

        localctx = gramatica_v4Parser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = gramatica_v4Parser.TypeIntG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 139
                self.match(gramatica_v4Parser.TK_INT)
                pass

            elif la_ == 2:
                localctx = gramatica_v4Parser.TypeFloatG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 140
                self.match(gramatica_v4Parser.TK_FLOAT)
                pass

            elif la_ == 3:
                localctx = gramatica_v4Parser.TypeStringG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                self.match(gramatica_v4Parser.TK_STRING)
                pass

            elif la_ == 4:
                localctx = gramatica_v4Parser.TypeBoolG4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 142
                self.match(gramatica_v4Parser.TK_BOOL)
                pass

            elif la_ == 5:
                localctx = gramatica_v4Parser.TypeVoidG4Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 143
                self.match(gramatica_v4Parser.TK_VOID)
                pass

            elif la_ == 6:
                localctx = gramatica_v4Parser.TypeIntArrayG4Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 144
                self.match(gramatica_v4Parser.TK_INT)
                self.state = 145
                self.match(gramatica_v4Parser.TK_COR_IZQ)
                self.state = 146
                self.match(gramatica_v4Parser.TK_COR_DER)
                pass

            elif la_ == 7:
                localctx = gramatica_v4Parser.TypeStructG4Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 147
                self.match(gramatica_v4Parser.TK_ID)
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
            return gramatica_v4Parser.RULE_instruccion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SentenciaForG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bucle_for(self):
            return self.getTypedRuleContext(gramatica_v4Parser.Bucle_forContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def impresion(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ImpresionContext,0)


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


    class SentenciaContinueG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_CONTINUE(self):
            return self.getToken(gramatica_v4Parser.TK_CONTINUE, 0)
        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaContinueG4" ):
                listener.enterSentenciaContinueG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaContinueG4" ):
                listener.exitSentenciaContinueG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaContinueG4" ):
                return visitor.visitSentenciaContinueG4(self)
            else:
                return visitor.visitChildren(self)


    class StatBloqueG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BloqueContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def asignacion_core(self):
            return self.getTypedRuleContext(gramatica_v4Parser.Asignacion_coreContext,0)

        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

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


    class SentenciaSwitchG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def switchStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.SwitchStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaSwitchG4" ):
                listener.enterSentenciaSwitchG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaSwitchG4" ):
                listener.exitSentenciaSwitchG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaSwitchG4" ):
                return visitor.visitSentenciaSwitchG4(self)
            else:
                return visitor.visitChildren(self)


    class SentenciaExpresionG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)

        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condicional(self):
            return self.getTypedRuleContext(gramatica_v4Parser.CondicionalContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bucle_mientras(self):
            return self.getTypedRuleContext(gramatica_v4Parser.Bucle_mientrasContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sentencia_return(self):
            return self.getTypedRuleContext(gramatica_v4Parser.Sentencia_returnContext,0)


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


    class SentenciaBreakG4Context(InstruccionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.InstruccionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_BREAK(self):
            return self.getToken(gramatica_v4Parser.TK_BREAK, 0)
        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentenciaBreakG4" ):
                listener.enterSentenciaBreakG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentenciaBreakG4" ):
                listener.exitSentenciaBreakG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentenciaBreakG4" ):
                return visitor.visitSentenciaBreakG4(self)
            else:
                return visitor.visitChildren(self)



    def instruccion(self):

        localctx = gramatica_v4Parser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_instruccion)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = gramatica_v4Parser.AsignacionVariableG4Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.asignacion_core()
                self.state = 151
                self.match(gramatica_v4Parser.SEMICOLON)
                pass

            elif la_ == 2:
                localctx = gramatica_v4Parser.SentenciaIfElseG4Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.condicional()
                pass

            elif la_ == 3:
                localctx = gramatica_v4Parser.SentenciaSwitchG4Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.switchStatement()
                pass

            elif la_ == 4:
                localctx = gramatica_v4Parser.SentenciaMientrasG4Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 155
                self.bucle_mientras()
                pass

            elif la_ == 5:
                localctx = gramatica_v4Parser.SentenciaForG4Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 156
                self.bucle_for()
                pass

            elif la_ == 6:
                localctx = gramatica_v4Parser.SentenciaImprimirG4Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 157
                self.impresion()
                pass

            elif la_ == 7:
                localctx = gramatica_v4Parser.SentenciaReturnG4Context(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 158
                self.sentencia_return()
                pass

            elif la_ == 8:
                localctx = gramatica_v4Parser.SentenciaBreakG4Context(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 159
                self.match(gramatica_v4Parser.TK_BREAK)
                self.state = 160
                self.match(gramatica_v4Parser.SEMICOLON)
                pass

            elif la_ == 9:
                localctx = gramatica_v4Parser.SentenciaContinueG4Context(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 161
                self.match(gramatica_v4Parser.TK_CONTINUE)
                self.state = 162
                self.match(gramatica_v4Parser.SEMICOLON)
                pass

            elif la_ == 10:
                localctx = gramatica_v4Parser.StatBloqueG4Context(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 163
                self.bloque()
                pass

            elif la_ == 11:
                localctx = gramatica_v4Parser.SentenciaExpresionG4Context(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 164
                self.expr(0)
                self.state = 165
                self.match(gramatica_v4Parser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_SWITCH(self):
            return self.getToken(gramatica_v4Parser.TK_SWITCH, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)

        def TK_LLA_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_LLA_IZQ, 0)

        def TK_LLA_DER(self):
            return self.getToken(gramatica_v4Parser.TK_LLA_DER, 0)

        def caseStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.CaseStatementContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.CaseStatementContext,i)


        def defaultStatement(self):
            return self.getTypedRuleContext(gramatica_v4Parser.DefaultStatementContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = gramatica_v4Parser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(gramatica_v4Parser.TK_SWITCH)
            self.state = 170
            self.match(gramatica_v4Parser.TK_PAR_IZQ)
            self.state = 171
            self.expr(0)
            self.state = 172
            self.match(gramatica_v4Parser.TK_PAR_DER)
            self.state = 173
            self.match(gramatica_v4Parser.TK_LLA_IZQ)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 174
                self.caseStatement()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 180
                self.defaultStatement()


            self.state = 183
            self.match(gramatica_v4Parser.TK_LLA_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_CASE(self):
            return self.getToken(gramatica_v4Parser.TK_CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def TK_DOS_PUNTOS(self):
            return self.getToken(gramatica_v4Parser.TK_DOS_PUNTOS, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_caseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStatement" ):
                listener.enterCaseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStatement" ):
                listener.exitCaseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseStatement" ):
                return visitor.visitCaseStatement(self)
            else:
                return visitor.visitChildren(self)




    def caseStatement(self):

        localctx = gramatica_v4Parser.CaseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_caseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(gramatica_v4Parser.TK_CASE)
            self.state = 186
            self.expr(0)
            self.state = 187
            self.match(gramatica_v4Parser.TK_DOS_PUNTOS)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34907005250994176) != 0):
                self.state = 188
                self.instruccion()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_DEFAULT(self):
            return self.getToken(gramatica_v4Parser.TK_DEFAULT, 0)

        def TK_DOS_PUNTOS(self):
            return self.getToken(gramatica_v4Parser.TK_DOS_PUNTOS, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_defaultStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultStatement" ):
                listener.enterDefaultStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultStatement" ):
                listener.exitDefaultStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultStatement" ):
                return visitor.visitDefaultStatement(self)
            else:
                return visitor.visitChildren(self)




    def defaultStatement(self):

        localctx = gramatica_v4Parser.DefaultStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_defaultStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(gramatica_v4Parser.TK_DEFAULT)
            self.state = 195
            self.match(gramatica_v4Parser.TK_DOS_PUNTOS)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34907005250994176) != 0):
                self.state = 196
                self.instruccion()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(gramatica_v4Parser.TK_LLA_IZQ, 0)

        def TK_LLA_DER(self):
            return self.getToken(gramatica_v4Parser.TK_LLA_DER, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.InstruccionContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.InstruccionContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_bloque

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

        localctx = gramatica_v4Parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(gramatica_v4Parser.TK_LLA_IZQ)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34907005250994176) != 0):
                self.state = 203
                self.instruccion()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
            self.match(gramatica_v4Parser.TK_LLA_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.TK_ID)
            else:
                return self.getToken(gramatica_v4Parser.TK_ID, i)

        def TK_PUNTO(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.TK_PUNTO)
            else:
                return self.getToken(gramatica_v4Parser.TK_PUNTO, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLvalue" ):
                return visitor.visitLvalue(self)
            else:
                return visitor.visitChildren(self)




    def lvalue(self):

        localctx = gramatica_v4Parser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_lvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(gramatica_v4Parser.TK_ID)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27:
                self.state = 212
                self.match(gramatica_v4Parser.TK_PUNTO)
                self.state = 213
                self.match(gramatica_v4Parser.TK_ID)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return gramatica_v4Parser.RULE_asignacion_core

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionCoreG4Context(Asignacion_coreContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.Asignacion_coreContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lvalue(self):
            return self.getTypedRuleContext(gramatica_v4Parser.LvalueContext,0)

        def ASSIGN(self):
            return self.getToken(gramatica_v4Parser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


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

        localctx = gramatica_v4Parser.Asignacion_coreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_asignacion_core)
        try:
            localctx = gramatica_v4Parser.AsignacionCoreG4Context(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.lvalue()
            self.state = 220
            self.match(gramatica_v4Parser.ASSIGN)
            self.state = 221
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
            return self.getToken(gramatica_v4Parser.TK_SI, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)

        def TK_ENTONCES(self):
            return self.getToken(gramatica_v4Parser.TK_ENTONCES, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.BloqueContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.BloqueContext,i)


        def TK_SINO(self):
            return self.getToken(gramatica_v4Parser.TK_SINO, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_condicional

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

        localctx = gramatica_v4Parser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(gramatica_v4Parser.TK_SI)
            self.state = 224
            self.match(gramatica_v4Parser.TK_PAR_IZQ)
            self.state = 225
            self.expr(0)
            self.state = 226
            self.match(gramatica_v4Parser.TK_PAR_DER)
            self.state = 227
            self.match(gramatica_v4Parser.TK_ENTONCES)
            self.state = 228
            self.bloque()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 229
                self.match(gramatica_v4Parser.TK_SINO)
                self.state = 230
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
            return self.getToken(gramatica_v4Parser.TK_MIENTRAS, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BloqueContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_bucle_mientras

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

        localctx = gramatica_v4Parser.Bucle_mientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_bucle_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(gramatica_v4Parser.TK_MIENTRAS)
            self.state = 234
            self.match(gramatica_v4Parser.TK_PAR_IZQ)
            self.state = 235
            self.expr(0)
            self.state = 236
            self.match(gramatica_v4Parser.TK_PAR_DER)
            self.state = 237
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
            return self.getToken(gramatica_v4Parser.TK_FOR, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.SEMICOLON)
            else:
                return self.getToken(gramatica_v4Parser.SEMICOLON, i)

        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)

        def bloque(self):
            return self.getTypedRuleContext(gramatica_v4Parser.BloqueContext,0)


        def varDeclaration(self):
            return self.getTypedRuleContext(gramatica_v4Parser.VarDeclarationContext,0)


        def asignacion_core(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.Asignacion_coreContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.Asignacion_coreContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_bucle_for

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

        localctx = gramatica_v4Parser.Bucle_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_bucle_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(gramatica_v4Parser.TK_FOR)
            self.state = 240
            self.match(gramatica_v4Parser.TK_PAR_IZQ)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 241
                localctx.init_var = self.varDeclaration()
                pass

            elif la_ == 2:
                self.state = 242
                localctx.init_assign = self.asignacion_core()
                self.state = 243
                self.match(gramatica_v4Parser.SEMICOLON)
                pass

            elif la_ == 3:
                self.state = 245
                self.match(gramatica_v4Parser.SEMICOLON)
                pass


            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34902897112678400) != 0):
                self.state = 248
                localctx.cond = self.expr(0)


            self.state = 251
            self.match(gramatica_v4Parser.SEMICOLON)
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 252
                localctx.update_assign = self.asignacion_core()

            elif la_ == 2:
                self.state = 253
                localctx.update_expr = self.expr(0)


            self.state = 256
            self.match(gramatica_v4Parser.TK_PAR_DER)
            self.state = 257
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
            return self.getToken(gramatica_v4Parser.TK_IMPRIMIR, 0)

        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)

        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_impresion

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

        localctx = gramatica_v4Parser.ImpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_impresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(gramatica_v4Parser.TK_IMPRIMIR)
            self.state = 260
            self.match(gramatica_v4Parser.TK_PAR_IZQ)
            self.state = 261
            self.expr(0)
            self.state = 262
            self.match(gramatica_v4Parser.TK_PAR_DER)
            self.state = 263
            self.match(gramatica_v4Parser.SEMICOLON)
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
            return self.getToken(gramatica_v4Parser.TK_RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(gramatica_v4Parser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_sentencia_return

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

        localctx = gramatica_v4Parser.Sentencia_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sentencia_return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(gramatica_v4Parser.TK_RETURN)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34902897112678400) != 0):
                self.state = 266
                self.expr(0)


            self.state = 269
            self.match(gramatica_v4Parser.SEMICOLON)
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
            return gramatica_v4Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprRelacionalCompG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)

        def TK_MAYOR(self):
            return self.getToken(gramatica_v4Parser.TK_MAYOR, 0)
        def TK_MENOR(self):
            return self.getToken(gramatica_v4Parser.TK_MENOR, 0)
        def TK_MAYOREQ(self):
            return self.getToken(gramatica_v4Parser.TK_MAYOREQ, 0)
        def TK_MENOREQ(self):
            return self.getToken(gramatica_v4Parser.TK_MENOREQ, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)

        def TK_POTENCIA(self):
            return self.getToken(gramatica_v4Parser.TK_POTENCIA, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)

        def TK_O(self):
            return self.getToken(gramatica_v4Parser.TK_O, 0)

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


    class ExprTernarioG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)

        def TK_INTERROGACION(self):
            return self.getToken(gramatica_v4Parser.TK_INTERROGACION, 0)
        def TK_DOS_PUNTOS(self):
            return self.getToken(gramatica_v4Parser.TK_DOS_PUNTOS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprTernarioG4" ):
                listener.enterExprTernarioG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprTernarioG4" ):
                listener.exitExprTernarioG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprTernarioG4" ):
                return visitor.visitExprTernarioG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprAritmeticaSumaResG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)

        def TK_SUMA(self):
            return self.getToken(gramatica_v4Parser.TK_SUMA, 0)
        def TK_RESTA(self):
            return self.getToken(gramatica_v4Parser.TK_RESTA, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)
        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)
        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)
        def args(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ArgsContext,0)


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


    class ExprArrayAccessG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)
        def TK_COR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_COR_IZQ, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)

        def TK_COR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_COR_DER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprArrayAccessG4" ):
                listener.enterExprArrayAccessG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprArrayAccessG4" ):
                listener.exitExprArrayAccessG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArrayAccessG4" ):
                return visitor.visitExprArrayAccessG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicaAndG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)

        def TK_Y(self):
            return self.getToken(gramatica_v4Parser.TK_Y, 0)

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


    class ExprAritmeticaMultDivModG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)

        def TK_MULT(self):
            return self.getToken(gramatica_v4Parser.TK_MULT, 0)
        def TK_DIV(self):
            return self.getToken(gramatica_v4Parser.TK_DIV, 0)
        def TK_MODULO(self):
            return self.getToken(gramatica_v4Parser.TK_MODULO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAritmeticaMultDivModG4" ):
                listener.enterExprAritmeticaMultDivModG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAritmeticaMultDivModG4" ):
                listener.exitExprAritmeticaMultDivModG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAritmeticaMultDivModG4" ):
                return visitor.visitExprAritmeticaMultDivModG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprAccesoCampoG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)

        def TK_PUNTO(self):
            return self.getToken(gramatica_v4Parser.TK_PUNTO, 0)
        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprAccesoCampoG4" ):
                listener.enterExprAccesoCampoG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprAccesoCampoG4" ):
                listener.exitExprAccesoCampoG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAccesoCampoG4" ):
                return visitor.visitExprAccesoCampoG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicaNotG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_NOT(self):
            return self.getToken(gramatica_v4Parser.TK_NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)

        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_TRUE(self):
            return self.getToken(gramatica_v4Parser.TK_TRUE, 0)
        def TK_FALSE(self):
            return self.getToken(gramatica_v4Parser.TK_FALSE, 0)

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


    class ExprCastingG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_PAR_IZQ(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_IZQ, 0)
        def type_(self):
            return self.getTypedRuleContext(gramatica_v4Parser.TypeContext,0)

        def TK_PAR_DER(self):
            return self.getToken(gramatica_v4Parser.TK_PAR_DER, 0)
        def expr(self):
            return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprCastingG4" ):
                listener.enterExprCastingG4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprCastingG4" ):
                listener.exitExprCastingG4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprCastingG4" ):
                return visitor.visitExprCastingG4(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralCadenaG4Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_CADENA(self):
            return self.getToken(gramatica_v4Parser.TK_CADENA, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)

        def TK_IGUAL(self):
            return self.getToken(gramatica_v4Parser.TK_IGUAL, 0)
        def TK_DIFERENTE(self):
            return self.getToken(gramatica_v4Parser.TK_DIFERENTE, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_ID(self):
            return self.getToken(gramatica_v4Parser.TK_ID, 0)

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

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gramatica_v4Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TK_NUMERO(self):
            return self.getToken(gramatica_v4Parser.TK_NUMERO, 0)

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
        localctx = gramatica_v4Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                localctx = gramatica_v4Parser.ExprLogicaNotG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 272
                self.match(gramatica_v4Parser.TK_NOT)
                self.state = 273
                self.expr(18)
                pass

            elif la_ == 2:
                localctx = gramatica_v4Parser.ExprCastingG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 274
                self.match(gramatica_v4Parser.TK_PAR_IZQ)
                self.state = 275
                self.type_()
                self.state = 276
                self.match(gramatica_v4Parser.TK_PAR_DER)
                self.state = 277
                self.expr(17)
                pass

            elif la_ == 3:
                localctx = gramatica_v4Parser.ExprAgrupacionG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 279
                self.match(gramatica_v4Parser.TK_PAR_IZQ)
                self.state = 280
                self.expr(0)
                self.state = 281
                self.match(gramatica_v4Parser.TK_PAR_DER)
                pass

            elif la_ == 4:
                localctx = gramatica_v4Parser.ExprLiteralNumericaG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 283
                self.match(gramatica_v4Parser.TK_NUMERO)
                pass

            elif la_ == 5:
                localctx = gramatica_v4Parser.ExprLiteralCadenaG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 284
                self.match(gramatica_v4Parser.TK_CADENA)
                pass

            elif la_ == 6:
                localctx = gramatica_v4Parser.ExprLiteralBoolG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 285
                _la = self._input.LA(1)
                if not(_la==50 or _la==51):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 7:
                localctx = gramatica_v4Parser.ExprLlamadaFuncionG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 286
                self.match(gramatica_v4Parser.TK_ID)
                self.state = 287
                self.match(gramatica_v4Parser.TK_PAR_IZQ)
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34902897112678400) != 0):
                    self.state = 288
                    self.args()


                self.state = 291
                self.match(gramatica_v4Parser.TK_PAR_DER)
                pass

            elif la_ == 8:
                localctx = gramatica_v4Parser.ExprArrayAccessG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 292
                self.match(gramatica_v4Parser.TK_ID)
                self.state = 293
                self.match(gramatica_v4Parser.TK_COR_IZQ)
                self.state = 294
                self.expr(0)
                self.state = 295
                self.match(gramatica_v4Parser.TK_COR_DER)
                pass

            elif la_ == 9:
                localctx = gramatica_v4Parser.ExprReferenciaVariableG4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 297
                self.match(gramatica_v4Parser.TK_ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 332
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 330
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = gramatica_v4Parser.ExprPotenciaG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 300
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 301
                        self.match(gramatica_v4Parser.TK_POTENCIA)
                        self.state = 302
                        self.expr(16)
                        pass

                    elif la_ == 2:
                        localctx = gramatica_v4Parser.ExprAritmeticaMultDivModG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 303
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 304
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 305
                        self.expr(16)
                        pass

                    elif la_ == 3:
                        localctx = gramatica_v4Parser.ExprAritmeticaSumaResG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 306
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 307
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 308
                        self.expr(15)
                        pass

                    elif la_ == 4:
                        localctx = gramatica_v4Parser.ExprRelacionalCompG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 309
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 310
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 311
                        self.expr(14)
                        pass

                    elif la_ == 5:
                        localctx = gramatica_v4Parser.ExprRelacionalIgualdadG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 312
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 313
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 314
                        self.expr(13)
                        pass

                    elif la_ == 6:
                        localctx = gramatica_v4Parser.ExprLogicaAndG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 315
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 316
                        self.match(gramatica_v4Parser.TK_Y)
                        self.state = 317
                        self.expr(12)
                        pass

                    elif la_ == 7:
                        localctx = gramatica_v4Parser.ExprLogicaOrG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 318
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 319
                        self.match(gramatica_v4Parser.TK_O)
                        self.state = 320
                        self.expr(11)
                        pass

                    elif la_ == 8:
                        localctx = gramatica_v4Parser.ExprTernarioG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 321
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 322
                        self.match(gramatica_v4Parser.TK_INTERROGACION)
                        self.state = 323
                        self.expr(0)
                        self.state = 324
                        self.match(gramatica_v4Parser.TK_DOS_PUNTOS)
                        self.state = 325
                        self.expr(10)
                        pass

                    elif la_ == 9:
                        localctx = gramatica_v4Parser.ExprAccesoCampoG4Context(self, gramatica_v4Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 327
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 328
                        self.match(gramatica_v4Parser.TK_PUNTO)
                        self.state = 329
                        self.match(gramatica_v4Parser.TK_ID)
                        pass

             
                self.state = 334
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
                return self.getTypedRuleContexts(gramatica_v4Parser.ExprContext)
            else:
                return self.getTypedRuleContext(gramatica_v4Parser.ExprContext,i)


        def TK_COMA(self, i:int=None):
            if i is None:
                return self.getTokens(gramatica_v4Parser.TK_COMA)
            else:
                return self.getToken(gramatica_v4Parser.TK_COMA, i)

        def getRuleIndex(self):
            return gramatica_v4Parser.RULE_args

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

        localctx = gramatica_v4Parser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.expr(0)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 336
                self.match(gramatica_v4Parser.TK_COMA)
                self.state = 337
                self.expr(0)
                self.state = 342
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
        self._predicates[23] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 7)
         




