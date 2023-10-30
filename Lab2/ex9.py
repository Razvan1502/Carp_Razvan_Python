def find_obstructed_seats(matrix):
    obstructed_seats = []

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows - 1, 0, -1):
        for j in range(cols):
            if matrix[i][j] <= matrix[i - 1][j]:
                obstructed_seats.append((i, j))

    return obstructed_seats

def main():
    field = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

    obstructed = find_obstructed_seats(field)
    print(obstructed)

if __name__ == "__main__":
    main()
