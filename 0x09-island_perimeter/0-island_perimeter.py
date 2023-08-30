#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start with the maximumperimeter for each land cell
                perimeter += 4

                # Check adjacent cells and subtract 1 for
                # each adjacent land cell
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1

    return perimeter
