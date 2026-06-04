import subprocess
import difflib
import tempfile
import os

class IRManualOptimizer:
    def __init__(self):
        self.available_passes = [
            "mem2reg",
            "instcombine",
            "simplifycfg",
            "dce",
            "inline",
            "loop-unroll"
        ]

    def get_available_passes(self):
        return self.available_passes

    def apply_manual_passes(self, ir_str, passes):
        """
        Llama al comando 'opt' de la compu para pasarle nuestros propios filtros al código
        """
        if not passes:
            return ir_str, "No se seleccionaron pases.", True, "OK"
            
        # Alistamos el comando que vamos a mandar a la terminal
        opt_args = ["opt", "-S"]
        for p in passes:
            if p in self.available_passes:
                opt_args.append(f"-passes={p}")
                
        # Creamos unos archivitos fantasma temporales para que 'opt' pueda leer y escribir
        fd_in, path_in = tempfile.mkstemp(suffix=".ll")
        fd_out, path_out = tempfile.mkstemp(suffix=".ll")
        
        try:
            with os.fdopen(fd_in, 'w') as f:
                f.write(ir_str)
                
            # Acá ejecutamos la herramienta desde Python
            cmd = opt_args + [path_in, "-o", path_out]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                return ir_str, "", False, f"Error al ejecutar opt: {result.stderr}"
                
            with open(path_out, 'r') as f:
                opt_ir_str = f.read()
                
            # Sacamos el antes y el después para mostrarlo en pantalla
            diff = self.generate_diff(ir_str, opt_ir_str)
            
            return opt_ir_str, diff, True, "Pases aplicados exitosamente"
            
        except FileNotFoundError:
            return ir_str, "", False, "Herramienta 'opt' de LLVM no encontrada. Instala llvm en WSL: sudo apt install llvm"
        finally:
            if os.path.exists(path_in): os.remove(path_in)
            if os.path.exists(path_out): os.remove(path_out)
            
    def generate_diff(self, original, modified):
        orig_lines = original.splitlines()
        mod_lines = modified.splitlines()
        
        diff = difflib.unified_diff(
            orig_lines, 
            mod_lines, 
            fromfile='IR Original', 
            tofile='IR Optimizado (Manual)', 
            lineterm=''
        )
        return '\n'.join(list(diff))
