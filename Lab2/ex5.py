def replace(matrix):

    for i in range(len(matrix)):
        for j in range(i):
            if i > j:
                matrix[i][j] = 0
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m = replace(matrix)
for row in m:
    print(row)