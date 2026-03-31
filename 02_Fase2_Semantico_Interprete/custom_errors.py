from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Determine if it's a Lexical or Syntactic error based on the message or offendingSymbol
        error_type = "Sintáctico"
        if "token recognition error at" in msg or offendingSymbol is None:
            error_type = "Léxico"
        
        formatted_error = f"* {error_type}: [Error {error_type}] Línea {line}, Columna {column}: {msg}"
        self.errors.append(formatted_error)

    def has_errors(self):
        return len(self.errors) > 0

    def print_errors(self):
        for error in self.errors:
            print(error)
