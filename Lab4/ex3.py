class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.matrix[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.matrix[i][j] = value

    def transpose(self):
        transposed = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.matrix = transposed
        self.rows, self.cols = self.cols, self.rows

    def matrix_multiply(self, other_matrix):
        if self.cols != other_matrix.rows:
            print("Matrices cannot be multiplied.")
            return None

        result = [[0 for _ in range(other_matrix.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(other_matrix.cols):
                for k in range(self.cols):
                    result[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]

        return result

    def apply_transformation(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = func(self.matrix[i][j])

    def display(self):
        for row in self.matrix:
            print(row)

# Example usage:
mat = Matrix(2, 3)

mat.set(0, 0, 1)
mat.set(0, 1, 2)
mat.set(0, 2, 3)
mat.set(1, 0, 4)
mat.set(1, 1, 5)
mat.set(1, 2, 6)

print("Original Matrix:")
mat.display()

#mat.transpose()
print("\nTransposed Matrix:")
mat.display()

mat2 = Matrix(3, 2)
mat2.set(0, 0, 1)
mat2.set(0, 1, 2)
mat2.set(1, 0, 3)
mat2.set(1, 1, 4)
mat2.set(2, 0, 5)
mat2.set(2, 1, 6)

result = mat.matrix_multiply(mat2)
if result:
    print("\nMatrix Multiplication Result:")
    for row in result:
        print(row)

mat.apply_transformation(lambda x: x * 2)
print("\nMatrix after applying transformation:")
mat.display()
