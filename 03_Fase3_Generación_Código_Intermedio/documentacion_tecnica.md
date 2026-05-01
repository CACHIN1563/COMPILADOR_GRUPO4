# Documentación Técnica: Fase 3 - Generación de Código Intermedio y Estructuras Extendidas

Esta sección detalla los componentes técnicos implementados en la Fase 3 del compilador del **Grupo 4**. La arquitectura se ha evolucionado para soportar estructuras de datos complejas y una organización modular del código.

---

## 1. Gramática Evolucionada (`Gramatica_v3.g4`)
La gramática representa el corazón sintáctico del lenguaje. En esta versión 3, se han expandido las capacidades del lenguaje para alinearse con estándares modernos de programación.

### Innovaciones Técnicas:
*   **Soporte de Arreglos (Arrays):** Se implementaron reglas para la declaración e inicialización de arreglos unidimensionales mediante la sintaxis `INT[] id = [v1, v2, v3];`. Esto requirió la creación de nodos específicos en el AST para gestionar literales de lista.
*   **Manejo de Cadenas (Strings):** Mejora en el lexer para el tratamiento de secuencias de escape y concatenación dinámica de caracteres.
*   **Modularización:** Inclusión de reglas para la organización de instrucciones en bloques lógicos más complejos, permitiendo una mejor estructuración del programa principal.
*   **Tipado Explícito Robusto:** Reforzamiento de las reglas de tipo (`INT`, `FLOAT`, `STRING`, `BOOL`, `VOID`) para asegurar que cada declaración cumpla con las restricciones semánticas desde la fase de parsing.

---

## 2. Analizador Semántico v3 (`semantic_visitor_v3.py`)
El analizador semántico actúa como el "juez de coherencia" del compilador. Utilizando el patrón de diseño **Visitor**, recorre el árbol sintáctico (AST) validando la lógica del programa.

### Funciones Clave:
*   **Validación de Arreglos:** Verifica que todos los elementos dentro de un literal de arreglo coincidan con el tipo declarado (ej. que no haya un `string` dentro de un arreglo de `INT`).
*   **Verificación de Ámbitos (Scopes):** Gestiona la visibilidad de las variables en bloques anidados, asegurando que las variables locales no colisionen con las globales y se liberen correctamente al salir de su contexto.
*   **Chequeo de Tipos en Expresiones:** Controla la compatibilidad en operaciones aritméticas y lógicas, manejando la promoción de tipos (como permitir un `INT` en una operación que espera `FLOAT`).

---

## 3. Intérprete de Ejecución v3 (`interpreter_visitor_v3.py`)
Este componente es el motor de ejecución que procesa el AST una vez que ha sido validado semánticamente.

### Detalles de Implementación:
*   **Gestión de Memoria Dinámica:** Utiliza una **Tabla de Símbolos** avanzada para almacenar y recuperar valores de variables y arreglos en tiempo de ejecución.
*   **Ejecución de Funciones:** Implementa una pila de llamadas para gestionar parámetros y valores de retorno, permitiendo la ejecución de subrutinas definidas por el usuario.
*   **Salida Estándar:** Procesa la instrucción `IMPRIMIR` para mostrar resultados en consola, convirtiendo tipos internos del lenguaje a representaciones legibles.

---

## 4. Orquestador del Sistema (`pipeline_v3.py`)
El Pipeline es el script principal que coordina el flujo de datos entre todas las fases del compilador. Su importancia radica en la **integración y el manejo de errores**.

### Flujo de Trabajo:
1.  **Carga de Fuente:** Lee el archivo con extensión personalizada (`.src` o `.txt`).
2.  **Análisis Léxico/Sintáctico:** Invoca a ANTLR para generar el AST.
3.  **Filtro de Errores Estructurales:** Si la gramática no se cumple, detiene el proceso y reporta línea y columna del error.
4.  **Análisis Semántico:** Valida la lógica. Si hay errores (ej. variable no declarada), interrumpe el flujo.
5.  **Generación/Ejecución:** Finalmente, procede a la ejecución del código o la generación de código intermedio.

---

## 5. Archivos de Soporte ANTLR (`Lexer`, `Parser`, `Tokens`)
Para garantizar la portabilidad del proyecto, se han incluido los archivos generados automáticamente. Estos transforman la gramática declarativa en código Python ejecutable, permitiendo que el sistema sea agnóstico a la instalación local de herramientas Java en la máquina de destino (como la del ingeniero evaluador).
