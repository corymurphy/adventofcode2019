import unittest

from day2.day2 import *
from day2.day2 import main as day2_main

class TestDay2(unittest.TestCase):

    def test_example0(self):
        intcode = [1,1,1,4,99,5,6,0,99]
        expected = [30,1,1,4,2,5,6,0,99]
        actual = run(intcode)
        self.assertEqual(expected, actual)

    def test_example0_position(self):
        intcode = [1,1,1,4,99,5,6,0,99]
        expected = 30
        actual = run(intcode)[0]
        self.assertEqual(expected, actual)

    def test_example1(self):
        intcode = [1,0,0,0,99]
        expected = [2,0,0,0,99]
        actual = run(intcode)
        self.assertEqual(expected, actual)

    def test_example1_position(self):
        intcode = [1,0,0,0,99]
        expected = 2
        actual = run(intcode)[0]
        self.assertEqual(expected, actual)

    def test_example2(self):
        intcode = [2,4,4,5,99,0]
        expected = [2,4,4,5,99,9801]
        actual = run(intcode)
        self.assertEqual(expected, actual)

    def test_example2_position(self):
        intcode = [2,4,4,5,99,0]
        expected = 2
        actual = run(intcode)[0]
        self.assertEqual(expected, actual)

    def test_example3(self):
        intcode = [1,1,1,4,99,5,6,0,99]
        expected = [30,1,1,4,2,5,6,0,99]
        actual = run(intcode)
        self.assertEqual(expected, actual)

    def test_example3_position(self):
        intcode = [1,1,1,4,99,5,6,0,99]
        expected = 30
        actual = run(intcode)[0]
        self.assertEqual(expected, actual)

    def test_part_one(self):
        intcode = str_list_to_int_list(get_deserialized_content('day2/input'))
        expected = 4576384
        actual = run(intcode)[0]
        self.assertEqual(expected, actual)

    def test_main(self):
        print("")
        print(" ------------------------- ")
        print("")
        print("Advent of Code Day 2")
        print("")
        day2_main('day2/input')
        print("")
        print(" ------------------------- ")
        print("")

if __name__ == '__main__':
    unittest.main()
