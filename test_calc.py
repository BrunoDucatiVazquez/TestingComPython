import unittest
import calc
# to run test use python test_file.py
class TestCalc(unittest.TestCase):
    
    def test_add1(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)
    
    def test_add2(self):
        testadd1 = calc.add(45,5)
        self.assertEqual(testadd1, 50)

    def test_multiply(self):
        testMultiply1 = calc.multiply(5,5)
        self.assertEqual(testMultiply1, 25)

    def test_subtract(self):
        testSubtract1 = calc.subtract(10,5)
        self.assertEqual(testSubtract1, 5)


if __name__ == '__main__':
    unittest.main()