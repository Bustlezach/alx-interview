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

    number_bytes = 0

    for num in data:
        bin_num = format(num, '#010b')[-8:]

        if number_bytes == 0:
            for digit in bin_num:
                if digit == '0':
                    break
                number_bytes += 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not (bin_num[0] == '1' and bin_num[1] == '0'):
                return False

        number_bytes -= 1

    return number_bytes == 0
