print("Task 1:")
num1 = int(input("Введите номер дня недели (от 1 до 7): "))
if num1 == 1:
    print("Понедельник")
elif num1 == 2:
    print("Вторник")
elif num1 == 3:
    print("Среда")
elif num1 == 4:
    print("Четверг")
elif num1 == 5:
    print("Пятница")
elif num1 == 6:
    print("Суббота")
elif num1 == 7:
    print("Воскресенье")
else:
    print("Вы ввели не то число")

print("\nTask 2:")
month = int(input("Введите номер месяца (от 1 до 12): "))
if month == 1:
    print("Январь")
elif month == 2:
    print("Февраль")
elif month == 3:
    print("Март")
elif month == 4:
    print("Апрель")
elif month == 5:
    print("Май")
elif month == 6:
    print("Июнь")
elif month == 7:
    print("Июль")
elif month == 8:
    print("Август")
elif month == 9:
    print("Сентябрь")
elif month == 10:
    print("Октябь")
elif month == 11:
    print("Ноябрь")
elif month == 12:
    print("Декабрь")
else:
    print("Вы ввели не то число")

print("\nTask 3:")
num = float(input("Введите число: "))
if num > 0:
    print("Number is positive")
elif num == 0:
    print("Number is equal to zero")
else:
    print("Number is negative")

print("\nTask 4:")
num1 = int(input("Введите 1 число:"))
num2 = int(input("Введите 2 число:"))
if num1 == num2:
    print("Введенные числа равны")
else:
    print("Введенные числа не равны")
if num1 >= num2:
    print(num2, num1)
else:
    print(num1, num2)

