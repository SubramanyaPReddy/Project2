import unittest
from FCalculator import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(4, self.calc.add(-3, 7), "The addition is wrong")

    def test_subtract(self):
        self.assertEqual(-3, self.calc.subtract(0, 3), "Subtraction is wrong")

    def test_multiply(self):
        self.assertEqual(-30, self.calc.multiply(-5, 6), "Multiplication is wrong")

    def test_divide(self):
        with self.assertRaises(ValueError):
            self.calc.divide(6, 0)

if __name__ == '__main__':
    unittest.main()
