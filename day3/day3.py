#!/usr/bin/env python3

def get_content(path):
    with open(path, 'r') as data:
        return data.readlines()

def str_list_to_int_list(input):
    for i, value in enumerate(input, start=0):
        input[i] = int(value)
    return input

def new_grid(x_max=1000, y_max=1000):
    x_axis = []
    for x in range(x_max):
        y_axis = []
        for y in range(y_max):
            y_axis.append(0)
        x_axis.append(y_axis)
    return x_axis

def get_path(raw):
    heading = raw[0:1]
    distance = int(raw[1:len(raw)])
    return heading, distance

def get_shortest_distance(cross_sections):
    shortest = 0
    for i, cross_section in enumerate(cross_sections, start=0):

        # conver to positive because it doesnt matter for distance
        x_dist = abs(cross_section[0])
        y_dist = abs(cross_section[1])
        sum = x_dist + y_dist

        if i == 0:
            shortest = sum
            continue

        if sum < shortest:
            shortest = sum

    return shortest

def get_cross_sections(dict1, dict2):
    cross_sections = []

    for loc in dict1.keys():
        if (loc[0], loc[1]) in dict2:
            cross_sections.append((loc[0], loc[1]))

    for loc in dict2.keys():
        if (loc[0], loc[1]) in dict1:
            if not (loc[0], loc[1]) in cross_sections:
                cross_sections.append((loc[0], loc[1]))
    
    return cross_sections

def travel(directions):
    visited = {}
    location = [0,0]

    for raw_path in directions:

        heading, distance = get_path(raw_path)
        x, y = tuple(location)

        # y axis - up / down
        if heading == 'U':
            for i in range(distance):
                y += 1
                visited[x,y] = True
            location[1] = y
            
        if heading == 'D':
            for i in range(distance):
                y -= 1
                visited[x,y] = True
            location[1] = y

        # x axis left / right
        if heading == 'L':
            for i in range(distance):
                x -= 1
                visited[x,y] = True
            location[0] = x

        if heading == 'R':
            for i in range(distance):
                x += 1
                visited[x,y] = True
            location[0] = x

    return visited

def part_one(input_path='input'):
    # hacky cleanup, could be improved but this works for now
    wire_directions = get_content(input_path)
    wire1_directions = wire_directions[0].replace('\n','').split(',')
    wire2_directions = wire_directions[1].replace('\n','').split(',')
    wire1_visted = travel(wire1_directions)
    wire2_visted = travel(wire2_directions)
    cross_sections = get_cross_sections(wire1_visted, wire2_visted)
    
    return get_shortest_distance(cross_sections)

def main(input_path='input'):
    print('part one: {}'.format(part_one(input_path)))

if __name__ == '__main__':
    main()
