# https://github.com/BlackDeer-cyber/Lab11-CD-EK
# Partner 1: Christopher Deer
# Partner 2: Elijah Kelford

import unittest
# from calculator import *
import calculator  #


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertEqual(calculator.div(5, 25), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_subtract(self):
        self.assertEqual(calculator.sub(10, 4), 6)
        self.assertEqual(calculator.sub(3, 7), -4)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)

    def test_logarithm(self):
        self.assertEqual(calculator.log(10, 100), 2.0)
        self.assertEqual(calculator.log(2, 8), 3.0)

    def test_log_invalid_base(self):
        # with self.assertRaises(ValueError):
        #     calculator.log(1, 10)

        with self.assertRaises(ValueError):
            calculator.log(0, 10)

        with self.assertRaises(ValueError):
            calculator.log(-2, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):
        # with self.assertRaises(ValueError):
        #     calculator.logarithm(1, 10)

        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)

        # with self.assertRaises(ValueError):
        #     calculator.logarithm(2, -10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)

        with self.assertRaises(ValueError):
            calculator.square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
