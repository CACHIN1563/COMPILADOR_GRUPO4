import sys
from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from Evaluador import Evaluador

def main():
    print("--- Analizador Léxico/Sintáctico Fase 1 ---")
    input_stream = FileStream("input.txt")
    lexer = GramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GramaticaParser(stream)
    tree = parser.program()
    evaluador = Evaluador()
    evaluador.visit(tree)

if __name__ == '__main__':
    main()
