## parser.py

import ply.lex as lex
import ply.yacc as yacc

# Token definitions for the lexer
tokens = (
    'NUMBER', 'SYMBOL', 'LPAREN', 'RPAREN'
)

# Token regex patterns
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SYMBOL = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    raise SyntaxError(f"Illegal character '{t.value[0]}'")

# Build the lexer
lexer = lex.lex()

# Parsing rules
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_symbol(p):
    'expression : SYMBOL'
    p[0] = p[1]

def p_expression_list(p):
    'expression : LPAREN list RPAREN'
    p[0] = p[2]

def p_list_empty(p):
    'list :'
    p[0] = []

def p_list_nonempty(p):
    'list : expression list'
    p[0] = [p[1]] + p[2]

def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at '{p.value}'")
    else:
        raise SyntaxError("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

class Parser:
    """Class to parse Lisp code into an abstract syntax tree (AST)."""

    def parse(self, code: str):
        """Parse the given Lisp code and return the AST."""
        return parser.parse(code)

