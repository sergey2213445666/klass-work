#30
import numpy as np
np.random.seed(0)
VM = np.random.randint(-10, 10, (3, 3))
print("Матрица ВМ:")
print(VM)
positive_elements = VM[VM > 0]
product_positive = np.prod(positive_elements)
print("\nПроизведение положительных элементов:", product_positive)
#31
import numpy as np
np.random.seed(1) 
VM = np.random.randint(0, 100, (3, 3))
print("Матрица В.М.:")
print(VM)
min_element = np.min(VM)
min_index = np.unravel_index(np.argmin(VM), VM.shape)
print("\nМинимальный элемент в матрице:", min_element)
print("Его координаты (строка, столбец):", min_index)
#32
import numpy as np
np.random.seed(2)
MM = np.random.randint(0, 100, (3, 3))
print("Матрица М.М.:")
print(MM)
min_element = np.min(MM)
max_element = np.max(MM)
min_index = np.unravel_index(np.argmin(MM), MM.shape)
max_index = np.unravel_index(np.argmax(MM), MM.shape)
MM[min_index], MM[max_index] = MM[max_index], MM[min_index]
print("\nИзмененная матрица М.М. (минимальный и максимальный элементы поменялись местами):")
print(MM)
#33
import numpy as np
np.random.seed(3)  
RM = np.random.randint(1, 10, (3, 4))
print("Матрица Р.М.:")
print(RM)
column_products = np.prod(RM, axis=0)
print("\nОдномерный массив из произведений элементов каждого столбца матрицы:")
print(column_products)
#34
import numpy as np
np.random.seed(5) 
MM = np.random.randint(-10, 10, (4, 5))
print("Матрица М.М.:")
print(MM)
negatives_count = np.sum(MM < 0, axis=1)
print("\nОдномерный массив из количеств отрицательных элементов каждой строки матрицы:")
print(negatives_count)
