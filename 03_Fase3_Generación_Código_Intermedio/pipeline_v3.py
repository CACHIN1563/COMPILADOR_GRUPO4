import sys
import time
from antlr4 import *
from Gramatica_v3Lexer import Gramatica_v3Lexer
from Gramatica_v3Parser import Gramatica_v3Parser
from custom_errors import CustomErrorListener
from semantic_visitor_v3 import SemanticVisitorV3
from interpreter_visitor_v3 import InterpreterVisitorV3
from tac_generator import TACGenerator
from ir_generator import IRGenerator

class PipelineV3:
    def __init__(self, file_path):
        self.file_path = file_path
        self.error_listener = CustomErrorListener()

    def run(self):
        try:
            print("\n=== PIPELINE V3 ===")

            # 1. LEXICO y 2. SINTACTICO
            start_lex_sin = time.time()
            input_stream = FileStream(self.file_path, encoding='utf-8')
            lexer = Gramatica_v3Lexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(self.error_listener)

            token_stream = CommonTokenStream(lexer)
            parser = Gramatica_v3Parser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(self.error_listener)

            tree = parser.program()
            end_lex_sin = (time.time() - start_lex_sin) * 1000

            if self.error_listener.has_errors():
                print(f"\n[!] Errores léxicos/sintácticos ({end_lex_sin:.2f}ms):")
                self.error_listener.print_errors()
                return

            print(f"✔ Léxico y sintáctico OK ({end_lex_sin:.2f}ms)")

            # 3. SEMANTICO
            start_sem = time.time()
            semantic = SemanticVisitorV3()
            semantic.visit(tree)
            end_sem = (time.time() - start_sem) * 1000

            if len(semantic.errores) > 0:
                print(f"\n[!] Errores semánticos ({end_sem:.2f}ms):")
                for e in semantic.errores:
                    print(e)
                return
            
            print(f"✔ Semántico OK ({end_sem:.2f}ms)")

            # 4. TAC
            start_tac = time.time()
            print("\n>>> Generando TAC...")
            tac = TACGenerator()
            tac.visit(tree)
            end_tac = (time.time() - start_tac) * 1000

            print(f"\n--- CÓDIGO TAC ({end_tac:.2f}ms) ---")
            for line in tac.get_code():
                print(line)

            with open("salida.tac", "w", encoding="utf-8") as f:
                for line in tac.get_code():
                    f.write(line + "\n")

            # 5. LLVM IR
            start_ir = time.time()
            print("\n>>> Generando LLVM IR...")
            irgen = IRGenerator()
            irgen.visit(tree)
            llvm_ir = irgen.get_ir()
            end_ir = (time.time() - start_ir) * 1000

            print(f"\n--- LLVM IR ({end_ir:.2f}ms) ---")
            print(llvm_ir)

            with open("salida.ll", "w", encoding="utf-8") as f:
                f.write(llvm_ir)

            # 6. EJECUCION
            start_exe = time.time()
            interpreter = InterpreterVisitorV3()
            interpreter.visit(tree)
            end_exe = (time.time() - start_exe) * 1000

            print(f"\n✔ Ejecución finalizada ({end_exe:.2f}ms)")

        except Exception as e:
            print(f"\n[X] Error crítico: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 pipeline_v3.py archivo.txt")
    else:
        app = PipelineV3(sys.argv[1])
        app.run()