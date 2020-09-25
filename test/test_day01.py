import unittest
import day01


class Part1(unittest.TestCase):
    def test_get_frequency(self):
        self.assertEqual(day01.get_frequency([+1, +1, +1]), 3)
        self.assertEqual(day01.get_frequency([+1, +1, -2]), 0)
        self.assertEqual(day01.get_frequency([-1, -2, -3]), -6)


class Part2(unittest.TestCase):
    def test_get_dejavu(self):
        self.assertEqual(day01.get_dejavu([+1, -1]), 0)
        self.assertEqual(day01.get_dejavu([+3, +3, +4, -2, -4]), 10)
        self.assertEqual(day01.get_dejavu([-6, +3, +8, +5, -6]), 5)
        self.assertEqual(day01.get_dejavu([+7, +7, -2, -7, -4]), 14)
