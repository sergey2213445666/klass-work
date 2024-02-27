#2
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))
result = A * (B / 3.14) + (C * 3 + 5)
print("\nResult of the expression A*(B/3.14) + (C*3 + 5):", result)



#1
my_dict = {}
my_dict["surname"] = "kosarev"
print ("Фамилия - ", my_dict["surname"])
my_dict1 = {}
my_dict1["country"] = "Russia"
print ("Страна - ", my_dict1["country"])
my_dict2 = {}
my_dict2["tour"] = "Moscow"
print ("Тур бы куплен в - ", my_dict2["tour"])
my_dict = {}
my_dict["year"] = "2012"
print ("В каком году был куплен тур - ", my_dict["year"])
my_dict = {}
my_dict["year_of_tour"] = "2013"
print ("В каком году была сама поездка - ", my_dict["year_of_tour"])
my_dict = {}
my_dict["Money"] = "5500$"
print ("Стоимость поездки - ", my_dict["Money"])
my_dict = {}
my_dict["surname"] = input("Фамилия - ")
my_dict1 = {}
my_dict1["country"] = input("Страна - ")
my_dict2 = {}
my_dict2["tour"] = input("Город - ")
my_dict = {}
my_dict["year"] = input("Год оформления - ")
my_dict = {}
my_dict["year_of_tour"] = input("Год поездки - ")
my_dict = {}
my_dict["Money"] = input("Стоимость - ")

#3 
R = int(input("Значение R ")); Y = int(input("Значение Y ")); E = R * (Y * Y) + (Y / 5); print("R * (Y * Y) + (Y / 5) = ", E) #Вводим значения и вычисляем

#4 
A = float(input("Введите положительное вещественное число A: ")) 
A1 = int(A) # Целая часть числа
A2 = A - A1 # Дробная часть числа
A3 = A ** 0.5 # Арифметический квадратный корень числа
A4 = A % 5 # Остаток от деления на 5

print("Целая часть числа A: ", A1)
print("Дробная часть числа A: ", A2)
print("Арифметический квадратный корень числа A: ", A3)
print("Остаток от деления числа A на 5: ", A4)

#5 
m = int(input("Введите количество минут, прошедших с полуночи (0 часов): "))
h = m // 60
r_m = m % 60
print("Время: ", h, "часов ", r_m, "минут")
