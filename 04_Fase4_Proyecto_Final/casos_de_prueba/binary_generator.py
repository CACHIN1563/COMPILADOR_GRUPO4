import subprocess
import os
import time

class BinaryGenerator:
    def __init__(self):
        pass

    def compile_to_linux(self, ir_file_path, output_bin="salida.bin"):
        """Llama a clang por detrás para sacar un binario normalito de Linux"""
        start_time = time.time()
        try:
            cmd = ["clang", ir_file_path, "-o", output_bin]
            result = subprocess.run(cmd, capture_output=True, text=True)
            elapsed = (time.time() - start_time) * 1000 # ms
            
            if result.returncode == 0:
                return True, output_bin, elapsed, "Compilación Linux exitosa."
            else:
                return False, None, elapsed, f"Error en clang (Linux): {result.stderr}"
        except FileNotFoundError:
            return False, None, 0, "Herramienta 'clang' no encontrada. Instala con: sudo apt install clang"

    def compile_to_windows(self, ir_file_path, output_exe="salida.exe"):
        """Hace la magia negra de compilar a .exe desde WSL (cross-compiling)"""
        start_time = time.time()
        try:
            # Le pasamos el target de windows para que clang sepa qué hacer
            cmd = ["clang", "-target", "x86_64-pc-windows-gnu", ir_file_path, "-o", output_exe]
            result = subprocess.run(cmd, capture_output=True, text=True)
            elapsed = (time.time() - start_time) * 1000 # ms
            
            if result.returncode == 0:
                return True, output_exe, elapsed, "Compilación Windows (.exe) exitosa."
            else:
                return False, None, elapsed, f"Error en clang cruzado (Windows): {result.stderr}"
        except FileNotFoundError:
            return False, None, 0, "Herramienta 'clang' no encontrada. Instala clang y mingw-w64."

    def execute_linux_binary(self, bin_path):
        """Corre el binario de Linux y nos devuelve lo que printea"""
        try:
            if not bin_path.startswith("./") and not bin_path.startswith("/"):
                bin_path = "./" + bin_path
            result = subprocess.run([bin_path], capture_output=True, text=True)
            return True, result.stdout + result.stderr
        except Exception as e:
            return False, str(e)
