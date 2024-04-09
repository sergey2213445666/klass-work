#35
import numpy as np
def matrix():
    a = np.random.randint (-10, 10, size=(7, 4))
    print("Матрица А(7, 4):")
    print(a)
    
    positive_sums = []
    for row in a:
        positive_sums = sum([x for x in row if x > 0])
        positive_sums.append(positive_sums)
    return positive_sums
positive_sums = matrix()
print("Одномерный массив из сумм положительный элементов каждой строки матрицы:")
print(positive_sums)
#36
import numpy as np

def create_matrix(M, N):
    A = np.random.randint(-10, 10, size=(M, N))
    print(f"Матрица A({M}, {N}):")
    print(A)
    
    column_means = []
    for j in range(N):
        column_mean = np.mean(A[:, j])
        column_means.append(column_mean)
    
    return column_means

M = 5
N = 3
column_means = create_matrix(M, N)
print("Одномерный массив из средних арифметических каждого столбца матрицы:")
print(column_means)
#37
import numpy as np

def create_matrix(M, N):
    A = np.random.randint(-10, 10, size=(M, N))
    print(f"Матрица A({M}, {N}):")
    print(A)
    
    row_nonzero_counts = [np.count_nonzero(row) for row in A]
    
    return row_nonzero_counts

M = 4
N = 3
row_nonzero_counts = create_matrix(M, N)
print("Одномерный массив из количеств ненулевых элементов каждой строки матрицы:")
print(row_nonzero_counts)
#38
import numpy as np

def create_matrix(M, N):
    B = np.random.randint(-10, 10, size=(M, N))
    print(f"Матрица B({M}, {N}):")
    print(B)
    
    col_neg_prod = [np.prod(col[col < 0]) for col in B.T]
    
    return col_neg_prod

M = 4
N = 3
col_neg_prod = create_matrix(M, N)
print("Одномерный массив из произведений отрицательных элементов каждого столбца матрицы:")
print(col_neg_prod)
#39
import numpy as np

def create_matrix(M, N):
    A = np.random.randint(1, 10, size=(M, N))  # Генерация случайной матрицы
    print(f"Матрица A({M}, {N}):")
    print(A)
    
    row_min_elements = [np.min(row) for row in A]
    
    return row_min_elements

M = 3
N = 4
row_min_elements = create_matrix(M, N)
print("Одномерный массив из минимальных элементов каждой строки матрицы:")
print(row_min_elements)
#41
import numpy as np

def create_matrix_and_column_products(M, N):
    B = np.random.randint(-10, 10, size=(M, N))  # Генерация случайной матрицы
    print(f"Матрица B({M}, {N}):")
    print(B)
    
    column_products = [np.prod(B[B[:, j] > 0, j]) for j in range(N)]
    
    return column_products

M = 4
N = 3
column_products = create_matrix_and_column_products(M, N)
print("Одномерный массив из произведений положительных элементов каждого столбца матрицы:")
print(column_products)
#43
import numpy as np

def create_matrix_and_row_col_counts(M, N):
    B = np.random.randint(0, 10, size=(M, N))  # Генерация случайной матрицы
    print(f"Матрица B({M}, {N}):")
    print(B)
    
    row_zero_counts = np.sum(B == 0, axis=1)
    col_nonzero_counts = np.sum(B != 0, axis=0)
    
    return row_zero_counts, col_nonzero_counts

M = 3
N = 4
row_zero_counts, col_nonzero_counts = create_matrix_and_row_col_counts(M, N)
print("Одномерный массив из количеств нулевых элементов каждой строки матрицы:")
print(row_zero_counts)
print("Одномерный массив из количеств ненулевых элементов каждого столбца матрицы:")
print(col_nonzero_counts)