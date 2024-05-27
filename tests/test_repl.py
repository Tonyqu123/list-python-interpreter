"""
## test_repl.py

import unittest
from unittest.mock import patch
from io import StringIO
from repl import REPL
from errors import LispError, SyntaxError, NameError, ArityError

class TestREPL(unittest.TestCase):
    """Unit tests for the REPL class of the Lisp interpreter."""

    def setUp(self):
        """Set up the REPL instance for testing."""
        self.repl = REPL()

    @patch('builtins.input', side_effect=['(+ 1 2)', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_repl_addition(self, mock_stdout, mock_input):
        """Test REPL with a simple addition expression."""
        self.repl.start()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn('3', output)

    @patch('builtins.input', side_effect=['(unknown-func)', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_repl_unknown_function(self, mock_stdout, mock_input):
        """Test REPL with an unknown function to trigger NameError."""
        self.repl.start()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn('Error: Unknown function: unknown-func', output)

    @patch('builtins.input', side_effect=['(+ 1)', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_repl_arity_error(self, mock_stdout, mock_input):
        """Test REPL with incorrect number of arguments to trigger ArityError."""
        self.repl.start()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn('Error: Incorrect number of arguments', output)

    @patch('builtins.input', side_effect=['(1 2)', 'exit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_repl_syntax_error(self, mock_stdout, mock_input):
        """Test REPL with a syntax error to trigger SyntaxError."""
        self.repl.start()
        output = mock_stdout.getvalue().strip().split('\n')
        self.assertIn('Error: Invalid syntax', output)

if __name__ == '__main__':
    unittest.main()
"""
