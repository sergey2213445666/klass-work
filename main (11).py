
#Задача 1 def lok():    import random
    A = [[random.randint(-100, 100) for j in range(4)] for i in range(7)]    positive_sums = [sum(filter(lambda x: x > 0, row)) for row in A]    print("Суммы положительных элементов каждой строки:")    print(positive_sums)
lol()
#Задача 2 
import randomdef create_matrix(M):
    A = [[random.randint(0, 9) for j in range(M)] for i in range(M)]    return Adef count_nonzero_elements(row):
    return sum(1 for element in row if element != 0)M = 5A = create_matrix(M)
print("Матрица A:")for row in A:    print(row)
nonzero_c = [count_nonzero(row) for row in A]print("Количество ненулевых элементов в каждой строке:")
print(nonzero_c)
#Задача 3 import random
def crex(M, N):    A = [[random.randint(0, 9) for _ in range(N)] for _ in range(M)]    return A
def fin(row):    return min(row)
M = 5N = 4A = create_matrix(M, N)
print("Матрица A:")for row in A:    print(row)
min_e = [find(row) for row in A]print("Минимальные элементы в каждой строке:")print(min_e)
#Задача 4
import randomdef frfr(M, N):
    A = [[random.randint(0, 9) for _ in range(N)] for _ in range(M)]    return A
def l(row):    return sum(1 for eleme in row if eleme != 0)M = 5
N = 4A = frfr(M, N)
print("Матрица A:")for row in A:    print(row)
lop = [count(row) for row in A]print("Количество ненулевых элементов в каждой строке:")
print(lop)
