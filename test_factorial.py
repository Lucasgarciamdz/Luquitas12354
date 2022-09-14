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
        self.assertEqual(factorial(16), 20922789888000)
        self.assertEqual(factorial(17), 355687428096000)
        self.assertEqual(factorial(18), 6402373705728000)
        self.assertEqual(factorial(19), 121645100408832000)
        self.assertEqual(factorial(20), 2432902008176640000)
        self.assertEqual(factorial(21), 51090942171709440000)
        self.assertEqual(factorial(22), 1124000727777607680000)
        self.assertEqual(factorial(23), 25852016738884976640000)
        self.assertEqual(factorial(24), 620448401733239439360000)
        self.assertEqual(factorial(25), 15511210043330985984000000)
        self.assertEqual(factorial(26), 403291461126605635584000000)
        self.assertEqual(factorial(27), 10888869450418352160768000000)
        self.assertEqual(factorial(28), 304888344611713860501504000000)
        self.assertEqual(factorial(29), 8841761993739701954543616000000)
        self.assertEqual(factorial(30), 265252859812191058636308480000000)
        


if __name__ == '__main__':
    unittest.main()