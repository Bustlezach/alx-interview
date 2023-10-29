#!/usr/bin/python3

def validUTF8(data):
    """Determines whether the binary of a number is a valid UTF-8 decoding.

    Args:
        data: A list of byte values.

    Returns:
        True if the data is valid UTF-8, False otherwise.
    """

    binary_sets = []
    state = False

    for val in data:
        bin_num = bin(val)
        binary_sets.append(bin_num[2:])

    for val in binary_sets:
        if not (val.startswith('0') or val.startswith('1')):
            if state:
                state = False
                break
        else:
            if '0' in val and '1' in val:
                state = True
            else:
                state = False
                break

    return state
