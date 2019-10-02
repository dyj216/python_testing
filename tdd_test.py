import unittest
from tdd_calculator import Calculator


# Run continuously this test:
# Install inotify-tools
# while inotifywait -e close_write .; do python -m unittest tdd_test.py; done


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(15, self.calculator.add(7, 8))
