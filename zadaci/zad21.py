import math

def varijacija_petlje(matrix):
    m = len(matrix)
    n = len(matrix[0])

    suma = 0
    for i in range(m):
        for j in range(n):
            if i + 1 < m:
                suma  += abs(matrix[i][j] - matrix[i+1][j])

            if j + 1 < n:
                suma += abs(matrix[i][j]  - matrix[i][j+1])

    return suma


def varijacija(matrix):
    m = len(matrix)
    n = len(matrix[0])
    suma1 = sum(abs(matrix[i][j] - matrix[i][j+1]) for i in range(m) for j in range(n) if j + 1 < n)
    suma2 = sum(abs(matrix[i][j] - matrix[i+1][j]) for i in range(m) for j in range(n) if i + 1 < m)
    return suma1 + suma2

matrix = [[100,120],
          [110,150]]

matrix2 =[[2, 1, 9],
 [0, 5, 3],
 [7, 8, 6]]


print(varijacija(matrix))

