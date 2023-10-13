#!/usr/bin/python3


def minOperations(n):
    """
    This function calculates the fewest number of 
    operations needed to result in exactly n H characters in the file

    Returns an integer

    given - the given string 
    copy character - cp_ch
    number of loops - operation 
    length of given string - given_len
    """
    given = "H"
    cp_ch = ""

    given_len = 1
    operation = 0

    while given_len < n:
        if n % given_len == 0:
            cp_ch = given
            operation += 1
        given += cp_ch
        given_len = len(given)
        operation += 1
    return operation
