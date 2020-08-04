class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        try:
            result = [[int(self.matrix[row][i]) + int(other.matrix[row][i]) for i in range(len(self.matrix[row]))]
                      for row in range(len(self.matrix))]
            return Matrix(result)
        except IndexError:
            return f'Размеры складываемых матриц отличаются!'


my_1 = [[34, 54, 66], [1, 3, 5], [12, 32, 34]]
my_2 = [[22, 33, 44], [11, 33, 55], [22, 22, 99]]

matrix1 = Matrix(my_1)
matrix2 = Matrix(my_2)
result_matrix = matrix1 + matrix2
print(result_matrix)



print()
print('----------------------2-------------------')
print('При отличии размеров складываемых матриц:')
my_1 = [[34, 54, 66], [1, 3, 5], [12, 32, 34]]
my_2 = [[22, 33, 44], [11, 33, 55]]

matrix1 = Matrix(my_1)
matrix2 = Matrix(my_2)
result_matrix = matrix1 + matrix2
print(result_matrix)
