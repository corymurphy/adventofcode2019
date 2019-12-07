import unittest

from day3.day3 import *
from day3.day3 import main as day3_main

class TestDay2(unittest.TestCase):

    def test_example0(self):
        expected = 6
        wire1_directions = 'U7,R6,D4,L4'.split(',')
        wire2_directions = 'R8,U5,L5,D3'.split(',')
        wire1_visted = travel(wire1_directions)
        wire2_visted = travel(wire2_directions)
        cross_sections = get_cross_sections(wire1_visted, wire2_visted)
        actual = get_shortest_distance(cross_sections)
        self.assertEqual(expected, actual)

    def test_example1(self):
        expected = 159
        wire1_directions = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
        wire2_directions = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
        wire1_visted = travel(wire1_directions)
        wire2_visted = travel(wire2_directions)
        cross_sections = get_cross_sections(wire1_visted, wire2_visted)
        actual = get_shortest_distance(cross_sections)
        self.assertEqual(expected, actual)

    def test_example2(self):
        expected = 135
        wire1_directions = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
        wire2_directions = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
        wire1_visted = travel(wire1_directions)
        wire2_visted = travel(wire2_directions)
        cross_sections = get_cross_sections(wire1_visted, wire2_visted)
        actual = get_shortest_distance(cross_sections)
        self.assertEqual(expected, actual)

    def test_part_one(self):
        expected = 709
        actual = part_one('day3/input')
        self.assertEqual(expected, actual)

    def test_shortest_steps0(self):
        expected = 610
        wire1_directions = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
        wire2_directions = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
        wire1_visted = travel(wire1_directions)
        wire2_visted = travel(wire2_directions)
        cross_sections = get_cross_sections_with_steps(wire1_visted, wire2_visted)
        actual = get_least_steps_by_cross_sections(cross_sections)
        self.assertEqual(expected, actual)

    def test_shortest_steps1(self):
        expected = 410
        wire1_directions = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'.split(',')
        wire2_directions = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'.split(',')
        wire1_visted = travel(wire1_directions)
        wire2_visted = travel(wire2_directions)
        cross_sections = get_cross_sections_with_steps(wire1_visted, wire2_visted)
        actual = get_least_steps_by_cross_sections(cross_sections)
        self.assertEqual(expected, actual)

    def test_main(self):
        print("")
        print(" ------------------------- ")
        print("")
        print("Advent of Code Day 3")
        print("")
        day3_main('day3/input')
        print("")
        print(" ------------------------- ")
        print("")

if __name__ == '__main__':
    unittest.main()


from day3.day3 import *
wire1_directions = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
wire2_directions = 'U62,R66,U55,R34,D71,R55,D58,R83'.split(',')
wire1_visted = travel(wire1_directions)
wire2_visted = travel(wire2_directions)
cross_sections = get_cross_sections(wire1_visted, wire2_visted)
cross_sections_steps = get_cross_sections_with_steps(wire1_visted, wire2_visted)
actual = get_shortest_distance(cross_sections)


a = cross_sections_steps[0]

a = {}

a[6,2] = 404
a[14,5] = 404