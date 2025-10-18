# ================================================
# step2_syntax_analyzer.py
# Syntax Analyzer for mini compiler
# Supports: variable declarations, assignments, print, if-else, while
# ================================================

class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type=None, expected_value=None):
        token = self.current_token()
        if token is None:
            raise Exception(f"❌ Syntax Error: Unexpected end of input, expected {expected_type}")
        if expected_type and token[0] != expected_type:
            raise Exception(f"❌ Syntax Error: Expected {expected_type}, got {token}")
        if expected_value and token[1] != expected_value:
            raise Exception(f"❌ Syntax Error: Expected '{expected_value}', got {token}")
        self.pos += 1
        return token

    def parse(self):
        while self.current_token() is not None:
            self.statement()

    def statement(self):
        token = self.current_token()

        # -------------------- Variable Declaration --------------------
        if token[0] == "KEYWORD" and token[1] in ["int", "float", "string", "char", "bool"]:
            self.consume("KEYWORD")
            self.consume("IDENTIFIER")
            if self.current_token() and self.current_token()[1] == "=":
                self.consume("OP")
                self.expression()
            self.consume("SEMICOLON")

        # -------------------- Assignment --------------------
        elif token[0] == "IDENTIFIER":
            self.consume("IDENTIFIER")
            self.consume("OP", "=")
            self.expression()
            self.consume("SEMICOLON")

        # -------------------- Print Statement --------------------
        elif token[0] == "KEYWORD" and token[1] == "print":
            self.consume("KEYWORD")

            # Allow both print x; and print(x);
            if self.current_token() and self.current_token()[0] == "LPAREN":
                self.consume("LPAREN")
                self.expression()
                self.consume("RPAREN")
            else:
                self.expression()

            self.consume("SEMICOLON")

        # -------------------- If-Else Statement --------------------
        elif token[0] == "KEYWORD" and token[1] == "if":
            self.consume("KEYWORD")
            self.consume("LPAREN")
            self.expression()
            self.consume("RPAREN")
            self.consume("LBRACE")
            while self.current_token() and self.current_token()[0] != "RBRACE":
                self.statement()
            self.consume("RBRACE")

            if self.current_token() and self.current_token()[1] == "else":
                self.consume("KEYWORD")
                self.consume("LBRACE")
                while self.current_token() and self.current_token()[0] != "RBRACE":
                    self.statement()
                self.consume("RBRACE")

        # -------------------- While Loop --------------------
        elif token[0] == "KEYWORD" and token[1] == "while":
            self.consume("KEYWORD")
            self.consume("LPAREN")
            self.expression()
            self.consume("RPAREN")
            self.consume("LBRACE")
            while self.current_token() and self.current_token()[0] != "RBRACE":
                self.statement()
            self.consume("RBRACE")

        else:
            raise Exception(f"❌ Syntax Error: Unexpected token {token}")

    # -------------------- Expression Parser --------------------
    def expression(self):
        token = self.current_token()

        if token[0] in ["NUMBER", "IDENTIFIER", "STRING", "CHAR", "KEYWORD"]:
            self.consume(token[0])
        elif token[0] == "LPAREN":  # handle parentheses in expressions like (a + b)
            self.consume("LPAREN")
            self.expression()
            self.consume("RPAREN")
        else:
            raise Exception(f"❌ Syntax Error: Expected operand, got {token}")

        while self.current_token() and self.current_token()[0] == "OP":
            self.consume("OP")
            next_token = self.current_token()
            if next_token[0] not in ["NUMBER", "IDENTIFIER", "STRING", "CHAR", "KEYWORD", "LPAREN"]:
                raise Exception(f"❌ Syntax Error: Expected operand, got {next_token}")
            self.expression()
