import llvmlite.binding as llvm

class Optimizer:
    def __init__(self):
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        
    def count_instructions(self, ir_str):
        count = 0
        for line in ir_str.split("\n"):
            line = line.strip()
            # Forma rápida de contar cuántas líneas de código nos quedaron:
            # ignorar llaves, espacios o labels para que cuadre el conteo
            if line and not line.startswith(";") and not line.endswith(":") and not line.startswith("}") and "=" in line or line.startswith("call") or line.startswith("store") or line.startswith("ret") or line.startswith("br") or line.startswith("switch"):
                count += 1
        return count

    def optimize_o3(self, ir_module_str):
        # 1. Leer el código que generamos antes
        module = llvm.parse_assembly(ir_module_str)
        module.verify()
        
        # 2. Ver cuántas líneas teníamos antes de optimizar
        pre_count = self.count_instructions(str(module))
        
        # 3. Preparamos el optimizador en nivel 3 (O3 para máxima eficiencia)
        pmb = llvm.create_pass_manager_builder()
        pmb.opt_level = 3
        
        # 4. Armamos el manager de pases
        mpm = llvm.create_module_pass_manager()
        pmb.populate(mpm)
        
        # 5. Corremos el optimizador sobre el código
        mpm.run(module)
        
        # 6. Sacamos el nuevo código y contamos cuántas líneas sobrevivieron
        opt_ir_str = str(module)
        post_count = self.count_instructions(opt_ir_str)
        
        # 7. Hacemos las mates para ver cuánto mejoró (porcentaje)
        if pre_count > 0:
            reduction = ((pre_count - post_count) / pre_count) * 100
        else:
            reduction = 0.0
            
        metrics = {
            "pre_count": pre_count,
            "post_count": post_count,
            "reduction_percent": round(reduction, 2),
            "passes_applied": "O3 (incluye Constant Propagation, DCE, Function Inlining, Loop Unrolling)"
        }
        
        return opt_ir_str, metrics
