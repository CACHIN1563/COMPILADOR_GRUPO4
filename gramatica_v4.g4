grammar gramatica_v4;

// @header { # ================================================================= # PROYECTO:
// LENGUAJE GRUPO 4 - UMG 2026 # INGENIERÍA EN SISTEMAS # DESCRIPCIÓN:
// Analizador Léxico, Sintáctico y Semántico Completo (v4). #
// ================================================================= }

@lexer::header {
# Módulo de Tokenización Personalizado para el Grupo 4
import os
import datetime
}

@parser::header {
# Módulo de Árbol Sintáctico - Lógica de Estructura G4
}

// ================================================================= REGLAS SINTÁCTICAS
// =================================================================

program:
    TK_PROGRAMA TK_ID TK_INICIO (declaration)* TK_FIN EOF # ProgramG4;

declaration:
    varDeclaration      # DeclVariableG4
    | funcDeclaration   # DeclFuncionG4
    | structDeclaration # DeclStructG4
    | importacion       # DeclImportG4
    | instruccion       # DeclInstruccionG4;

structDeclaration:
    TK_STRUCT TK_ID TK_LLA_IZQ (structField)* TK_LLA_DER;

structField:
    type TK_ID SEMICOLON;

importacion:
    TK_IMPORT TK_ID SEMICOLON;

varDeclaration
    : type TK_ID (ASSIGN expr)? SEMICOLON              # VarDeclarationG4
    | type TK_COR_IZQ TK_COR_DER TK_ID ASSIGN arrayLiteral SEMICOLON # VarArrayDeclarationG4
    ;

arrayLiteral
    : TK_COR_IZQ (expr (TK_COMA expr)*)? TK_COR_DER
    ;

funcDeclaration:
    type TK_ID TK_PAR_IZQ params? TK_PAR_DER bloque # FuncDeclarationG4;

params:
    param (TK_COMA param)*;

param:
    type TK_ID;

type
    : TK_INT                                  # TypeIntG4
    | TK_FLOAT                                # TypeFloatG4
    | TK_STRING                               # TypeStringG4
    | TK_BOOL                                 # TypeBoolG4
    | TK_VOID                                 # TypeVoidG4
    | TK_INT TK_COR_IZQ TK_COR_DER            # TypeIntArrayG4
    | TK_ID                                   # TypeStructG4
    ;

instruccion
    : asignacion_core SEMICOLON              # AsignacionVariableG4
    | condicional                            # SentenciaIfElseG4
    | switchStatement                        # SentenciaSwitchG4
    | bucle_mientras                         # SentenciaMientrasG4
    | bucle_for                              # SentenciaForG4
    | impresion                              # SentenciaImprimirG4
    | sentencia_return                       # SentenciaReturnG4
    | TK_BREAK SEMICOLON                     # SentenciaBreakG4
    | TK_CONTINUE SEMICOLON                  # SentenciaContinueG4
    | bloque                                 # StatBloqueG4
    | expr SEMICOLON                         # SentenciaExpresionG4
    ;

switchStatement:
    TK_SWITCH TK_PAR_IZQ expr TK_PAR_DER TK_LLA_IZQ caseStatement* defaultStatement? TK_LLA_DER;

caseStatement:
    TK_CASE expr TK_DOS_PUNTOS instruccion*;

defaultStatement:
    TK_DEFAULT TK_DOS_PUNTOS instruccion*;

bloque:
    TK_LLA_IZQ instruccion* TK_LLA_DER;

lvalue:
    TK_ID (TK_PUNTO TK_ID)*;

asignacion_core:
    lvalue ASSIGN expr # AsignacionCoreG4;

condicional:
    TK_SI TK_PAR_IZQ expr TK_PAR_DER TK_ENTONCES bloque (
        TK_SINO bloque
    )?;

bucle_mientras:
    TK_MIENTRAS TK_PAR_IZQ expr TK_PAR_DER bloque;

bucle_for:
    TK_FOR TK_PAR_IZQ (init_var=varDeclaration | init_assign=asignacion_core SEMICOLON | SEMICOLON) (cond=expr)? SEMICOLON (update_assign=asignacion_core | update_expr=expr)? TK_PAR_DER bloque;

impresion:
    TK_IMPRIMIR TK_PAR_IZQ expr TK_PAR_DER SEMICOLON;

sentencia_return:
    TK_RETURN expr? SEMICOLON;

