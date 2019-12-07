#!/usr/bin/env python3

import os

def str_list_to_int_list(input):
    for i, value in enumerate(input, start=0):
        input[i] = int(value)
    return input

def get_content(path):
    with open(path, 'r') as data:
        return data.read()

def get_deserialized_content(path):
    return get_content(path).split(',')

def run(intcode=[0]):

    i = 0
    opcode = intcode[i]
    while opcode != 99:
        
        one = intcode[intcode[i+1]]
        two = intcode[intcode[i+2]]
        result_index = intcode[i+3]

        if opcode == 1:
            result = one + two
        elif opcode == 2:
            result = one * two
        else:
            raise Exception("invalid opcode {}".format(opcode))

        intcode[result_index] = result
        i = i + 4
        opcode = intcode[i]

    return intcode

def get_noun_verb_to_equal_output(init_intcode, target_output=19690720, noun_max=100, verb_max=100):
    output = 0
    for noun in range(noun_max):
        for verb in range(verb_max):
            
            intcode = init_intcode.copy()
            intcode[1] = noun
            intcode[2] = verb

            try:
                output = run(intcode)[0]
            except:
                continue
            if output == target_output:
                return (100 * noun) + verb

    raise Exception('could not find target optcode')

def main(input_path='input'):
    pass
    init_intcode = str_list_to_int_list(get_deserialized_content(input_path))
    print('part one: {}'.format(run(init_intcode.copy())[0]))
    print('part two: {}'.format(get_noun_verb_to_equal_output(init_intcode.copy(), 19690720)))


if __name__ == '__main__':
    main()