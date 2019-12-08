import unittest

from day4.day4 import *
from day4.day4 import main as day4_main

class TestDay4(unittest.TestCase):

    def test_is_ascending_123456_true(self):
        self.assertTrue(is_ascending([1,2,3,4,5,6]))

    def test_is_ascending_123856_true(self):
        self.assertFalse(is_ascending([1,2,3,8,5,6]))

    def test_contains_matching_sequential_122345_true(self):
        self.assertTrue(contains_matching_sequential([1,2,2,4,5]))

    def test_contains_matching_sequential_123456_false(self):
        self.assertFalse(contains_matching_sequential([1,2,3,4,5,6]))

    def test_part_one(self):
        expected = 1890
        actual = len(get_possible_combinations())
        self.assertEqual(expected, actual)

    def test_contains_matching_sequential_pt2_112233_true(self):
        self.assertTrue(contains_matching_sequence_pt2([1,1,2,2,3,3]))

    def test_contains_matching_sequential_pt2_123444_true(self):
        self.assertFalse(contains_matching_sequence_pt2([1,2,3,4,4,4]))

    def test_contains_matching_sequential_pt2_111122_true(self):
        self.assertTrue(contains_matching_sequence_pt2([1,1,1,1,2,2]))

    def test_main(self):
        print("")
        print(" ------------------------- ")
        print("")
        print("Advent of Code Day 4")
        print("")
        day4_main()
        print("")
        print(" ------------------------- ")
        print("")

if __name__ == '__main__':
    unittest.main()
