#!/usr/bin/python3

"""Rotate a 2D matrix 90 degrees clockwise"""
import sys


def rotate_2d_matrix(matrix):
    """This function transposed and reversed the matrix"""
    if not type(matrix) is list:
        sys.exit(1)

    n = len(matrix)
    if not n >= 2:
        sys.exit(1)

    for i in range(int(n / 2)):
        y = (n - i - 1)
        for j in range(i, y):
            x = (n - 1 - j)
            temp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = temp
            