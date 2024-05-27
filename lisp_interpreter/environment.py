## environment.py

class Environment:
    """Class to handle variable scopes and bindings in the Lisp interpreter."""

    def __init__(self, parent: 'Environment' = None):
        """Initialize the environment with an optional parent environment."""
        self.parent = parent
        self.variables = {}

    def define(self, var: str, value: any) -> None:
        """Define a new variable in the current environment."""
        self.variables[var] = value

    def lookup(self, var: str) -> any:
        """Look up a variable in the current environment and its parents."""
        if var in self.variables:
            return self.variables[var]
        elif self.parent is not None:
            return self.parent.lookup(var)
        else:
            raise NameError(f"Variable '{var}' not found")

    def set(self, var: str, value: any) -> None:
        """Set the value of an existing variable in the current environment or its parents."""
        if var in self.variables:
            self.variables[var] = value
        elif self.parent is not None:
            self.parent.set(var, value)
        else:
            raise NameError(f"Variable '{var}' not found")
