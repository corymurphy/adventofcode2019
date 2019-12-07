import unittest

from day2 import *
from day2 import main as day2_main

class TestDay2(unittest.TestCase):

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