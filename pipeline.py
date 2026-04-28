import sys
from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from custom_errors import CustomErrorListener
from semantic_visitor import SemanticVisitor
from interpreter_visitor import InterpreterVisitor

class Pipeline:
    """
    Orquestador principal del Compilador Grupo 4.
    Integra las 4 fases: Léxico, Sintáctico, Semántico e Intérprete.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.error_listener = CustomErrorListener()

    def run(self):
        try:
            # 1. FASE LÉXICA
            input_stream = FileStream(self.file_path, encoding='utf-8')
            lexer = GramaticaLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(self.error_listener)
            
            # 2. FASE SINTÁCTICA
            token_stream = CommonTokenStream(lexer)
            parser = GramaticaParser(token_stream)
            parser.removeErrorListeners()
            parser.addErrorListener(self.error_listener)
            
            tree = parser.program()
            
            # Verificación de errores Léxicos/Sintácticos
            if self.error_listener.has_errors():
                print("\n[!] DETENIDO: Se encontraron errores estructurales:")
                self.error_listener.print_errors()
                return

            # 3. FASE SEMÁNTICA (Validación de tipos y ámbitos)
            print("\n>>> Iniciando Análisis Semántico...")
            semantic = SemanticVisitor()
            semantic.visit(tree)
            
            if len(semantic.errores) > 0:
                print("\n[!] DETENIDO: Se encontraron errores semánticos:")
                for err in semantic.errores:
                    print(err)
                return
            
            print(">>> Análisis Semántico exitoso. Sin errores.")

            # 4. FASE DE EJECUCIÓN (Intérprete)
            print("\n>>> Iniciando Ejecución...\n" + "="*30)
            interpreter = InterpreterVisitor()
            interpreter.visit(tree)
            print("="*30 + "\n>>> Ejecución finalizada con éxito.")

        except Exception as e:
            print(f"\n[X] Error Crítico del Sistema: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 pipeline.py <archivo_fuente>")
    else:
        app = Pipeline(sys.argv[1])
        app.run()
