import re

def lexer(code):
    token_patterns = [
        ('KEYWORD', r'\b(int|float|if|else|while|print)\b'),
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),
        ('NUMBER', r'\d+(\.\d+)?'),
        ('OPERATOR', r'[+\-*/=<>!]'),
        ('SEPARATOR', r'[(){};,]'),
        ('WHITESPACE', r'\s+'),
    ]
    tokens = []
    while code:
        match = None
        for token_type, pattern in token_patterns:
            regex = re.match(pattern, code)
            if regex:
                match = regex.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, match))
                code = code[len(match):]
                break
        if not match:
            raise Exception(f"❌ Lexical Error near '{code[0]}'")
    return tokens
