import unittest
from StepHorse import Stephorse

class TestStephorse(unittest.TestCase):
    def test_horsestop(self):
        self.assertEqual(Stephorse(1,1,1,4), 'Stop')

    def test_horsestep(self):
        self.assertEqual(Stephorse(2,4,3,2), 'Step')

    def test_minus(self):
        self.assertRaises(ValueError, Stephorse, -1, -5, -8, -5)
    def test_type(self):
        self.assertRaises(TypeError, Stephorse, 'a', 'a', 'a', 'a')
        self.assertRaises(TypeError, Stephorse, 1-2j, 1-2j, 1-2j, 1-2j )
    def test_value(self):
        self.assertRaises(ValueError, Stephorse, 9, 10, 11, 13)
    def test_zero_value(self):
        self.assertRaises(ValueError, Stephorse, 0, 0, 0, 0)
    def test_zero_value(self):
        self.assertRaises(TypeError, Stephorse, 1.5, 2.4, 5.9, 4.2)