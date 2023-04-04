print("Task 1:")
string = input("Введите строку: ")
reverse = string[::-1]
if string == reverse:
    print(string, "- палиндром")
else:
    print(string, "- не палиндром")

print("Task 2:")
digit = input("Введите число: ")
reverse = digit[::-1]
if digit == reverse:
    print(digit, "- палиндром")
else:
    print(digit, "- не палиндром")

print("Task 3:")
string = input("Введите строку: ")
symbol = 0
digits = 0
bukvi = 0
for i in string:
    if 33 <= ord(i) <= 47 or 58 <= ord(i) <= 63:
        symbol += 1
    elif 48 <= ord(i) <= 57:
        digits += 1
    elif 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        bukvi += 1
print("Всего цифр - ", digits, ";", "Всего символов -", symbol, ";", "Всего букв -", bukvi, ";")

print("Task 4:")
stroka = input("Введите строку: ")
symbol = input("Введите символ: ")
count = 0
for i in stroka:
    if i == symbol:
        count += 1
print(count)




