def is_number(char: str) -> bool:
    try:
        int(char)
        return True
    except ValueError:
        return False


def sum_numbers(text: str) -> int:
    numbers = []
    num_string = []
    for i in range(len(text)):
        current_char = text[i]
        next_char = ''

        try:
            has_next = False
            if i != len(text) - 1:
                has_next = True
                next_char = text[i + 1]

            if not has_next and is_number(current_char):
                num_string.append(current_char)
                raise ValueError

            if has_next and is_number(current_char) and (is_number(next_char) or next_char == ' '):
                num_string.append(current_char)
                continue

            raise ValueError

        except ValueError:
            if len(num_string) > 0:
                numbers.append(int(''.join(num_string)))
                num_string = []

    return sum(numbers)


def sum_numbers_v2(text: str) -> int:
    text = text.split()
    z = 0
    for i in text:
        try:
            z += int(i)
        except ValueError:
            pass
    return z


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers_v2('This picture is an oil on canvas '
                          'painting by Danish artist Anna '
                          'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
