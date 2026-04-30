import os
import sys
from pipeline_v3 import PipelineV3

# Colores ANSI para una terminal "enriquecida"
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(f"{Colors.HEADER}{Colors.BOLD}")
    print("====================================================")
    print("      COMPILADOR INTERACTIVO - GRUPO 4 (v3)         ")
    print("====================================================")
    print(f"{Colors.ENDC}")

def menu():
    while True:
        clear_screen()
        print_header()
        print(f"{Colors.OKCYAN}1. {Colors.BOLD}Escribir / Analizar Código Fuente{Colors.ENDC}")
        print(f"{Colors.OKCYAN}2. {Colors.BOLD}Ver Código Intermedio (TAC){Colors.ENDC}")
        print(f"{Colors.OKCYAN}3. {Colors.BOLD}Ver Módulo LLVM IR (.ll){Colors.ENDC}")
        print(f"{Colors.OKCYAN}4. {Colors.BOLD}Ejecutar Pruebas Predefinidas{Colors.ENDC}")
        print(f"{Colors.FAIL}5. Salir{Colors.ENDC}")

        opcion = input(f"\n{Colors.BOLD}Seleccione una opción: {Colors.ENDC}")

        if opcion == "1":
            print(f"\n{Colors.WARNING}--- Modo de Entrada de Código ---{Colors.ENDC}")
            print("Escriba su código (Escriba 'END' en una línea sola para terminar):")
            
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            
            source_code = "\n".join(lines)
            
            with open("temp_input.src", "w", encoding="utf-8") as f:
                f.write(source_code)
            
            print(f"\n{Colors.OKBLUE}>>> Iniciando Pipeline de Compilación...{Colors.ENDC}")
            p = PipelineV3("temp_input.src")
            p.run()
            input(f"\n{Colors.BOLD}Presione Enter para continuar...{Colors.ENDC}")

        elif opcion == "2":
            try:
                if not os.path.exists("salida.tac"):
                    print(f"\n{Colors.FAIL}[!] No se ha generado TAC aún.{Colors.ENDC}")
                else:
                    with open("salida.tac", "r", encoding="utf-8") as f:
                        print(f"\n{Colors.OKGREEN}--- CÓDIGO DE TRES DIRECCIONES (TAC) ---{Colors.ENDC}")
                        print(f.read())
            except Exception as e:
                print(f"Error: {e}")
            input(f"\n{Colors.BOLD}Presione Enter para continuar...{Colors.ENDC}")

        elif opcion == "3":
            try:
                if not os.path.exists("salida.ll"):
                    print(f"\n{Colors.FAIL}[!] No se ha generado LLVM IR aún.{Colors.ENDC}")
                else:
                    with open("salida.ll", "r", encoding="utf-8") as f:
                        print(f"\n{Colors.OKGREEN}--- LLVM INTERMEDIATE REPRESENTATION ---{Colors.ENDC}")
                        print(f.read())
            except Exception as e:
                print(f"Error: {e}")
            input(f"\n{Colors.BOLD}Presione Enter para continuar...{Colors.ENDC}")

        elif opcion == "4":
            print("\nArchivos disponibles:")
            archivos = [f for f in os.listdir(".") if f.endswith(".txt") or f.endswith(".src")]
            for i, f in enumerate(archivos):
                print(f"{i+1}. {f}")
            
            idx = input("\nSeleccione número de archivo: ")
            try:
                archivo = archivos[int(idx)-1]
                p = PipelineV3(archivo)
                p.run()
            except:
                print("Selección inválida")
            input(f"\n{Colors.BOLD}Presione Enter para continuar...{Colors.ENDC}")

        elif opcion == "5":
            print(f"\n{Colors.OKBLUE}Saliendo del compilador... ¡Hasta pronto!{Colors.ENDC}\n")
            break
        else:
            print(f"\n{Colors.FAIL}Opción no reconocida.{Colors.ENDC}")
            time.sleep(1)

if __name__ == "__main__":
    import time
    menu()