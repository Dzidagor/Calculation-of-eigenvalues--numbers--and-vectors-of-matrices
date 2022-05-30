import numpy as np
matrix_A = np.array([[1.7, 1.6, 1.7, 1.8],
              [1.6, 2.7, 1.4, 1.3],
              [1.7, 1.4, 3.7, 1.4],
              [1.8, 1.3, 1.4, 4.7]])


integers_matrix_A, vectors_matrix_A = np.linalg.eig(matrix_A)
max_integer_matrix_A = max(abs(integers_matrix_A))


for i in range(len(integers_matrix_A)):
    if integers_matrix_A[i] == max_integer_matrix_A:
        index_max_integer_matrix_A = i

print(f"Собственные значения: {integers_matrix_A}\n"
      f"Собственные вектора: {vectors_matrix_A}\n"
      f"--------------------------------------\n"
      f"Максимальное по модулю собственное число: {max_integer_matrix_A}\n"
      f"Соответствующий ему собственный вектор:{vectors_matrix_A[index_max_integer_matrix_A]}")


