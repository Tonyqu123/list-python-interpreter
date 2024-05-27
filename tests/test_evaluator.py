"""
Unit tests for evaluator.py

This module contains unit tests for the Evaluator class and built-in functions for a Lisp interpreter.
"""

import unittest
from evaluator import Evaluator, create_global_env
from environment import Environment
from errors import LispError, NameError, ArityError

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.env = create_global_env()
        self.evaluator = Evaluator()

    def test_evaluate_integer(self):
        self.assertEqual(self.evaluator.evaluate(42, self.env), 42)

    def test_evaluate_variable(self):
        self.env.define('x', 10)
        self.assertEqual(self.evaluator.evaluate('x', self.env), 10)

    def test_evaluate_addition(self):
        ast = ['+', 1, 2]
        self.assertEqual(self.evaluator.evaluate(ast, self.env), 3)

    def test_evaluate_subtraction(self):
        ast = ['-', 5, 3]
        self.assertEqual(self.evaluator.evaluate(ast, self.env), 2)

    def test_evaluate_multiplication(self):
        ast = ['*', 2, 3]
        self.assertEqual(self.evaluator.evaluate(ast, self.env), 6)

    def test_evaluate_division(self):
        ast = ['/', 6, 2]
        self.assertEqual(self.evaluator.evaluate(ast, self.env), 3)

    def test_evaluate_division_by_zero(self):
        ast = ['/', 6, 0]
        with self.assertRaises(LispError):
            self.evaluator.evaluate(ast, self.env)

    def test_evaluate_empty_list(self):
        ast = []
        with self.assertRaises(LispError):
            self.evaluator.evaluate(ast, self.env)

    def test_evaluate_unknown_ast_node(self):
        ast = {'key': 'value'}
        with self.assertRaises(LispError):
            self.evaluator.evaluate(ast, self.env)

    def test_add_function_arity_error(self):
        with self.assertRaises(ArityError):
            self.evaluator.evaluate(['+', 1], self.env)

    def test_subtract_function_arity_error(self):
        with self.assertRaises(ArityError):
            self.evaluator.evaluate(['-', 1], self.env)

    def test_multiply_function_arity_error(self):
        with self.assertRaises(ArityError):
            self.evaluator.evaluate(['*', 1], self.env)

    def test_divide_function_arity_error(self):
        with self.assertRaises(ArityError):
            self.evaluator.evaluate(['/', 1], self.env)

if __name__ == '__main__':
    unittest.main()
