import sys
from antlr4 import *
from Gramatica_v3Lexer import Gramatica_v3Lexer
from Gramatica_v3Parser import Gramatica_v3Parser
from custom_errors import CustomErrorListener
from semantic_visitor_v3 import SemanticVisitorV3
from interpreter_visitor_v3 import InterpreterVisitorV3

class PipelineV3:
    def __init__(self, file_path):
        self.file_path = file_path
        self.error_listener = CustomErrorListener()

    def run(self):
        try:
            print("\n=== PIPELINE V3 ===")

            # 1. LEXICO
            input_stream = FileStream(self.file_path, encoding='utf-8')
            lexer = Gramatica_v3Lexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(self.error_listener)

            # 2. SINTACTICO
            token_stream = CommonTokenStream(lexer)
            parser = Gramatica_v3Parser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(self.error_listener)

            tree = parser.program()

            if self.error_listener.has_errors():
                print("\n[!] Errores léxicos/sintácticos:")
                self.error_listener.print_errors()
                return

            print("✔ Léxico y sintáctico OK")

            # 3. SEMANTICO
            semantic = SemanticVisitorV3()
            semantic.visit(tree)

            if len(semantic.errores) > 0:
                print("\n[!] Errores semánticos:")
                for e in semantic.errores:
                    print(e)
                return

            print("✔ Semántico OK")

            # 4. EJECUCION
            interpreter = InterpreterVisitorV3()
            interpreter.visit(tree)

            print("\n✔ Ejecución finalizada")

        except Exception as e:
            print(f"\n[X] Error crítico: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 pipeline_v3.py archivo.txt")
    else:
        app = PipelineV3(sys.argv[1])
        app.run()