import unittest
from my_math import expo, hypotonuse, is_prime, sum_of_digits

#Kevin test:

class test_prime(unittest.TestCase):
    def test_one(self):
        self.assertFalse(is_prime(1))  

    def test_zero(self):
        self.assertFalse(is_prime(0))  

    def test_negative(self):
        self.assertFalse(is_prime(-4))

    def test_prime(self):
        self.assertTrue(is_prime(7))

    def test_positive(self):
        self.assertFalse(is_prime(10))



class test_sum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(456), 15)
        self.assertEqual(sum_of_digits(789), 24)

    







#Amadou test:








if __name__ == "__main__":
    unittest.main()