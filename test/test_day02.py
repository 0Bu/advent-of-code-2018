import unittest
import day02


class Part1(unittest.TestCase):
    ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

    def test_get_variance(self):
        self.assertDictEqual(day02.get_variance(self.ids[0]), dict.fromkeys(set(self.ids[0]), 1))
        self.assertDictEqual(day02.get_variance(self.ids[1]), {"a": 2, "b": 3, "c": 1})
        self.assertDictEqual(day02.get_variance(self.ids[2]), {"a": 1, "b": 2, "c": 1, "d": 1, "e": 1})
        self.assertDictEqual(day02.get_variance(self.ids[3]), {"a": 1, "b": 1, "c": 3, "d": 1})
        self.assertDictEqual(day02.get_variance(self.ids[4]), {"a": 2, "b": 1, "c": 1, "d": 2})
        self.assertDictEqual(day02.get_variance(self.ids[5]), {"a": 1, "b": 1, "c": 1, "d": 1, "e": 2})
        self.assertDictEqual(day02.get_variance(self.ids[6]), {"a": 3, "b": 3})

    def test_get_checksum(self):
        self.assertEqual(day02.get_checksum(self.ids), 12)


class Part2(unittest.TestCase):
    ids = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

    def test_get_common_letters(self):
        self.assertEqual(day02.get_common_letters(self.ids), "fgij")
