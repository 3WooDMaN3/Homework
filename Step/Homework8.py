"""TASK 1"""
from random import randint
pick = True
select = 0
while pick:
    num1 = 0
    random_number = randint(0, 2)
    while random_number != num1 and pick:
        num1 = int(input("\nВведите число: "))
        if num1 == random_number:
            print("Вы выиграли:")
            select = input("Хотите сыграть еще? Введите да или нет: ")
        elif num1 > random_number:
            print("Меньше\n")
        else:
            print("Больше\n")
    if select == "да" or select == "yes":
        continue
    else:
        break


"""TASK 2"""
x = int(input("Введите начало диапазона: "))
y = int(input("Введите конец диапазона: "))
for el in range(x, y + 1):
    res = 1
    for i in range(1, y+1):
        res *= el
        print(el, "^", i, "=", res)
    print("______________\n")