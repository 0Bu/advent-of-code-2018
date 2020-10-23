import unittest
import day03

claims = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'
]


class Part1(unittest.TestCase):
    def test_get_overlapped_claims(self):
        self.assertEqual(day03.get_overlapping_claims(claims), 4)


class Part2(unittest.TestCase):
    def test_get_nonoverlapping_claim_ids(self):
        self.assertSetEqual(day03.get_nonoverlapping_claim_ids(claims), {3})
