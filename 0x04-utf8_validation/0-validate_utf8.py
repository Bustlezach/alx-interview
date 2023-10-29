#!/usr/bin/python3
"""
Determines if given data represents valid utf8.
"""


def validUTF8(data):
    """Determines whether the binary of a number is a valid UTF-8 decoding.

    Args:
        data: A list of byte values.

    Returns:
        True if the data is valid UTF-8, False otherwise.
    """

    state = 0

    for num in data:
        bin_num = format(num, '#010b')[-8:]

        if state == 0:
            for digit in bin_num:
                if digit == '0':
                    break
                state += 1

            if state == 0:
                continue

            if state == 1 or state > 4:
                return False
        else:
            if not (bin_num.startswith('1') and bin_num.startswith('0')):
                return False

        state -= 1

    return state == 0
