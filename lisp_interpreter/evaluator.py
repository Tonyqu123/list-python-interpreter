## evaluator.py

from environment import Environment
from errors import LispError, NameError, ArityError

class Evaluator:
    """Class to evaluate the abstract syntax tree (AST) according to Lisp semantics."""

    def evaluate(self, ast: any, env: Environment) -> any:
        """Evaluate the given AST in the context of the provided environment."""
        if isinstance(ast, int):
            return ast
        elif isinstance(ast, str):
            return env.lookup(ast)
        elif isinstance(ast, list):
            if not ast:
                raise LispError("Cannot evaluate an empty list")
            func = self.evaluate(ast[0], env)
            args = [self.evaluate(arg, env) for arg in ast[1:]]
            return self.apply(func, args)
        else:
            raise LispError(f"Unknown AST node type: {type(ast)}")

    def apply(self, func: any, args: list) -> any:
        """Apply a function to the given arguments."""
        if callable(func):
            return func(*args)
        else:
            raise LispError(f"Attempt to call a non-function: {func}")

# Example built-in functions
def add(*args):
    if len(args) < 2:
        raise ArityError("add function requires at least two arguments")
    return sum(args)

def subtract(*args):
    if len(args) < 2:
        raise ArityError("subtract function requires at least two arguments")
    result = args[0]
    for arg in args[1:]:
        result -= arg
    return result

def multiply(*args):
    if len(args) < 2:
        raise ArityError("multiply function requires at least two arguments")
    result = 1
    for arg in args:
        result *= arg
    return result

def divide(*args):
    if len(args) < 2:
        raise ArityError("divide function requires at least two arguments")
    result = args[0]
    for arg in args[1:]:
        if arg == 0:
            raise LispError("Division by zero")
        result /= arg
    return result

# Initialize the global environment with built-in functions
def create_global_env() -> Environment:
    env = Environment()
    env.define('+', add)
    env.define('-', subtract)
    env.define('*', multiply)
    env.define('/', divide)
    return env
