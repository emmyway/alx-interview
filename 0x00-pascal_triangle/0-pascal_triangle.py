#!/usr/bin/python3

def pascal_triangle(n):
    '''
    Generate a Pascal's triangle up to nth row.

    Args:
    n (int): The number of rows in Pascal's triangle to generate.

    Returns:
    List[List[int]]: A list of lists representing Pascal's triangle,
    Return an empty list
    '''

    if n <= 0:
        return []

    # Initialize Pascal's triangle withthe first row
    triangle = [[1]]

    # construct each row of Pascal's triangle
    for i in range(1, n):
        # start the row with a 1
        row = [1]

        # compute the values for the current row
        for j in range(1, i):
            # each value is the sum of the two values directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # end the row with a 1
        row.append(1)

        # Add the row to the triangle
        triangle.append(row)

    return triangle
