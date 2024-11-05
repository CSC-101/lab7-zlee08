from convert import str_to_float


def gather_numbers() -> list[float]:
    number_list = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish):")
        if user_input.lower() == 'done':
            break
        number = str_to_float(user_input)
        if number is not None:
            number_list.append(number)
        else:
            print("Invalid input")
        return number_list

if __name__ == '__main__':
    number_list = gather_numbers()
    print("Sum of numbers:",sum(number_list))

