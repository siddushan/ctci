def swap(i, j, matrix):
    tmp = matrix[i][j]
    matrix[i][j] = matrix[j][i]
    matrix[j][i] = tmp
    return matrix


def rotate(matrix):
    """
    :param matrix: 2d list
    :return: 90 degree rotated matrix
    """
    matrix.reverse()
    """
    [[7,8,9],
     [4,5,6],
     [1,2,3]]
    """
    for i in range(len(matrix)):
        for j in range(i):
            matrix = swap(i, j, matrix)
    return matrix


li = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

print(rotate(li))
