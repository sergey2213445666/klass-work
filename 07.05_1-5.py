#1 
tourist_info = {
    "фамилия": "Иванов",
    "страна": "Франция",
    "год": 2022,
    "стоимость": 1000
}
print("Сведения о туристе:")
for key, value in tourist_info.items():
    print(f"{key}: {value}")
tourist_info["фамилия"] = input("Введите фамилию: ")
tourist_info["страна"] = input("Введите название страны: ")
tourist_info["год"] = int(input("Введите год поездки: "))
tourist_info["стоимость"] = float(input("Введите стоимость тура: "))
print("\nОбновленные сведения о туристе:")
for key, value in tourist_info.items():
    print(f"{key}: {value}")
#2
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
result = a * (b / 3.14) + (c * 3 + 5)
print("Результат выражения a*(b/3.14)+(c*3+5) равен:", result)
#3
R, Y = map(float, input("Введите значения R и Y через пробел: ").split())
result = R * Y**2 + (Y / 5)
print(f"Результат выражения {R}*{Y}²+({Y}/5) равен: {result}")
#4
import math
A = float(input("Введите положительное вещественное число A: "))
whole_part = int(A)
fractional_part = A - whole_part
sqrt_A = math.sqrt(A)
remainder = A % 5
print(f"Целая часть числа A: {whole_part}")
print(f"Дробная часть числа A: {fractional_part}")
print(f"Арифметический квадратный корень числа A: {sqrt_A}")
print(f"Остаток от деления числа A на 5: {remainder}")
#5
minutes = int(input("Введите количество минут, прошедших с полуночи (0 часов): "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"Время: {hours} часов {remaining_minutes} минут")