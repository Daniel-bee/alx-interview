#!/usr/bin/python3
"""
Rotate 2D Matrix
"""
import copy


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    new_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        count = len(matrix) - 1
        for j in range(len(matrix)):
            matrix[i][j] = new_matrix[count][i]
            count -= 1
