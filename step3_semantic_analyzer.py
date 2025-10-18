class SemanticAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.symbol_table = {}

    def analyze(self):
        i = 0
        while i < len(self.tokens):
            token = self.tokens[i]
            if token[0] == 'KEYWORD' and token[1] in ('int', 'float'):
                var = self.tokens[i+1][1]
                if var in self.symbol_table:
                    raise Exception(f"❌ Semantic Error: Variable '{var}' already declared")
                self.symbol_table[var] = token[1]
            i += 1
        return self.symbol_table
