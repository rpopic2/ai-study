import unittest
import calc


class calctest(unittest.TestCase):
    def testaddition(self):
        self.assertEqual(5, calc.calcualte("3+2"))
        self.assertEqual(3, calc.calcualte("1+2"))