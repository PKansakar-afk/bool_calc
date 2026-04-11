from sly import Parser
from project.components.lexica import MyLexer
from project.components.ast.statement import BoolValue, BoolOp, VarFetch, VarAssign

class ASTParser(Parser):
    debugfile = 'parser.out'
    start = 'statement'
    tokens = MyLexer.tokens
    
    # Precedence rules: Bottom of the list has the highest priority.
    # Therefore, AND has higher priority than OR.
    precedence = (
        ('left', OR),
        ('left', AND),
    )

    @_('NAME ASSIGN expr')
    def statement(self, p) -> tuple:
        # Create an assignment node, evaluate it (which saves it to memory), and return
        assign_node = VarAssign(p.NAME, p.expr)
        return assign_node.evaluate(), assign_node.to_prefix()

    @_('expr')
    def statement(self, p) -> tuple:
        # The parser returns a tuple: (Evaluated Boolean, Prefix String)
        return p.expr.evaluate(), p.expr.to_prefix()

    @_('expr AND expr')
    def expr(self, p):
        return BoolOp('∧', p.expr0, p.expr1)

    @_('expr OR expr')
    def expr(self, p):
        return BoolOp('∨', p.expr0, p.expr1)

    @_('LPAREN expr RPAREN')
    def expr(self, p):
        return p.expr

    @_('TRUE')
    def expr(self, p):
        return BoolValue(True)

    @_('FALSE')
    def expr(self, p):
        return BoolValue(False)
    
    @_('NAME')
    def expr(self, p):
        # If we see a variable name in an expression, fetch it
        return VarFetch(p.NAME)

if __name__ == "__main__":
    lexer = MyLexer()
    parser = ASTParser()
    text = "t ∨ f ∧ f"
    
    # Should evaluate as t ∨ (f ∧ f) -> t ∨ f -> True
    # Prefix should be: ∨ t ∧ f f
    result_val, result_prefix = parser.parse(lexer.tokenize(text))
    
    print(f"Result: {'t' if result_val else 'f'}")
    print(f"Prefix: {result_prefix}")