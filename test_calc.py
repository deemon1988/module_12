import calc
import unittest

class CalcTest(unittest.TestCase):
    def setUp(self):
        print("setup")
        # self.a = 2
        # self.b = 1

    def test_add(self):
        # result = self.a + self.b
        # self.assertEqual(result,3)
        self.assertEqual(calc.add(2,1),3)
        """
        Test for add function in calculator
        :return:
        """
    def test_sub(self):
        self.assertEqual(calc.sub(3, 1), 2)

    def test_div(self):
        self.assertEqual(calc.div(4, 2), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(2, 2), 4)

if __name__ == '__main__':
    unittest.main()