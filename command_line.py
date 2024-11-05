import sys

import convert

if __name__ == '__main__':
    total_sum = 0

    for arg in sys.argv[1:]:
        number = convert.str_to_float(arg)
        if number is not None:
            total_sum += number
        else:
            print("Invalid input")
    print("Sum of valid numbers:",total_sum)
