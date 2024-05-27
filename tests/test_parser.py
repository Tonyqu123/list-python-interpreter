## test_parser.py

import unittest
from parser import Parser, lexer, parser

## TestParser
class TestParser(unittest.TestCase):
    """Unit tests for the Parser class and its methods."""

    ## setUp
    def setUp(self):
        """Set up the test environment."""
        self.parser = Parser()

    ## test_parse_number
    def test_parse_number(self):
        """Test parsing a single number."""
        result = self.parser.parse("42")
        self.assertEqual(result, 42)

    ## test_parse_symbol
    def test_parse_symbol(self):
        """Test parsing a single symbol."""
        result = self.parser.parse("foo")
        self.assertEqual(result, "foo")

    ## test_parse_empty_list
    def test_parse_empty_list(self):
        """Test parsing an empty list."""
        result = self.parser.parse("()")
        self.assertEqual(result, [])

    ## test_parse_nonempty_list
    def test_parse_nonempty_list(self):
        """Test parsing a non-empty list."""
        result = self.parser.parse("(42 foo)")
        self.assertEqual(result, [42, "foo"])

    ## test_parse_nested_list
    def test_parse_nested_list(self):
        """Test parsing a nested list."""
        result = self.parser.parse("(42 (foo 7))")
        self.assertEqual(result, [42, ["foo", 7]])

    ## test_parse_invalid_character
    def test_parse_invalid_character(self):
        """Test parsing an invalid character."""
        with self.assertRaises(SyntaxError):
            self.parser.parse("42 @")

    ## test_parse_syntax_error
    def test_parse_syntax_error(self):
        """Test parsing a syntax error."""
        with self.assertRaises(SyntaxError):
            self.parser.parse("(42 foo")

    ## test_lexer_number
    def test_lexer_number(self):
        """Test lexer for a single number."""
        lexer.input("42")
        token = lexer.token()
        self.assertEqual(token.type, 'NUMBER')
        self.assertEqual(token.value, 42)

    ## test_lexer_symbol
    def test_lexer_symbol(self):
        """Test lexer for a single symbol."""
        lexer.input("foo")
        token = lexer.token()
        self.assertEqual(token.type, 'SYMBOL')
        self.assertEqual(token.value, "foo")

    ## test_lexer_parens
    def test_lexer_parens(self):
        """Test lexer for parentheses."""
        lexer.input("()")
        token = lexer.token()
        self.assertEqual(token.type, 'LPAREN')
        token = lexer.token()
        self.assertEqual(token.type, 'RPAREN')

    ## test_lexer_ignore_whitespace
    def test_lexer_ignore_whitespace(self):
        """Test lexer ignores whitespace."""
        lexer.input("  \t\n42")
        token = lexer.token()
        self.assertEqual(token.type, 'NUMBER')
        self.assertEqual(token.value, 42)

    ## test_lexer_illegal_character
    def test_lexer_illegal_character(self):
        """Test lexer raises error on illegal character."""
        lexer.input("@")
        with self.assertRaises(SyntaxError):
            lexer.token()

## main
if __name__ == '__main__':
    unittest.main()
