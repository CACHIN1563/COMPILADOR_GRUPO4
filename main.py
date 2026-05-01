import sys
from antlr4 import *
from GramaticaLexer import GramaticaLexer
from GramaticaParser import GramaticaParser
from Evaluador import Evaluador

# =================================================================
# UNIVERSIDAD MARIANO GÁLVEZ DE GUATEMALA
# FACULTAD DE INGENIERÍA EN SISTEMAS DE INFORMACIÓN
# CURSO: COMPILADORES
# PROYECTO FINAL: INTÉRPRETE DE LENGUAJE G4 - GRUPO NO. 4
# =================================================================

def mostrar_encabezado_g4():
    """
    Imprime la identificación del grupo y la universidad en la terminal.
    Personalizado para el Grupo 4.
    """
    print("="*70)
    print("        UNIVERSIDAD MARIANO GÁLVEZ DE GUATEMALA")
    print("           INGENIERÍA EN SISTEMAS - GRUPO 4")
    print("="*70)
    print(">> Intérprete de Lenguaje de Alto Nivel G4")
    print(">> Estado: Cargando entorno de ejecución...")
    print("-" * 70)


def ejecutar_analisis():
    mostrar_encabezado_g4()
    # Permitir pasar el archivo por argumento, por defecto usa input.txt
    import sys
    archivo_entrada = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    
    try:
        # 1. Carga del flujo de entrada desde archivo
        input_stream = FileStream(archivo_entrada, encoding='utf-8')
        
        from custom_errors import CustomErrorListener
        error_listener = CustomErrorListener()

        # 2. Análisis Léxico (Tokenización)
        lexer = GramaticaLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)
        
        token_stream = CommonTokenStream(lexer)
        
        # 3. Análisis Sintáctico (Construcción del AST)
        parser = GramaticaParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        
        tree = parser.program()
        
        # 4. Verificación de errores
        if error_listener.has_errors():
            print(f"\n[!] Se detectaron errores (Fase 2 - Manejo de Errores) en '{archivo_entrada}':")
            error_listener.print_errors()
            print("-" * 70)
            return

        # 5. Ejecución del Programa mediante el Visitor (Evaluador)
        print(f"\n[GRUPO 4] Iniciando ejecución de: {archivo_entrada}")
        print("-" * 70)
        
        evaluador_instancia = Evaluador()
        evaluador_instancia.visit(tree)
        
        print("-" * 70)
        print(">> Programa finalizado exitosamente.")
        print("="*70)

    except FileNotFoundError:
        print(f"\n[!] ERROR: No se localizó el archivo fuente '{archivo_entrada}'.")
    except Exception as e:
        print(f"\n[!] ERROR CRÍTICO DURANTE LA EJECUCIÓN: {e}")

if __name__ == "__main__":
    ejecutar_analisis()