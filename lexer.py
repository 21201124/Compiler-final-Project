# ===============================================
# step1_lexer.py
# Lexical Analyzer for mini compiler
# Supports: int, float, string, char, bool, identifiers, operators
# ===============================================

import re

KEYWORDS = ["int", "float", "string", "char", "bool", "if", "else", "while", "print", "true", "false"]

def lexer(source_code):
    tokens = []

    # Token specification: order matters
    token_specification = [
        ('NUMBER',    r'\d+(\.\d+)?'),  # int or float
        ('IDENTIFIER',r'[A-Za-z_]\w*'),
        ('STRING',    r'"[^"]*"'),
        ('CHAR',      r"'[^']'"),
        ('OP',        r'\+\+|--|==|!=|<=|>=|&&|\|\||[+\-*/=<>]'),
        ('SEMICOLON', r';'),
        ('LPAREN',    r'\('),
        ('RPAREN',    r'\)'),
        ('LBRACE',    r'\{'),
        ('RBRACE',    r'\}'),
        ('SKIP',      r'[ \t\n]+'),
        ('MISMATCH',  r'.'),
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    for mo in re.finditer(tok_regex, source_code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP':
            continue
        elif kind == 'IDENTIFIER' and value in KEYWORDS:
            kind = 'KEYWORD'
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Lexical Error near {value}')
        tokens.append((kind, value))
    return tokens