// Jerarquía de Expresiones
expr:
    TK_NOT expr                                                 # ExprLogicaNotG4
    | TK_PAR_IZQ type TK_PAR_DER expr                           # ExprCastingG4
    | <assoc = right> expr TK_POTENCIA expr                     # ExprPotenciaG4
    | expr (TK_MULT  | TK_DIV   | TK_MODULO) expr               # ExprAritmeticaMultDivModG4
    | expr (TK_SUMA | TK_RESTA) expr                            # ExprAritmeticaSumaResG4
    | expr (TK_MAYOR | TK_MENOR | TK_MAYOREQ | TK_MENOREQ) expr # ExprRelacionalCompG4
    | expr (TK_IGUAL | TK_DIFERENTE) expr                       # ExprRelacionalIgualdadG4
    | expr TK_Y expr                                            # ExprLogicaAndG4
    | expr TK_O expr                                            # ExprLogicaOrG4
    | expr TK_INTERROGACION expr TK_DOS_PUNTOS expr             # ExprTernarioG4
    | TK_PAR_IZQ expr TK_PAR_DER                                # ExprAgrupacionG4
    | expr TK_PUNTO TK_ID                                       # ExprAccesoCampoG4
    | TK_NUMERO                                                 # ExprLiteralNumericaG4
    | TK_CADENA                                                 # ExprLiteralCadenaG4
    | (TK_TRUE | TK_FALSE)                                      # ExprLiteralBoolG4
    | TK_ID TK_PAR_IZQ args? TK_PAR_DER                         # ExprLlamadaFuncionG4
    | TK_ID TK_COR_IZQ expr TK_COR_DER                          # ExprArrayAccessG4
    | TK_ID                                                     # ExprReferenciaVariableG4;

args:
    expr (TK_COMA expr)*;

// ================================================================= REGLAS LÉXICAS
// =================================================================

// Operadores Aritméticos
TK_SUMA: '+';
TK_RESTA: '-';
TK_MULT: '*';
TK_DIV: '/';
TK_MODULO: '%';
TK_POTENCIA: '^';

// Operadores Relacionales
TK_IGUAL: '==';
TK_DIFERENTE: '!=' | '<>';
TK_MAYOR: '>';
TK_MENOR: '<';
TK_MAYOREQ: '>=';
TK_MENOREQ: '<=';

// Operadores Lógicos
TK_Y: '&&' | 'Y';
TK_O: '||' | 'O';
TK_NOT: '!' | 'NOT';

// Delimitadores
ASSIGN: '=';
SEMICOLON: ';';
TK_COMA: ',';
TK_PAR_IZQ: '(';
TK_PAR_DER: ')';
TK_LLA_IZQ: '{';
TK_LLA_DER: '}';
TK_COR_IZQ: '[';
TK_COR_DER: ']';
TK_DOS_PUNTOS: ':';
TK_INTERROGACION: '?';
TK_PUNTO: '.';

// Palabras Reservadas
TK_PROGRAMA: 'PROGRAMA' | 'program';
TK_INICIO: 'INICIO';
TK_FIN: 'FIN';
TK_SI: 'SI' | 'if';
TK_ENTONCES: 'ENTONCES';
TK_SINO: 'SINO' | 'else';
TK_MIENTRAS: 'MIENTRAS' | 'while';
TK_FOR: 'FOR' | 'for';
TK_IMPRIMIR: 'IMPRIMIR' | 'print';
TK_RETURN: 'RETORNAR' | 'return';
TK_IMPORT: 'IMPORT';
TK_BREAK: 'BREAK' | 'break';
TK_CONTINUE: 'CONTINUE' | 'continue';
TK_SWITCH: 'switch';
TK_CASE: 'case';
TK_DEFAULT: 'default';
TK_STRUCT: 'struct';

// Tipos de Datos
TK_INT: 'INT' | 'int';
TK_FLOAT: 'FLOAT' | 'float';
TK_STRING: 'STRING' | 'string';
TK_BOOL: 'BOOL' | 'bool';
TK_VOID: 'VOID' | 'void';

// Booleanos
TK_TRUE: 'true';
TK_FALSE: 'false';

// Literales e Identificadores
TK_NUMERO: [0-9]+ ('.' [0-9]+)?;
TK_CADENA: '"' (~["\r\n])* '"';
TK_ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Manejo de espacios y comentarios
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\n\r]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
