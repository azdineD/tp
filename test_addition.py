import unittest
from addition import addition

class TestAddition(unittest.TestCase):
    def test_addition_positive(self):
        self.assertEqual(addition(2, 3), 5)

    def test_addition_negative(self):
        self.assertEqual(addition(-2, -3), -5)

    def test_addition_mixed(self):
        self.assertEqual(addition(-2, 3), 1)

    def test_addition_zero(self):
        self.assertEqual(addition(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
