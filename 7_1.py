class Matrix:

    def __init__(self, matrix):

        self.matrix = matrix

    def __add__(self, other):

        result = []

        for item in zip(self.matrix, other.matrix):
            result.append([sum([i, j]) for i, j in zip(*item)])

        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])


if __name__ == '__main__':
    matrix_1 = Matrix([[17, 2, 15, 6], [32, 14, 7, 18]])
    print(matrix_1, '\n')

    matrix_2 = Matrix([[11, 22, 55, 66], [33, 44, 77, 88]])
    print(matrix_2, '\n')

    print(matrix_1 + matrix_2)