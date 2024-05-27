## repl.py

from parser import Parser
from evaluator import Evaluator
from environment import create_global_env
from errors import LispError, SyntaxError, NameError, ArityError

class REPL:
    """Class to handle the Read-Eval-Print Loop (REPL) for the Lisp interpreter."""

    def __init__(self):
        """Initialize the REPL with a parser, evaluator, and global environment."""
        self.parser = Parser()
        self.evaluator = Evaluator()
        self.global_env = create_global_env()

    def start(self) -> None:
        """Start the REPL loop for interactive execution."""
        print("Welcome to the Lisp REPL. Type 'exit' to quit.")
        while True:
            try:
                # Display prompt and read input
                code = input("lisp> ")
                if code.strip().lower() == 'exit':
                    break

                # Parse the input code into an AST
                ast = self.parser.parse(code)

                # Evaluate the AST in the global environment
                result = self.evaluator.evaluate(ast, self.global_env)

                # Print the result
                print(result)

            except (SyntaxError, NameError, ArityError, LispError) as e:
                # Handle and display errors
                print(f"Error: {e.msg}")

if __name__ == "__main__":
    repl = REPL()
    repl.start()
