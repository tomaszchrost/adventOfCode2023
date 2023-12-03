import DataFormatter

ASCII_DECIMAL_VALUE_0 = 48
ASCII_DECIMAL_VALUE_9 = 57


def check_for_int(character):
    if ASCII_DECIMAL_VALUE_0 <= ord(character) <= ASCII_DECIMAL_VALUE_9:
        return int(character)
    return None


spelt_numbers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def get_first_and_last_digit(text):
    first_digit = None
    last_digit = None
    current_characters = ''

    for character in text:
        number = check_for_int(character)
        if number:
            first_digit = number
            break
        else:
            current_characters += character
            for spelt_number in spelt_numbers:
                if spelt_number in current_characters:
                    first_digit = spelt_numbers[spelt_number]
                    break
            if first_digit is not None:
                break

    current_characters = ''

    for character in reversed(text):
        number = check_for_int(character)
        if number:
            last_digit = number
            break
        else:
            current_characters += character
            reversed_characters = ''.join(reversed(current_characters))
            for spelt_number in spelt_numbers:
                if spelt_number in reversed_characters:
                    last_digit = spelt_numbers[spelt_number]
                    break
            if last_digit is not None:
                break

    return int(str(first_digit) + str(last_digit))


def calculate_sum_of_first_and_last_digits(lines):
    sum = 0
    for line in lines:
        sum += get_first_and_last_digit(line)

    return sum


if __name__ == '__main__':
    # dataFormatter = DataFormatter.DataFormatter('firstStarData.dat')
    # data = dataFormatter.get_formatted_data_for_first_star()
    # print(calculate_sum_of_first_and_last_digits(data))

    dataFormatter = DataFormatter.DataFormatter('firstStarData.dat')
    data = dataFormatter.get_formatted_data_for_first_star()
    print(calculate_sum_of_first_and_last_digits(data))
