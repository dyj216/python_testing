import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_square_root(self):
        for (number, root) in [(4, 2), (9, 3), (16, 4)]:
            with self.subTest(fn_input=number, expected=root):
                self.assertEqual(root, self.calculator.square_root(number))
