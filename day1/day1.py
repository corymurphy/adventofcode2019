#!/usr/bin/env python3

import os

def get_content(path):
    with open(path, 'r') as data:
        return data.readlines()

def round_down(value):
    if value <= 0:
        raise Exception('cannot round a value less than or equal 0')
    if is_int(value):
        return value

    if round(value) > value:
        return round(value) - 1
    else:
        return round(value)

def is_int(value):
    if value % 1 == 0:
        return True
    else:
        return False

def get_fuel_requirements(path):
    masses = get_content(path)
    total_fuel = 0
    for mass in masses:
        fuel = round_down(int(mass) / 3) - 2
        total_fuel = total_fuel + fuel
    return total_fuel

def get_fuel_requirements_from_mass(mass):
    return round_down(int(mass) / 3) - 2

def get_fuel_required_for_fuel_mass(mass, total_fuel=0):
    if total_fuel == 0:
        total_fuel = mass

    required_fuel = get_fuel_requirements_from_mass(mass)
    if required_fuel <= 0:
        return 0 + total_fuel
    if required_fuel <= 2:
        return required_fuel + total_fuel
    total_fuel = total_fuel + required_fuel
    return get_fuel_required_for_fuel_mass(required_fuel, total_fuel)

def part_one(mass_path = 'input'):
    masses = get_content(mass_path)
    total_fuel = 0
    for mass in masses:
        total_fuel = total_fuel + get_fuel_requirements_from_mass(mass)
    return total_fuel

def part_two(mass_path = 'input'):
    masses = get_content(mass_path)
    total_fuel = 0
    for mass in masses:
        fuel_for_mass = get_fuel_requirements_from_mass(mass)
        total_fuel = total_fuel + get_fuel_required_for_fuel_mass(fuel_for_mass)
    return total_fuel

def main(mass_path='input'):
    print("part one: {}".format(part_one(mass_path)))

    print("part two: {}".format(part_two(mass_path)))

if __name__ == '__main__':
    main()


