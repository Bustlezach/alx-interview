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
    if n <= 1:
        return 0


    given = 'H'
    cp_ch = ''
    operation = 0
    given_len = 1


    while given_len < n:
        if n % given_len == 0:
            cp_ch = given
            operation += 1
        given += cp_ch
        given_len = len(given)
        operation += 1

    return operation

# Example usage:
n = 9
result = minOperations(n)
print("Number of operations:", result)
