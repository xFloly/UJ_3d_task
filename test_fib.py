import unittest
from fib import fib

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_correct(self):
        self.assertEqual(fib(5), 5)

    # def test_fibonacci_incorrect(self):
    #     self.assertEqual(fib(5), 10)