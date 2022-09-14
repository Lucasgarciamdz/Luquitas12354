#create test for the factorial function
import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(11), 39916800)
        self.assertEqual(factorial(12), 479001600)
        self.assertEqual(factorial(13), 6227020800)
        self.assertEqual(factorial(14), 87178291200)
        self.assertEqual(factorial(15), 1307674368000)
        


if __name__ == '__main__':
    unittest.main()