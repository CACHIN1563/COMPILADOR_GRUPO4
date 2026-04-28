grammar Gramatica;

// @header { # ================================================================= # PROYECTO:
// LENGUAJE GRUPO 4 - UMG 2026 # INGENIERÍA EN SISTEMAS # DESCRIPCIÓN:
// Analizador Léxico, Sintáctico y Semántico Completo. #
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
    varDeclaration    # DeclVariableG4
    | funcDeclaration # DeclFuncionG4
    | instruccion     # DeclInstruccionG4;

varDeclaration:
    type_ TK_ID (ASSIGN expr)? SEMICOLON # VarDeclarationG4;

funcDeclaration:
    type_ TK_ID TK_PAR_IZQ params? TK_PAR_DER bloque # FuncDeclarationG4;

params:
    param (TK_COMA param)*;

param:
    type_ TK_ID;

type_:
    TK_INT      # TypeIntG4
    | TK_FLOAT  # TypeFloatG4
    | TK_STRING # TypeStringG4
    | TK_BOOL   # TypeBoolG4
    | TK_VOID   # TypeVoidG4;

instruccion:
    asignacion_core SEMICOLON # AsignacionVariableG4
    | condicional             # SentenciaIfElseG4
    | bucle_mientras          # SentenciaMientrasG4
    | bucle_for               # SentenciaForG4
    | impresion               # SentenciaImprimirG4
    | sentencia_return        # SentenciaReturnG4
    | bloque                  # StatBloqueG4
    | expr SEMICOLON          # SentenciaExpresionG4;

bloque:
    TK_LLA_IZQ instruccion* TK_LLA_DER;

asignacion_core:
    TK_ID ASSIGN expr # AsignacionCoreG4;

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
    | <assoc = right> expr TK_POTENCIA expr                     # ExprPotenciaG4
    | expr (TK_MULT | TK_DIV) expr                              # ExprAritmeticaMultDivG4
    | expr (TK_SUMA | TK_RESTA) expr                            # ExprAritmeticaSumaResG4
    | expr (TK_MAYOR | TK_MENOR | TK_MAYOREQ | TK_MENOREQ) expr   # ExprRelacionalCompG4
    | expr (TK_IGUAL | TK_DIFERENTE) expr                       # ExprRelacionalIgualdadG4
    | expr TK_Y expr                                            # ExprLogicaAndG4
    | expr TK_O expr                                            # ExprLogicaOrG4
    | TK_PAR_IZQ expr TK_PAR_DER                                # ExprAgrupacionG4
    | TK_NUMERO                                                 # ExprLiteralNumericaG4
    | TK_CADENA                                                 # ExprLiteralCadenaG4
    | (TK_TRUE | TK_FALSE)                                      # ExprLiteralBoolG4
    | TK_ID TK_PAR_IZQ args? TK_PAR_DER                         # ExprLlamadaFuncionG4
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

// Palabras Reservadas
TK_PROGRAMA: 'PROGRAMA';
TK_INICIO: 'INICIO';
TK_FIN: 'FIN';
TK_SI: 'SI';
TK_ENTONCES: 'ENTONCES';
TK_SINO: 'SINO';
TK_MIENTRAS: 'MIENTRAS';
TK_FOR: 'FOR';
TK_IMPRIMIR: 'IMPRIMIR';
TK_RETURN: 'RETORNAR';

// Tipos de Datos
TK_INT: 'INT';
TK_FLOAT: 'FLOAT';
TK_STRING: 'STRING';
TK_BOOL: 'BOOL';
TK_VOID: 'VOID';

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
