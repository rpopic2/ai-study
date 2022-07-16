import unittest
import calc


class calctest(unittest.TestCase):
    def testaddition(self):
        self.assertEqual(5, calc.calculate("3+2"))
        self.assertEqual(3, calc.calculate("1+2"))
        self.assertEqual(13, calc.calculate("10+3"))
