import math
import random
import time


def table():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    start_time = time.time()
    result = int(input(f'{a} * {b} = '))
    end_time = time.time()

    if result == a * b:
        print(f'temps = {end_time - start_time}')
    else:
        print(f'Nuuuuul : {a} * {b} = {a*b}')


def perfect_square(multiplied=False):
    a = random.randint(1, 10)
    a_square = a*a
    multiplier = None

    if multiplied:
        multiplier = random.randint(1, 10)

    start_time = time.time()

    if multiplied:
        result = input(f'√{a_square * multiplier} = ')

    else:
        result = input(f'√{a_square} = ')

    end_time = time.time()

    if (int(result.replace('r', '')) == a and not multiplied) or \
            (result == f'{a}r{multiplier}' and multiplied) or\
            int(result.split('r')[0]) * math.sqrt(int(result.split('r')[1])) or\
            int(result.replace('r', '')) == math.sqrt(a_square * multiplier):
        print(f'temps = {end_time - start_time}')

    else:
        if multiplied:
            print(f'nuuul ! result = {math.sqrt(a_square * multiplier)}\n ou result = {a}√{multiplier}')
        else:
            print(f'nuuul! result = {a}')


perfect_square(multiplied=False)
