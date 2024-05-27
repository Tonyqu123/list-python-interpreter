"""
## test_environment.py

Unit tests for the Environment class in environment.py.
"""

import unittest
from environment import Environment

class TestEnvironment(unittest.TestCase):
    def setUp(self):
        """Set up a new environment for each test."""
        self.env = Environment()

    def test_define_and_lookup(self):
        """Test defining and looking up variables."""
        self.env.define('x', 42)
        self.assertEqual(self.env.lookup('x'), 42)

    def test_lookup_nonexistent_variable(self):
        """Test looking up a variable that does not exist."""
        with self.assertRaises(NameError):
            self.env.lookup('y')

    def test_set_existing_variable(self):
        """Test setting the value of an existing variable."""
        self.env.define('x', 42)
        self.env.set('x', 100)
        self.assertEqual(self.env.lookup('x'), 100)

    def test_set_nonexistent_variable(self):
        """Test setting the value of a variable that does not exist."""
        with self.assertRaises(NameError):
            self.env.set('y', 100)

    def test_lookup_in_parent_environment(self):
        """Test looking up a variable in the parent environment."""
        parent_env = Environment()
        parent_env.define('x', 42)
        child_env = Environment(parent=parent_env)
        self.assertEqual(child_env.lookup('x'), 42)

    def test_set_in_parent_environment(self):
        """Test setting the value of a variable in the parent environment."""
        parent_env = Environment()
        parent_env.define('x', 42)
        child_env = Environment(parent=parent_env)
        child_env.set('x', 100)
        self.assertEqual(parent_env.lookup('x'), 100)

if __name__ == '__main__':
    unittest.main()
