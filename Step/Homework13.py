'''----------------------------------------------------------------------------------------------'''
print("Task 1:")
number = input("Введите число в двоичной системе счисления: ")
summ, result = 1, 0
for i in number[::-1]:
    if int(i) == 1:
        result += summ
    summ *= 2
print(f"Число в десятичной = {result}")
'''----------------------------------------------------------------------------------------------'''
print("Task 2:")
num = int(input("Введите кол-во метров: "))
select = input("Введите меру длины, куда хотите переводить: ")
if select == "милиметр" or select == "милиметры":
    print(f"{num} метров = {num*1000} милиметров")
elif select == "дюйм" or select == "дюймы":
    print(f"{num} метров = {num*39.37} дюймов")
elif select == "ярд" or select == "ярды":
    print(f"{num} метров = {num*3.281} ярд")
'''----------------------------------------------------------------------------------------------'''
print("Task 3:")
num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))
if num1 == num2:
    print(f"{num1} = {num2}")
else:
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
'''----------------------------------------------------------------------------------------------'''
print("Task 4:")
length = int(input("Введите длину линии: "))
synbol = input("Введите символ: ")
for i in range(length):
    print(synbol)
'''----------------------------------------------------------------------------------------------'''
print("Task 5: ")
digit = 0
x = True
while x:
    digit = int(input("Введите число: "))
    if digit == 7:
        x = False
    elif digit > 0:
        print("Number is positive")
    elif digit < 0:
        print("Number is negative")
    elif digit == 0:
        print('Number is equal to zero')
'''----------------------------------------------------------------------------------------------'''
print("\nTask 6 and 7: ")
stroka = input("Введите строку: ")
new_stroka = []
count = 0
before = False
for i in stroka:
    if before != i:
        new_stroka.append(i)
        before = i
    else:
        count+=1
print(f"Получим строку: {''.join(new_stroka)}")
print(f"Всего одинаковых лишних соседних символов в строке = {count}")
print(f"\nПолучим список: {new_stroka}")
print(f"Всего одинаковых лишних соседних символов в списке = {count}")
'''----------------------------------------------------------------------------------------------'''
print("Task 8:")
num = int(input("Введите число: "))
print("Введенное число в двоичной системе = ", end="")
list = []
while num != 0:
    list.append(str(num%2))
    num //= 2
list.reverse()
print("".join(list))
'''----------------------------------------------------------------------------------------------'''
print("Task 9:")
''' это задание вроде такое же как 7'''
n = int(input("Введите общее кол-во элементов: "))
new_list = [input("Введите элемент: ") for i in range(n)]
result = []
count = 0
before = False
for i in new_list:
    if before != i:
        before = i
    else:
        count += 1
print(new_list)
print(f"Всего одинаковых соседних одинаковых элементов в списке = {count}")
'''----------------------------------------------------------------------------------------------'''
from random import randint
print("Task1 10:")
m = int(input("Введите длину списка: "))
array = [randint(-100, 100) for i in range(m)]
print(array)
count = 0
for i in range(len(array)):
    for el in range(i+1, len(array)):
        if array[i] == array[el]:
            print(f"Число = {array[i]}")
            print(f"Индекс = {i, el}")
            count += 1
print(f"Кол-во одинаковых элементов = {count}")
'''----------------------------------------------------------------------------------------------'''
print("Task 11: ")
n, m = map(int, input("Введите два числа через пробел: ").split())
list_el = [[randint(-100, 100) for j in range(m)] for i in range(n)]
print(list_el)
print("1.1: ")
overall1 = 0
for i in list_el:
    overall1 += sum(i)
print(f"Sum of numbers = {overall1}")

print("1.2: ")
overall2 = 0
for i in list_el:
    for el in i:
        if el > 0:
            overall2 += el
print(f"Sum of positive numbers = {overall2}")

print("1.3:")
overall3 = 0
for i in list_el:
    for el in i:
        if el < 0:
            overall3 += el
print(f"Sum of negative numbers = {overall3}")

print("1.4:")
overall4 = 0
for i in list_el:
    for el in i:
        if el % 2 == 0:
            overall4 += el
print(f"Sum of even numbers = {overall4}")

print("1.5:")
overall5 = 0
for i in list_el:
    for el in i:
        if el % 2 != 0:
            overall5 += el
print(f"Sum of odd numbers = {overall5}")

print("1.6:")
overall6 = 0
total = 0
for i in range(len(list_el)):
    for el in range(len(list_el)):
        count = 0
        if int(list_el[i][el]) > 0:
            for j in range(1, int(list_el[i][el])+1):
                if list_el[i][el] % j == 0:
                    count += 1
            if count == 2:
                overall6 += list_el[i][el]
                total += 1
print(f"Sum of simple numbers = {overall6}")
print("1.7:")
print(f"Всего {total} простых чисел")
