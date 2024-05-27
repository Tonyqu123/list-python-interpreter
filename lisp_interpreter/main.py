## main.py

from repl import REPL

def main() -> None:
    """Main function to start the Lisp REPL."""
    repl = REPL()
    repl.start()

if __name__ == "__main__":
    main()
