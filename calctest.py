import unittest
import calc


class calctest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(5, calc.calculate("3+2"))
        self.assertEqual(13, calc.calculate("10+3"))
        self.assertEqual(13, calc.calculate("10 + 3"))
        self.assertEqual(13, calc.calculate(" 10 + 3"))
        self.assertEqual(13, calc.calculate("10 + 3    "))

    def test_subtraction(self):
        self.assertEqual(2, calc.calculate("5 - 3"))


class calcinternaltest(unittest.TestCase):
    def test_getoperator(self):
        self.assertEqual('+', calc.parse_operator("3+2"))
        self.assertEqual('-', calc.parse_operator("3-2"))
        self.assertEqual('-', calc.parse_operator("3 - 2"))
        self.assertEqual('*', calc.parse_operator("3 * 2"))

    def test_parse(self):
        self.assertTupleEqual((3, '*', 2), calc.parse("3*2"))
        self.assertTupleEqual((3, '*', 2), calc.parse("3* 2"))


class calcplugintest(unittest.TestCase):
    def test_addOp(self):
        calc.add_op_new('#', lambda x, y: x*y)
        self.assertEqual(6, calc.calculate("3 # 2"))
