import unittest
import rpn

class TestBasics(unittest.TestCase): 
    def test_add(self): 
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exponent(self):
        result = rpn.calculate("2 4 ^")
        self.assertEqual(16, result)
    def test_copy(self):
        result = rpn.calculate("4 c +")
        self.assertEqual(8, result)
    def test_mod(self):
        result = rpn.calculate("4 3 %")
        self.assertEqual(1, result)
    def test_intdiv(self):
        result = rpn.calculate("4 3 //")
        self.assertEqual(1, result)
    def test_factorial(self):
        result = rpn.calculate("4 !")
        self.assertEqual(24, result)
    def test_bitwiseAnd(self):
        result = rpn.calculate("0 3 &")
        self.assertEqual(0, result)
    def test_bitwiseOr(self):
        result = rpn.calculate("0 3 |")
        self.assertEqual(3, result)
    def test_bitwiseNot(self): 
        result = rpn.calculate("0 ~")
        self.assertEqual(-1, result)
    def test_divZero(self):
        result = rpn.calculate("4 0 / 4 1 /")
        self.assertEqual(4, result)
