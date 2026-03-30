grammar Gramatica;

// @header { # ================================================================= # PROYECTO:
// LENGUAJE GRUPO 4 - UMG 2026 # AUTORÍA: ESTUDIANTES DE INGENIERÍA EN SISTEMAS # DESCRIPCIÓN:
// Analizador Léxico y Sintáctico Completo. #
// ================================================================= }

@lexer::header {
# Módulo de Tokenización Personalizado para el Grupo 4
import os
import datetime
}

@parser::header {
# Módulo de Árbol Sintáctico - Lógica de Estructura G4
}

@lexer::members {
def info_grupo(self):
    return "UMG-G4-COMP"

def imprimir_log_debug(self, msg):
    # Función manual para trazado de tokens en fase de desarrollo
    pass
}

@parser::members {
def obtener_version_parser(self):
    return "Build-3.41.G4"
}

// ================================================================= REGLAS SINTÁCTICAS (ESTRUCTURA
// DEL LENGUAJE) =================================================================

// Punto de entrada del programa según requisitos de estructura
program:
	TK_PROGRAMA TK_ID TK_INICIO instruccion* TK_FIN EOF # ProgramaCompletoG4;

instruccion:
	asignacion			# InstruccionAsignacionG4
	| condicional		# InstruccionCondicionalG4
	| bucle_mientras	# InstruccionBucleG4
	| impresion			# InstruccionImprimirG4
	| bloque			# InstruccionBloqueG4
	| expr SEMICOLON	# InstruccionExpresionG4;

bloque: TK_LLA_IZQ instruccion* TK_LLA_DER # BloqueCodigoG4;

asignacion: TK_ID ASSIGN expr SEMICOLON # AsignacionVariableG4;

condicional:
	TK_SI TK_PAR_IZQ expr TK_PAR_DER TK_ENTONCES bloque (
		TK_SINO bloque
	)? # SentenciaIfElseG4;

bucle_mientras:
	TK_MIENTRAS TK_PAR_IZQ expr TK_PAR_DER bloque # SentenciaMientrasG4;

impresion:
	TK_IMPRIMIR TK_PAR_IZQ expr TK_PAR_DER SEMICOLON # SentenciaImprimirG4;

// Jerarquía de Expresiones (Aritméticas, Relacionales y Lógicas)
expr:
	TK_NOT expr													# ExprLogicaNotG4
	| <assoc = right> expr TK_POTENCIA expr						# ExprPotenciaG4
	| expr (TK_MULT | TK_DIV) expr								# ExprAritmeticaMultDivG4
	| expr (TK_SUMA | TK_RESTA) expr							# ExprAritmeticaSumaResG4
	| expr (TK_MAYOR | TK_MENOR | TK_MAYOREQ | TK_MENOREQ) expr	# ExprRelacionalCompG4
	| expr (TK_IGUAL | TK_DIFERENTE) expr						# ExprRelacionalIgualdadG4
	| expr TK_Y expr											# ExprLogicaAndG4
	| expr TK_O expr											# ExprLogicaOrG4
	| TK_PAR_IZQ expr TK_PAR_DER								# ExprAgrupacionG4
	| TK_NUMERO													# ExprLiteralNumericaG4
	| TK_CADENA													# ExprLiteralCadenaG4
	| TK_ID														# ExprReferenciaVariableG4;

// =================================================================

// Operadores Aritméticos
TK_SUMA: '+';
TK_RESTA: '-';
TK_MULT: '*';
TK_DIV: '/';
TK_POTENCIA: '^';

// Operadores Relacionales (Símbolos del Requisito)
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

// Delimitadores y Asignación
ASSIGN: '=';
SEMICOLON: ';';
TK_PAR_IZQ: '(';
TK_PAR_DER: ')';
TK_LLA_IZQ: '{';
TK_LLA_DER: '}';
TK_COR_IZQ: '[';
TK_COR_DER: ']';

// Palabras Reservadas
TK_PROGRAMA: 'PROGRAMA';
TK_INICIO: 'INICIO';
TK_FIN: 'FIN';
TK_SI: 'SI';
TK_ENTONCES: 'ENTONCES';
TK_SINO: 'SINO';
TK_MIENTRAS: 'MIENTRAS';
TK_IMPRIMIR: 'IMPRIMIR';

// Literales e Identificadores
TK_NUMERO: [0-9]+ ('.' [0-9]+)?;
TK_CADENA: '"' (~["\r\n])* '"';
TK_ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Manejo de espacios (Ocultos para el Parser)
WS: [ \t\r\n]+ -> skip;

COMMENT: '//' ~[\n\r]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
