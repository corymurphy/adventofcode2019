import unittest
from day1 import *
from day1 import main as day1_main

class TestDay1(unittest.TestCase):

    def test_mass_is_1969_required_fuel_is_654(self):
        expected = 654
        actual = get_fuel_requirements_from_mass(1969)
        self.assertEqual(expected, actual)

    def test_mass_is_100756_required_fuel_is_33583(self):
        expected = 33583
        actual = get_fuel_requirements_from_mass(100756)
        self.assertEqual(expected, actual)

    def test_round_down_should_round_up_but_force_round_down(self):
        input = 479.6
        expected = 479
        actual = round_down(input)
        self.assertEqual(expected, actual)

    def test_round_down_should_round_down(self):
        input = 479.2
        expected = 479
        actual = round_down(input)
        self.assertEqual(expected, actual)

    def test_get_fuel_required_for_fuel_mass_33583_is_50346(self):
        expected = 50346
        actual = get_fuel_required_for_fuel_mass(33583)
        self.assertEqual(expected, actual)

    def test_part_one(self):
        expected = 3437969
        actual = part_one('day1/input')
        self.assertEqual(expected, actual)

    def test_part_two(self):
        expected = 5154075
        actual = part_two('day1/input')
        self.assertEqual(expected, actual)


    def test_main(self):
        print("")
        print(" ------------------------- ")
        print("")
        print("Advent of Code Day 1")
        print("")
        day1_main('day1/input')
        print("")
        print(" ------------------------- ")
        print("")

if __name__ == '__main__':
    unittest.main()