#1
n = int(input("введите n: "))

i = 1 
while i < n:
    print(i)
    i += 1


#2
a = int(input("введите a: "))

n = 1 
s = 0

while s <= a:
    s += 1/n 
    if s > a:
        break
    print(n)
    n += 1
    
#3
n = int(input("введите n: "))

i = 1 
while i*i <= n:
    i += 1 
print(n, ":" , i)

#4
n = 201
while n % 12 != 0:
    n += 1 
print(n)

#5
n = 600
while n % 28 != 0:
    n -= 1 
print(n)