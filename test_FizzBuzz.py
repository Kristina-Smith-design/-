import unittest
from FizzBuzz import FizzBuzz

class TestNumMultiple(unittest.TestCase):
    def test_multipleFiz(self):
        self.assertEqual(FizzBuzz(3), 'Fiz')
        

    def test_multipleBuz(self):
        self.assertEqual(FizzBuzz(50), 'Buz')

    def test_multipleFizBuz(self):
        self.assertEqual(FizzBuzz(45), 'FizBuz')
        self.assertEqual(FizzBuzz(15), 'FizBuz')

    def test_multipleNum(self):
        self.assertEqual(FizzBuzz(1), 1)

    def test_type(self):
    	self.assertRaises(TypeError, FizzBuzz, 'aaa')
    	self.assertRaises(TypeError, FizzBuzz, 1-2j)

    def test_zero_value(self):
    	self.assertEqual(FizzBuzz(0), 0)