import sys
from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from custom_errors import CustomErrorListener
from semantic_visitor import SemanticVisitor
from interpreter_visitor import InterpreterVisitor

def main():
    input_stream = FileStream("input.txt", encoding='utf-8')
    lexer = GramaticaLexer(input_stream)
    
    error_listener = CustomErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    
    token_stream = CommonTokenStream(lexer)
    parser = GramaticaParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    tree = parser.program()
    
    if error_listener.has_errors():
        print("Errores Léxicos/Sintácticos:")
        error_listener.print_errors()
        return

    print("--- Análisis Semántico ---")
    semantic = SemanticVisitor()
    semantic.visit(tree)
    
    if len(semantic.errores) > 0:
        print("Se encontraron los siguientes errores semánticos:")
        for err in semantic.errores:
            print(err)
        return
        
    print("--- Ejecución ---")
    interpreter = InterpreterVisitor()
    interpreter.visit(tree)

main()
