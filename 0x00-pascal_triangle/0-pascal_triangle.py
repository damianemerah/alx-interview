#!/usr/bin/python3
"""
Generates Pascal's triangle
"""


def pascal_triangle(n):
    """
    pascal_triangle:
        Solves and generate pascal triangle
    n:
        number of triangle to generate
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        triangle.append(row)

    return triangle
