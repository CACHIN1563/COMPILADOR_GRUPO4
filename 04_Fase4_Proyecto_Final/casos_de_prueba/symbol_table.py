# =================================================================
# GESTIÓN DE MEMORIA - TABLA DE SÍMBOLOS (GRUPO 4)
# =================================================================
# Esta clase controla los ámbitos (scopes) usando una pila de diccionarios.
# Cada vez que entramos a un {} hacemos un push_scope.

class SymbolTable:
    def __init__(self):
        # La pila_ambitos es nuestro 'stack of hash tables'.
        # El índice 0 siempre será el GLOBAL.
        self.pila_ambitos = [{}]

    def push_scope(self):
        """Abre un nuevo nivel de visibilidad (Scope)."""
        self.pila_ambitos.append({})

    def pop_scope(self):
        """Cierra el nivel actual al salir de un bloque o función."""
        if len(self.pila_ambitos) > 1:
            self.pila_ambitos.pop()
        else:
            # Esto no debería pasar si el parser está bien.
            raise Exception("Error crítico: Intentando eliminar el ámbito global.")

    def declare(self, nombre, tipo_dato, valor=None, es_funcion=False, parametros=None):
        """Declara una nueva entrada en el ámbito más interno."""
        if nombre in self.pila_ambitos[-1]:
            # El enunciado dice: error si hay redeclaración en el mismo ambito.
            return False, f"La variable '{nombre}' ya existe en este bloque."
        
        # Guardamos todo en un diccionario dentro de la tabla hash actual
        self.pila_ambitos[-1][nombre] = {
            'type': tipo_dato,
            'value': valor,
            'is_func': es_funcion,
            'params': parametros # Lista de (tipo, nombre) para funciones
        }
        return True, None

    def lookup(self, nombre):
        """Busca de adentro hacia afuera (Shadowing)."""
        for ambito in reversed(self.pila_ambitos):
            if nombre in ambito:
                return ambito[nombre]
        return None

    def update_value(self, nombre, nuevo_valor):
        """Actualiza el valor de una variable existente."""
        for ambito in reversed(self.pila_ambitos):
            if nombre in ambito:
                if ambito[nombre]['is_func']:
                    return False, f"Ojo: '{nombre}' es una función, no puedes asignarle valores."
                ambito[nombre]['value'] = nuevo_valor
                return True, None
        return False, f"Error: La variable '{nombre}' no ha sido declarada."

    def is_in_current_scope(self, nombre):
        """Chequeo rápido para ver si está en el nivel actual."""
        return nombre in self.pila_ambitos[-1]

    def __str__(self):
        return f"Estado de Memoria (Grupo 4): {str(self.pila_ambitos)}"
