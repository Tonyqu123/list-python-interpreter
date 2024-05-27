## errors.py

class LispError(Exception):
    """Base class for all Lisp-related errors."""
    def __init__(self, msg: str):
        super().__init__(msg)
        self.msg = msg

class SyntaxError(LispError):
    """Raised when there is a syntax error in the Lisp code."""
    def __init__(self, msg: str = "Syntax Error"):
        super().__init__(msg)

class NameError(LispError):
    """Raised when a variable is not found in the environment."""
    def __init__(self, msg: str = "Name Error"):
        super().__init__(msg)

class ArityError(LispError):
    """Raised when a function is called with an incorrect number of arguments."""
    def __init__(self, msg: str = "Arity Error"):
        super().__init__(msg)
