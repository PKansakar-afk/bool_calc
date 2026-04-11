from sly import Lexer

class MyLexer(Lexer):
    """
    Lexer for Propositional Logic.
    Tokens: t (true), f (false), ∧ (AND), ∨ (OR), =, names, and parentheses.
    x = t ∨ f -> NAME('x'), ASSIGN('='), TRUE('t'), OR('∨'), FALSE('f').
    """
    
    tokens = { 'TRUE', 'FALSE', 'AND', 'OR', 'LPAREN', 'RPAREN', 'NAME', 'ASSIGN' }
    ignore = ' \t'

    AND    = r'\∧'
    OR     = r'∨'
    ASSIGN = r'='
    LPAREN = r'\('
    RPAREN = r'\)'

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

    NAME['t'] = 'TRUE'
    NAME['f'] = 'FALSE'

    # Increases newline count
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Shows error for illegal character
    def error(self, t):
        print(f"ERROR: Illegal character '{t.value[0]}' at line {self.lineno}")
        self.index += 1

if __name__ == '__main__':
    string_input:str = "t ∨ f ∧ f"
    lex:Lexer = MyLexer()
    for token in lex.tokenize(string_input):
        print(token)