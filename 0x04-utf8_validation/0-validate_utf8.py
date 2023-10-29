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

    num_bytes = 0

    for num in data:
        bin_num = format(num, '#010b')[-8:]

        if num_bytes == 0:
            for digit in bin_num:
                if digit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (bin_num[0] == '1' and bin_num[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
