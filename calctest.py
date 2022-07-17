import unittest
import calc


class calctest(unittest.TestCase):
    def test_addition(self):
        calc.define_operator('+', lambda x, y: x+y)
        self.assertEqual(5, calc.calculate("3+2"))
        self.assertEqual(13, calc.calculate("10+3"))
        self.assertEqual(13, calc.calculate("10 + 3"))
        self.assertEqual(13, calc.calculate(" 10 + 3"))
        self.assertEqual(13, calc.calculate("10 + 3    "))

    def test_subtraction(self):
        calc.define_operator('-', lambda x, y: x-y)
        self.assertEqual(2, calc.calculate("5 - 3"))

    def test_unknown_operator_error(self):
        self.assertEqual(None, calc.calculate("3}2"))

    def test_non_numeric_error(self):
        calc.define_operator('-', lambda x,y: x-y)
        self.assertEqual(None, calc.calculate("a-2"))
        self.assertEqual(2, calc.calculate("2-a"))


class calcinternaltest(unittest.TestCase):
    def test_getoperator(self):
        self.assertEqual('+', calc.parse_operator("3+2"))
        self.assertEqual('-', calc.parse_operator("3-2"))
        self.assertEqual('-', calc.parse_operator("3 - 2"))
        self.assertEqual('*', calc.parse_operator("3 * 2"))

    def test_parse(self):
        self.assertTupleEqual((3, '*', 2), calc.parse("3*2"))
        self.assertTupleEqual((3, '*', 2), calc.parse("3* 2"))

    def test_parse_number(self):
        self.assertEqual(2, calc.parse_number("2"))
        self.assertEqual(0, calc.parse_number("b"))
        self.assertEqual(2, calc.parse_number(" 2"))


class calcplugintest(unittest.TestCase):
    def test_addOp(self):
        calc.define_operator('#', lambda x, y: x*y)
        self.assertEqual(6, calc.calculate("3 # 2"))
