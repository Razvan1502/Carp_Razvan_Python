def spiral_traversal(matrix):
    m = len(matrix)
    n = len(matrix[0])
    k = 0
    l = 0

    while (k < m and l < n):
        # top row
        for i in range(l, n):
            print(matrix[k][i], end=" ")

        k += 1

        # rightmost column
        for i in range(k, m):
            print(matrix[i][n - 1], end=" ")

        n -= 1

        if (k < m):
            # bottom row
            for i in range(n - 1, (l - 1), -1):
                print(matrix[m - 1][i], end=" ")

            m -= 1

        if (l < n):
            # leftmost column
            for i in range(m - 1, k - 1, -1):
                print(matrix[i][l], end=" ")

            l += 1

def main():
    matrix = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p']
    ]
    spiral_traversal(matrix)

if __name__ == "__main__":
    main()
