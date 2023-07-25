#!/usr/bin/python3
"""
pascal triangle function
"""


def pascal_triangle(num: int):
    """
    this function will compute the binomial coefficient of pascal triangle.
    """
    if num <= 0:
        return []
    output = [[1]]

    while len(output) != num:
        arr = output[-1]
        next_arr = [1]
        for i in range(0, len(arr)):
            if (i + 1) != len(arr):
                val = arr[i] + arr[i + 1]
            else:
                val = arr[i]
            next_arr.append(val)
        output.append(next_arr)
    return output
