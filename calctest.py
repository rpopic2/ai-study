import unittest
import calc


class calctest(unittest.TestCase):
    def testaddition(self):
        self.assertEqual(5, calc.calculate("3+2"))
        self.assertEqual(13, calc.calculate("10+3"))
        self.assertEqual(13, calc.calculate("10 + 3"))

    def testparseexpr(self):
        self.assertEqual('+', calc.get_expr("3+2"))
        self.assertEqual('-', calc.get_expr("3-2"))
        self.assertEqual('-', calc.get_expr("3 - 2"))
        self.assertEqual('-', calc.get_expr("3-2="))
