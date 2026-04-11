from abc import ABC, abstractmethod
from project.components.memory import Memory

class Expression(ABC): 
    """Abstract base class for all boolean expressions."""
    @abstractmethod
    def evaluate(self) -> bool:
        pass

    @abstractmethod
    def to_prefix(self) -> str:
        pass

class BoolValue(Expression):
    """Handles absolute truth values (t or f)."""
    def __init__(self, value: bool):
        self.value = value

    def evaluate(self) -> bool:
        return self.value

    def to_prefix(self) -> str:
        return "t" if self.value else "f"

class BoolOp(Expression):
    """Handles logical operations (∧ or ∨)."""
    def __init__(self, op: str, left: Expression, right: Expression):
        self.op = op # '∧' or '∨'
        self.left = left
        self.right = right

    def evaluate(self) -> bool:
        # Evaluate left and right children
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        
        # Apply logic
        if self.op == '∧':
            return left_val and right_val
        elif self.op == '∨':
            return left_val or right_val
        else:
            raise ValueError(f"Unsupported operator: {self.op}")

    def to_prefix(self) -> str:
        # Prefix notation
        return f"{self.op} {self.left.to_prefix()} {self.right.to_prefix()}"
    
class VarFetch(Expression):
    """Retrieves a variable from Memory"""
    def __init__(self, name: str):
        self.name = name
        self.memory = Memory()

    def evaluate(self) -> bool:
        # get() returns a dict, we want the "value" key
        return self.memory.get(self.name)["value"]

    def to_prefix(self) -> str:
        return self.name

class VarAssign(Expression):
    """Assigns an expression to a variable in Memory"""
    def __init__(self, name: str, expr: Expression):
        self.name = name
        self.expr = expr
        self.memory = Memory()

    def evaluate(self) -> bool:
        # Evaluate the right side of the equals sign
        val = self.expr.evaluate()
        # Store in memory. We use type(val).__name__ for a clean string like 'bool'
        self.memory.set(self.name, val, type(val).__name__)
        return val

    def to_prefix(self) -> str:
        return f"= {self.name} {self.expr.to_prefix()}"