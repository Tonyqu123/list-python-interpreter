## test_main.py

import unittest
from unittest.mock import patch, MagicMock
import sys

## Import the main function from the main module
sys.path.append('/data/lisp_interpreter')
from main import main

## TestMain
class TestMain(unittest.TestCase):
    """
    Test cases for the main function in main.py.
    """

    ## test_main_function
    def test_main_function(self):
        """
        Test the main function to ensure it initializes and starts the REPL correctly.
        """
        with patch('repl.REPL') as MockREPL:
            mock_repl_instance = MockREPL.return_value
            mock_repl_instance.start = MagicMock()

            main()

            ## Check if REPL instance was created
            MockREPL.assert_called_once()

            ## Check if start method was called on the REPL instance
            mock_repl_instance.start.assert_called_once()

## Run the tests
if __name__ == '__main__':
    unittest.main()
