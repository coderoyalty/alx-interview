#!/usr/bin/python3
"""
island perimeter solution
"""


def island_perimeter(grid):
    """
    calculate the perimeter of an island
    """
    if not grid:
        return 0
    rows = len(grid)
    cols = rows

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                elif j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
