import os
import sys
import time
from pipeline_v4 import PipelineV4
from ir_manual import IRManualOptimizer

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
    print("  COMPILADOR INTERACTIVO - PROYECTO FINAL (v4)      ")
    print("====================================================")
    print(f"{Colors.ENDC}")

def menu_manual_ir():
    if not os.path.exists("salida.ll"):
        print(f"\n{Colors.FAIL}[!] No se ha generado LLVM IR aún. Ejecuta una compilación primero.{Colors.ENDC}")
        input(f"\n{Colors.BOLD}Presione Enter para regresar...{Colors.ENDC}")
        return
        
    with open("salida.ll", "r") as f:
        ir_original = f.read()

    opt_manual = IRManualOptimizer()
    available = opt_manual.get_available_passes()
    selected_passes = []

    while True:
        clear_screen()
        print(f"{Colors.HEADER}--- MÓDULO DE OPTIMIZACIÓN MANUAL IR ---{Colors.ENDC}")
        print(f"Pases seleccionados actualmente: {Colors.OKGREEN}{selected_passes}{Colors.ENDC}\n")
        
        for i, p in enumerate(available):
            prefix = "[x]" if p in selected_passes else "[ ]"
            print(f"{Colors.OKCYAN}{i+1}. {prefix} {p}{Colors.ENDC}")
            
        print(f"{Colors.WARNING}A. Aplicar pases y ver diff{Colors.ENDC}")
        print(f"{Colors.FAIL}R. Regresar al menú principal{Colors.ENDC}")
        
        opcion = input(f"\n{Colors.BOLD}Seleccione un pase para alternar o una acción: {Colors.ENDC}").strip().lower()
        
        if opcion == 'r':
            break
        elif opcion == 'a':
            print(f"\n{Colors.OKBLUE}Aplicando pases seleccionados...{Colors.ENDC}")
            opt_ir, diff, ok, msg = opt_manual.apply_manual_passes(ir_original, selected_passes)
            if not ok:
                print(f"{Colors.FAIL}{msg}{Colors.ENDC}")
            else:
                print(f"\n{Colors.OKGREEN}--- COMPARADOR DIFF ---{Colors.ENDC}")
                if diff.strip():
                    for line in diff.split("\n"):
                        if line.startswith("+"): print(f"{Colors.OKGREEN}{line}{Colors.ENDC}")
                        elif line.startswith("-"): print(f"{Colors.FAIL}{line}{Colors.ENDC}")
                        elif line.startswith("@"): print(f"{Colors.OKCYAN}{line}{Colors.ENDC}")
                        else: print(line)
                else:
                    print("No hubo cambios en el IR tras aplicar los pases.")
                    
                # Guardar resultado
                with open("salida_manual.ll", "w") as f:
                    f.write(opt_ir)
                print(f"\n{Colors.WARNING}IR optimizado guardado en salida_manual.ll{Colors.ENDC}")
                
                resp = input(f"\n¿Desea re-ejecutar el programa con este IR optimizado para comprobar que la salida no cambió? (s/n): ").strip().lower()
                if resp == 's':
                    print(f"\n{Colors.OKBLUE}Re-ejecutando IR con lli (Intérprete nativo LLVM)...{Colors.ENDC}")
                    import subprocess
                    try:
                        res = subprocess.run(["lli", "salida_manual.ll"], capture_output=True, text=True)
                        print(f"{Colors.OKGREEN}--- SALIDA DE LA EJECUCIÓN (Debe ser idéntica) ---{Colors.ENDC}")
                        print(res.stdout)
                        if res.stderr:
                            print(f"{Colors.FAIL}Errores durante ejecución: {res.stderr}{Colors.ENDC}")
                    except FileNotFoundError:
                        print(f"{Colors.FAIL}No se encontró la herramienta 'lli'. Instala llvm en WSL.{Colors.ENDC}")
                
            input(f"\n{Colors.BOLD}Presione Enter para continuar...{Colors.ENDC}")
        else:
            try:
                idx = int(opcion) - 1
                if 0 <= idx < len(available):
                    p = available[idx]
                    if p in selected_passes:
                        selected_passes.remove(p)
                    else:
                        selected_passes.append(p)
            except:
                pass

def menu():
    while True:
        clear_screen()
        print_header()
        print(f"{Colors.OKCYAN}1. {Colors.BOLD}Compilar archivo .src (End-to-End Pipeline v4){Colors.ENDC}")
        print(f"{Colors.OKCYAN}2. {Colors.BOLD}Optimización Manual de IR (IR Manual Panel){Colors.ENDC}")
        print(f"{Colors.OKCYAN}3. {Colors.BOLD}Ver Código Intermedio (TAC){Colors.ENDC}")
        print(f"{Colors.FAIL}4. Salir{Colors.ENDC}")

        opcion = input(f"\n{Colors.BOLD}Seleccione una opción: {Colors.ENDC}")

        if opcion == "1":
            print("\nArchivos .src disponibles en el directorio:")
            archivos = [f for f in os.listdir(".") if f.endswith(".src") or f.endswith(".txt")]
            if not archivos:
                print(f"{Colors.FAIL}No se encontraron archivos .src{Colors.ENDC}")
                input(f"\n{Colors.BOLD}Presione Enter para continuar...{Colors.ENDC}")
                continue
                
            for i, f in enumerate(archivos):
                print(f"{i+1}. {f}")
            
            idx = input("\nSeleccione número de archivo: ")
            
            print("\nSeleccione plataforma de binario destino:")
            print("1. Linux nativo")
            print("2. Windows (.exe)")
            print("3. Ambos")
            print("4. Ninguno (Solo hasta Fase 7)")
            plat_op = input("Opción: ")
            
            target = None
            if plat_op == "1": target = "linux"
            elif plat_op == "2": target = "windows"
            elif plat_op == "3": target = "ambos"
            
            try:
                archivo = archivos[int(idx)-1]
                print(f"\n{Colors.OKBLUE}>>> Iniciando Pipeline V4 para {archivo}...{Colors.ENDC}")
                p = PipelineV4(archivo, target_os=target)
                p.run()
            except Exception as e:
                print(f"Selección inválida o error: {e}")
            input(f"\n{Colors.BOLD}Presione Enter para continuar...{Colors.ENDC}")

        elif opcion == "2":
            menu_manual_ir()

        elif opcion == "3":
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

        elif opcion == "4":
            print(f"\n{Colors.OKBLUE}Saliendo del compilador... ¡Éxitos en tu entrega!{Colors.ENDC}\n")
            break
        else:
            print(f"\n{Colors.FAIL}Opción no reconocida.{Colors.ENDC}")
            time.sleep(1)

if __name__ == "__main__":
    menu()
