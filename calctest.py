import unittest
import calc


def define_basic_op():
    calc.define_operator('+', lambda x, y: x+y)
    calc.define_operator('-', lambda x, y: x-y)
    calc.define_operator('*', lambda x, y: x*y)
    calc.define_operator('/', lambda x, y: x/y)


class calctest(unittest.TestCase):
    define_basic_op()

    def test_addition(self):
        self.assertEqual(5, calc.main("3+2"))
        self.assertEqual(13, calc.main("10+3"))
        self.assertEqual(13, calc.main("10 + 3"))
        self.assertEqual(13, calc.main(" 10 + 3"))
        self.assertEqual(13, calc.main("10 + 3    "))

    def test_subtraction(self):
        self.assertEqual(2, calc.main("5 - 3"))

    def test_unknown_operator_error(self):
        self.assertRaises(Exception, calc.main, "3}2")

    def test_new_calc(self):
        self.assertEqual(5, calc.calculate(2, "+", 3))
        
    def test_uselastoutput(self):
        calc.main("3+2")
        self.assertEqual(8, calc.main("+3"))
        
    def test_getlastresult(self):
        calc.main("2+7")
        self.assertEqual(9, calc.lastResult)


class calcinternaltest(unittest.TestCase):
    def test_getoperator(self):
        define_basic_op()
        self.assertEqual('+', calc.parse_operator("3+2"))
        self.assertEqual('-', calc.parse_operator("3-2"))
        self.assertEqual('-', calc.parse_operator("3 - 2"))
        self.assertEqual('*', calc.parse_operator("3 * 2"))

    def test_parse(self):
        self.assertTupleEqual((3, '*', 2), calc.parse("3*2"))
        self.assertTupleEqual((3, '*', 2), calc.parse("3* 2"))

    def test_parse_number(self):
        self.assertEqual(2, calc.parse_number("2"))
        self.assertRaises(Exception, calc.parse_number, "b")
        self.assertEqual(2, calc.parse_number(" 2"))


class calcplugintest(unittest.TestCase):
    def test_addOp(self):
        calc.define_operator('#', lambda x, y: x*y)
        self.assertEqual(6, calc.main("3 # 2"))



class basicCalcTest(unittest.TestCase):
    def test_basicAddition(self):
        self.assertEqual(5, calc.main_loop("2+3"))
        