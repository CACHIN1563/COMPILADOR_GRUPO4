import os
from pipeline_v3 import PipelineV3

def menu():
    while True:
        print("\n=============== MENU COMPILADOR ================")
        print("1. Analizar archivo")
        print("2. Ver TAC")
        print("3. Ver LLVM IR")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n*************** Ejecutando análisis ****************")

            archivo = input("Ingrese ruta del archivo: ")
            if not os.path.exists(archivo):
                print("Archivo no encontrado")
            else:
                p = PipelineV3(archivo)
                p.run()

        elif opcion == "2":
            try:
                with open("salida.tac", "r") as f:
                    print("\n*************** Mostrando TAC ****************")
                    print("\n------ TAC ------")
                    print(f.read())
            except:
                print("\n******************* ESPERA *********************")
                print("Primero ejecuta análisis")

        elif opcion == "3":
            try:
                with open("salida.ll", "r") as f:
                    print("\n*************** Mostrando LLVM IR ****************")
                    print("\n------ LLVM IR ------")
                    print(f.read())
            except:
                print("\n******************* ESPERA *********************")
                print("Primero ejecuta análisis")

        elif opcion == "4":
            print("\nSaliendo...\n")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()