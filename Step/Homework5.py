print("Task 1:")
price = int(input("Введите цену билета: "))
number_adults = int(input("Введите кол-во взрослых: "))
number_kids = int(input("Введите кол-во детей: "))
totalPriceForAdults = price * number_adults
totalPriceForKids = price * 0.6 * number_kids
print(totalPriceForAdults + totalPriceForKids)

print("\nTask 2:")
price = int(input("Введите цену блокнота: "))
discount = int(input("Введите скидку(%): "))
numbers_notebooks = int(input("Введите кол-во блокнотов: "))
total = numbers_notebooks * (1 - discount/100) * price
print(total)

print("\nTask 3:")
num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))
num3 = int(input("Введите 3 число: "))

if num1 > num2 and num1 > num3:
    print("1st: True")
if num2 > num3 and num2 < num1:
    print("2st: True")
if num3 > 0 and num3 < num1 and num3 < num2:
    print("3rd: True")




print("\nTask 4:")
num = 0
while 9999 > num or num >= 99999:
    num = int(input("Введите 5-значное число: "))

const = num
# Разбиваем на отдельные числа
first = num // 10000
num -= first * 10000
second = num // 1000
num -= second * 1000
third = num // 100
num -= third * 100
fourth = num // 10
num -= fourth * 10
fivth = num // 1
print(fivth, fourth, third, second, first)

'''переменная count считает кол-во делителей числа, если кол-во делителей == 2, то число простое.
Далее если число простое присваваем к переменной _1, _2... значения True, для того чтобы можно было вывести сумму всех простых чисел'''

# для числа fivth
count = 0
i = 1
while i < 10:
    if fivth % i == 0:
        count += 1
    i += 1
if count == 2:
    print(fivth, "- простое число")
    _5 = True
else:
    _5 = False

# для числа fourth
count = 0
i = 1
while i < 10:
    if fourth % i == 0:
        count += 1
    i += 1
if count == 2:
    print(fourth, "- простое число")
    _4 = True
else:
    _4 = False

# для числа third
count = 0
i = 1
while i < 10:
    if third % i == 0:
        count += 1
    i += 1
if count == 2:
    print(third, "- простое число")
    _3 = True
else:
    _3 = False

# для числа second
count = 0
i = 1
while i < 10:
    if second % i == 0:
        count += 1
    i += 1
if count == 2:
    print(second, "- простое число")
    _2 = True
else:
    _2 = False

# для числа first
count = 0
i = 1
while i < 10:
    if first % i == 0:
        count += 1
    i += 1
if count == 2:
    print(first, "- простое число")
    _1 = True
else:
    _1 = False

if _5 and _4 and _3 and _2 and _1:
    print(fivth + fourth + third + second + first)


print("________________________")
print("С помощью цикла for:")
for i in str(const):
    count = 0
    for el in range(1, 11):
        if int(i) % el == 0:
            count += 1
    if count == 2:
        print(i, "- простое число")




