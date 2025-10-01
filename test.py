import unittest
from main import two_sum

class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example2(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_example3(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_example4(self):
        self.assertEqual(two_sum([8, 9, 3, 6, 1, 0], 14), [0, 3])

    def test_example5(self):
        self.assertEqual(two_sum([1, 9, 7, 19, 0], 19), [3, 4])

    def test_example6(self):
        self.assertEqual(two_sum([20, 12, 32, 40, 11], 43), [2, 4])

unittest.main(argv=[''], verbosity=2, exit=False)