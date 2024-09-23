#!/usr/bin/python3
"""
Returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """ Calculate the perimeter of an island """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check for water or out of bounds in each direction
                # Check above
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check below
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
