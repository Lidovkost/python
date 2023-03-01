import numpy
class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists
    def __str__(self):
        list_for_print = ''
        for list in self.matrix:
             list_for_print += str(list) + '\n'
        return (list_for_print)
    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            print('Cкладывать и вычитать матрицы можно только одинаковой размерности.')
            return
        new_matrix = numpy.zeros((len(self.matrix),len(self.matrix[0])))
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[0])):
                new_matrix[i,j] = self.matrix[i][j] + other.matrix[i][j]
        return new_matrix
a = [1, 2, 3, 4, 5]
b = [2, 3, 4 ,5, 6]
c = [3, 4, 5, 6, 7]
d = [9, 8, 7, 6, 5]
lists = [a, b, c, d]
lists2 = [d, c, b, a]
matrix1 = Matrix(lists)
matrix2 = Matrix(lists2)
print(matrix1)
print(matrix2)

matrix_sum = matrix1 + matrix2
print(matrix_sum)