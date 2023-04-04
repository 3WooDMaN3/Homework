print("Task 1:")
string = input("Введите текст: ")
new_string = string.split(". ")
for i in new_string:
    text = i.capitalize()
    print(f"{text}.", end=" ")
print("\n")

count = 0
symbols = 0
sign = 0
for i in string:
    if 48 <= ord(i) <= 57:
        count += 1
    if 33 <= ord(i) <= 47 or 58 <= ord(i) <= 63:
        symbols += 1
    if i == "!":
        sign += 1
print(f"Overall number of digits is {count} \nOverall number of symbols is {symbols} \nOverall number of ! is {sign}")

print("Task 2:")
expression = input("Введите выражение (вводите пожалуйста через пробел(13 + 13)): ")
new_expression = expression.split(" ")
''' В new_expression получаем список (как пример: ['44', '+', '2']), затем, с помощью индексов вычисляется выражение'''
if new_expression[1] == "+":
    result = float(new_expression[0]) + float(new_expression[2])
    print(f"{new_expression[0]} + {new_expression[2]} = {result}")
elif new_expression[1] == "-":
    result = float(new_expression[0]) - float(new_expression[2])
    print(f"{new_expression[0]} - {new_expression[2]} = {result}")
elif new_expression[1] == "*":
    result = float(new_expression[0]) * float(new_expression[2])
    print(f"{new_expression[0]} * {new_expression[2]} = {result}")
elif new_expression[1] == "/":
    result = float(new_expression[0]) / float(new_expression[2])
    print(f"{new_expression[0]} / {new_expression[2]} = {result}")

print("Task 3:")
print("\nКвадрат:\n")
for i in range(1, 9):
    print("*  " * 8)

print("\nПолый квадрат:\n")
for i in range(1, 9):
    if 1 < i < 8:
        print("*\t\t\t\t\t *")
    else:
        print("*  " * 8)

print("\nРавнобедренный треуголник\n")
for i in range(1, 9):
    print("*" * i)

print("\nПеревернутая версия\n")
for i in range(8, 0, -1):
    print("*" * i)


print("\nДругая перевернутая версия\n")
i = 8
el = 0
while i >= 0 and el <=8:
    print(" " * el + "*" * i)
    i -= 1
    el += 1

print("\nПолый квадрат c диагоналями:\n")


"""Читать этот код по мне вообще невозможно, поэтому я постараюсь словами обьяснить.
Сначало я сделал просто крест, с помощью двух циклов (1 цикл работает 4 раза до середины креста,
 2 цикл работает также только уже от середины креста, можно сказать что он перевернутый).
 А в конце я просто добавил звездочки как верхнюю и нижнюю стороны. В начале у меня был алгоритм, который поначалу даже работал,
  но потом все пошло не по плану и я начал экспериментировать, постоянно проверяя что получилось))"""
i = 8
el = 0
print("*  " * 11, "\t\t обычный print")
while i > 1 and el <= 4:
    print("* ", "   " * el + "*" + "   " * i + "*" + " " * el * 3 + " *", "\t\t 1 цикл")
    i -= 2
    el += 1
print("*\t\t\t   *\t\t\t  *", "\t\t обычный print")

i = 4
el = 0
while i >= 0 and el < 8:
    i -= 1
    el += 2
    print("* ", "   " * i + "*" + "   " * el + "*" + " " * i * 3 + " *", "\t\t 2 цикл")
print("*  " * 11, "\t\t обычный print")