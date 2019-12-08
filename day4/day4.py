#!/usr/bin/env python3

def is_ascending(digits):
    for i, digit in enumerate(digits):
        if i == 0:
            continue

        if digit < digits[i - 1]:
            return False
    return True

def contains_matching_sequence_pt2(digits):
    has_dubs = False
    has_trips = False
    max_index = len(digits) - 1

    dubs_hit_on = []
    trips_hit_on = []

    for i, digit in enumerate(digits):
        if i == 0:
            continue

        if digits[i-1] == digit:
            if not digit in dubs_hit_on:
                dubs_hit_on.append(digit)
            has_dubs = True
    
        if i == max_index:
            if has_dubs and has_trips:
                if len(dubs_hit_on) > len(trips_hit_on) and not dubs_hit_on == trips_hit_on:
                    return True

            if has_dubs and not has_trips:
                return True
            


        if digits[i-1] == digit and not i + 1 > max_index and digits[i+1] == digit:
            if not digit in trips_hit_on:
                trips_hit_on.append(digit)
            has_trips = True
        
    return False

def contains_matching_sequential(digits):
    for i, digit in enumerate(digits):
        if i == 0:
            continue
    
        if digit == digits[i - 1]:
            return True
    return False

def get_possible_combinations(start=138241, end=674034):
    potential_passwords = []

    for number in range(start, end):
        digits = [int(d) for d in str(number)]
        if is_ascending(digits) and contains_matching_sequential(digits):
            potential_passwords.append(number)

    return potential_passwords


def get_possible_combinations_pt2(start=138241, end=674034):
    potential_passwords = []

    for number in range(start, end):
        digits = [int(d) for d in str(number)]
        if is_ascending(digits) and contains_matching_sequence_pt2(digits):
            potential_passwords.append(number)

    return potential_passwords

def part_one(start=138241, end=674034):
    potential_passwords = get_possible_combinations()
    return len(potential_passwords)

def part_two(start=138241, end=674034):
    potential_passwords = get_possible_combinations_pt2()
    return len(potential_passwords)

def main(start=138241, end=674034):
    print('part one: {}'.format(part_one()))
    print('part two: {}'.format(part_two()))

if __name__ == '__main__':
    main()
