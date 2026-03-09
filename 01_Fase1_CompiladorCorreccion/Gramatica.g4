grammar Gramatica;

program : (instruccion)* EOF ;

instruccion : expr ';' ;

expr : '(' expr ')' 
     | expr ('*'|'/') expr 
     | expr ('+'|'-') expr 
     | TK_NUMERO
     | TK_ID
     ;

TK_NUMERO : [0-9]+ ('.' [0-9]+)? ;
TK_ID : [a-zA-Z_][a-zA-Z0-9_]* ;
WS : [ \t\r\n]+ -> skip ;
