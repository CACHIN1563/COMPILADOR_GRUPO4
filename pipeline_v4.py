import sys
import time
import os
from antlr4 import *
from gramatica_v4Lexer import gramatica_v4Lexer
from gramatica_v4Parser import gramatica_v4Parser
from custom_errors import CustomErrorListener
from semantic_visitor_v4 import SemanticVisitorV4
from tac_generator_v4 import TACGeneratorV4
from ir_generator_v4 import IRGeneratorV4
from optimizer import Optimizer
from binary_generator import BinaryGenerator
# Asumiremos InterpreterVisitorV4
from interpreter_visitor_v4 import InterpreterVisitorV4

class PipelineV4:
    def __init__(self, file_path, target_os=None):
        self.file_path = file_path
        self.error_listener = CustomErrorListener()
        self.target_os = target_os # "linux", "windows" o "ambos"

    def run(self):
        try:
            print("\n=== PIPELINE V4 (PROYECTO FINAL) ===")

            # FASE 1 y 2. LÉXICO Y SINTÁCTICO
            start_lex_sin = time.time()
            input_stream = FileStream(self.file_path, encoding='utf-8')
            lexer = gramatica_v4Lexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(self.error_listener)

            token_stream = CommonTokenStream(lexer)
            parser = gramatica_v4Parser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(self.error_listener)

            tree = parser.program()
            end_lex_sin = (time.time() - start_lex_sin) * 1000

            if self.error_listener.has_errors():
                print(f"\n[!] Errores léxicos/sintácticos ({end_lex_sin:.2f}ms):")
                self.error_listener.print_errors()
                return False

            print(f"✔ Fase 1-2: Léxico y Sintáctico OK ({end_lex_sin:.2f}ms)")

            # FASE 3. SEMÁNTICO
            start_sem = time.time()
            semantic = SemanticVisitorV4()
            semantic.visit(tree)
            end_sem = (time.time() - start_sem) * 1000

            if len(semantic.errores) > 0:
                print(f"\n[!] Errores semánticos ({end_sem:.2f}ms):")
                for e in semantic.errores:
                    print(e)
                return False
            
            print(f"✔ Fase 3: Semántico OK ({end_sem:.2f}ms)")

            # FASE 4. TAC
            start_tac = time.time()
            tac = TACGeneratorV4()
            tac.visit(tree)
            end_tac = (time.time() - start_tac) * 1000

            with open("salida.tac", "w", encoding="utf-8") as f:
                for line in tac.get_code():
                    f.write(line + "\n")
            print(f"✔ Fase 4: TAC Generado ({end_tac:.2f}ms)")

            # FASE 5. LLVM IR GENERATOR
            start_ir = time.time()
            
            # Determinar target triple
            target_triple = None
            if self.target_os == "windows":
                target_triple = "x86_64-pc-windows-gnu"
            elif self.target_os == "linux":
                target_triple = "x86_64-pc-linux-gnu"
                
            irgen = IRGeneratorV4(target_triple=target_triple)
            irgen.visit(tree)
            llvm_ir = irgen.get_ir()
            end_ir = (time.time() - start_ir) * 1000

            with open("salida.ll", "w", encoding="utf-8") as f:
                f.write(llvm_ir)
            print(f"✔ Fase 5: LLVM IR Generado ({end_ir:.2f}ms)")

            # FASE 6. INTÉRPRETE / EJECUTOR
            print(f"\n✔ Fase 6: Ejecución Intérprete:")
            start_exe = time.time()
            interpreter = InterpreterVisitorV4()
            interpreter.visit(tree)
            end_exe = (time.time() - start_exe) * 1000
            print(f"  [Tiempo de intérprete: {end_exe:.2f}ms]\n")

            # FASE 7. OPTIMIZER O3
            start_opt = time.time()
            opt = Optimizer()
            llvm_opt_ir, metrics = opt.optimize_o3(llvm_ir)
            end_opt = (time.time() - start_opt) * 1000
            
            with open("salida.opt.ll", "w", encoding="utf-8") as f:
                f.write(llvm_opt_ir)
                
            print(f"✔ Fase 7: Optimización O3 ({end_opt:.2f}ms)")
            print(f"  Instrucciones originales: {metrics['pre_count']}")
            print(f"  Instrucciones optimizadas: {metrics['post_count']}")
            print(f"  Reducción: {metrics['reduction_percent']}%")

            # FASE 8. GENERACIÓN BINARIO NATIVO
            if self.target_os in ["linux", "windows", "ambos"]:
                start_bin = time.time()
                bin_gen = BinaryGenerator()
                
                if self.target_os in ["linux", "ambos"]:
                    ok, out_path, t, msg = bin_gen.compile_to_linux("salida.opt.ll", "salida_linux.bin")
                    if ok:
                        print(f"✔ Fase 8: Binario Linux generado: {out_path} ({t:.2f}ms)")
                    else:
                        print(f"[!] Error generando Linux bin: {msg}")
                        
                if self.target_os in ["windows", "ambos"]:
                    ok, out_path, t, msg = bin_gen.compile_to_windows("salida.opt.ll", "salida_windows.exe")
                    if ok:
                        print(f"✔ Fase 8: Binario Windows generado: {out_path} ({t:.2f}ms)")
                    else:
                        print(f"[!] Error generando Windows bin: {msg}")
                
            return True

        except Exception as e:
            print(f"\n[X] Error crítico en Pipeline: {e}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 pipeline_v4.py archivo.src [linux|windows|ambos]")
    else:
        target = sys.argv[2] if len(sys.argv) > 2 else None
        app = PipelineV4(sys.argv[1], target_os=target)
        app.run()
