#15
import random
n = int(input("Введите размерность одномерного массива: "))
array = [random.randint(1, 100) for _ in range(n)]
print("Исходный массив:", array)
sq = array * array
print(sq)
tr = sq * array
print(tr)

#16
def find_min(a, b, c):
    return min(a, b, c)
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
min_num = find_min(num1, num2, num3)
print("Наименьшее число из введенных:", min_num)

#17
def find_remainder(char, num):
    char_code = ord(char)
    remainder = char_code % num
    return remainder
char = input("Введите символ: ")
num = int(input("Введите целое число: "))
result = find_remainder(char, num)
print("Остаток от деления кода символа ", char, " на число ", num, " равен: ", result)

#18
def find_integer_part(char, num):
    char_code = ord(char)
    integer_part = num // char_code
    return integer_part
char = input("Введите символ: ")
num = float(input("Введите вещественное число: "))
result = find_integer_part(char, num)
print("Целая часть от деления числа ", num, " на код символа ", char, " равна: ", result)
'
#19
import math
def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    side_a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    side_b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    side_c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    s = (side_a + side_b + side_c) / 2
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    return area
x1, y1 = map(float, input("Введите координаты первой вершины (x y): ").split())
x2, y2 = map(float, input("Введите координаты второй вершины (x y): ").split())
x3, y3 = map(float, input("Введите координаты третьей вершины (x y): ").split())
result = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
print("Площадь треугольника равна:", result)

#20
arr = list(map(int, input("Введите массив из 15 элементов через пробел: ").split()))
zero_indexes = [i for i, num in enumerate(arr) if num == 0]
if zero_indexes:
    print("Номера нулевых элементов: ", join(map(str, zero_indexes)))
else:
    print("Нулевых элементов нет")
last_positive_index = -1
for i, num in enumerate(arr):
    if num > 0:
        last_positive_index = i
if last_positive_index != -1:
    print("Номер последнего положительного элемента: ", last_positive_index)
else:
    print("Положительных элементов нет")
