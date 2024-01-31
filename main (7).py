a = int(input("Введите массу тела: "))
b = int(input("Введите объем тела: "))
s = a / b
print("ответ: s =" ,s)

#2

d = int(input("введите первое число:"))
l = int(input("введите второе число: "))
sum_res = d + l
diff = d - l
prod = d * l
q = d / l

print("ОТВЕТ: sum_res=" ,sum_res)
print("ОТВЕТ : diff=" ,diff)
print("ОТВЕТ: prod=" ,prod)
print("ОТВЕТ: q" ,q)




# 3
num1 = int(input("Введите первое положительное число: "))
num2 = int(input("Введите второе положительное число: "))
b = (num1 + num2) / 2
c = (num1 * num2)
print("Среднее арифметическое:", b)
print("Среднее геометрическое:", c)

# 4
area = int(input("Введите площадь государства (в кв. км): "))
population = int(input("Введите количество жителей: "))
b = population / area
print("Плотность населения составляет", b, "чел/кв. км")

# 5
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))
g = 2 * (a * b + b * c + a * c)
volume = a * b * c
print("Площадь поверхности прямоугольного параллелепипеда:", g)
print("Объем прямоугольного параллелепипеда:", volume)