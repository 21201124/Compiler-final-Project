# ================================================
# step3_semantic_analyzer.py
# Builds a Symbol Table with all types
# ================================================

class Symbol:
    def __init__(self, name, type_, value=None, scope="global"):
        self.name = name
        self.type = type_
        self.value = value
        self.scope = scope

    def __repr__(self):
        return f"{self.name:<10} | {self.type:<10} | {str(self.value):<10} | {self.scope}"

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, type_, value=None, scope="global"):
        if name in self.symbols:
            print(f"⚠️ Warning: Redeclaration of variable '{name}'.")
        self.symbols[name] = Symbol(name, type_, value, scope)

    def update(self, name, value):
        if name not in self.symbols:
            print(f"❌ Error: Undeclared variable '{name}' used.")
        else:
            self.symbols[name].value = value

    def lookup(self, name):
        return self.symbols.get(name, None)

class SemanticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.table = SymbolTable()
        self.supported_types = ["int", "float", "string", "char", "bool"]

    def analyze(self):
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]

            # Variable declaration
            if token[0] == "KEYWORD" and token[1] in self.supported_types:
                var_type = token[1]
                if i+1 < len(self.tokens) and self.tokens[i+1][0] == "IDENTIFIER":
                    var_name = self.tokens[i+1][1]
                    var_value = None

                    # Initialization
                    if i+3 < len(self.tokens) and self.tokens[i+2][1] == "=":
                        init_token = self.tokens[i+3]
                        if var_type == "int" and init_token[0] == "NUMBER":
                            var_value = int(init_token[1])
                        elif var_type == "float" and init_token[0] == "NUMBER":
                            var_value = float(init_token[1])
                        elif var_type == "string" and init_token[0] == "STRING":
                            var_value = init_token[1][1:-1]  # remove quotes
                        elif var_type == "char" and init_token[0] == "CHAR":
                            var_value = init_token[1][1:-1]
                        elif var_type == "bool" and init_token[0] == "KEYWORD" and init_token[1] in ["true","false"]:
                            var_value = True if init_token[1]=="true" else False
                        i += 3
                    self.table.insert(var_name, var_type, var_value)

            # Assignment
            elif token[0] == "IDENTIFIER" and i+1 < len(self.tokens) and self.tokens[i+1][1] == "=":
                var_name = token[1]
                if i+2 < len(self.tokens):
                    val_token = self.tokens[i+2]
                    value = None
                    if val_token[0] == "NUMBER":
                        value = int(val_token[1])
                    elif val_token[0] == "STRING":
                        value = val_token[1][1:-1]
                    elif val_token[0] == "CHAR":
                        value = val_token[1][1:-1]
                    elif val_token[0] == "KEYWORD" and val_token[1] in ["true","false"]:
                        value = True if val_token[1]=="true" else False
                    self.table.update(var_name, value)
            i += 1

        # Return dictionary for main.py
        return {name: vars(sym) for name, sym in self.table.symbols.items()}
