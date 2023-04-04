print("\nTask 1")
num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))
num3 = int(input("Введите 3 число: "))
average = (num1 + num2 + num3)/3
max1 = num1 > num2 and num1 > num3
max2 = num2 > num3 and num2 > num1
max3 = num3 > num2 and num3 > num1
print("Среднее арифметическое равно", average)
print(" Если 1 число = True, то", num1, "- максимальное. | Проверка: ", max1)
print(" Если 2 число = True, то", num2, "- максимальное. | Проверка: ", max2)
print(" Если 3 число = True, то", num3, "- максимальное. | Проверка: ", max3)

"""
# Мне не пришло в голову, как можно вывести максимальное число по другому
# и без применения функций if and else. Т.к мы еще их не брали.
# Но на всякий случай я написал в этом комментарии решение с их использованием.

if num1 > num2 and num1 > num3:
    print(num1, "- максимальное число")
else:
    pass
if num2 > num3 and num2 > num1:
    print(num2, "- максимальное число")
else:
    pass
if num3 > num2 and num3 > num1:
    print(num3, "- максимальное число")
else:
    pass
"""

print("\nTask 2")
salary = int(input("Введите зарплату: "))
credit = int(input("Введите сумму месячного платежа по кредиту: "))
debt = int(input("Введите задолженность за коммунальные услуги: "))
result = salary - credit - debt
print("После всех выплат у вас осталось:", result, "$")

print("\nTask 3")
diagonal1 = int(input("Введите первую диагональ: "))
diagonal2 = int(input("Введите вторую диагональ: "))
S_of_romb = 1/2 * diagonal1 * diagonal2
print("Площаль ромба равна: ", S_of_romb)

print("\nTask 4")
passed = int(input("Введите кол-во студентов, сдавших экзамен: "))
did_not_pass = int(input("Введите кол-во студентов, не сдавших экзамен: "))
percentage = did_not_pass / passed * 100
per_passed = 100 - percentage
per_did_not_passed = percentage
print("Процент сдавших экзамен:", per_passed)
print("Процент не сдавших экзамен:", per_did_not_passed)
print(passed >= did_not_pass)


