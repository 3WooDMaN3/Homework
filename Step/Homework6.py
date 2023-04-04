print("\nTask 1:\n")
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))
print("Числа кратные 7: ", end="")
while num1 <= num2:
    while num1 % 7 == 0:
        print(num1, end=", ")
        num1 += 1
    num1 += 1


print("\nTask 2:\n")
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))
#
number1 = num1
number2 = num2
number_1 = num1
number_2 = num2
#
print("1. Все числа: ", end="")
while num1 <= num2:
    print(num1, end=", ")
    num1 += 1

print("\n\n2. Числа в обратном порядке: ", end="")
while num2 > 0:
    print(num2, end=", ")
    num2 -= 1

print("\n\n3. Все числа кратные 7:", end=" ")
while number1 < number2:
    while number1 % 7 == 0:
        print(number1, end=", ")
        number1 += 1
    number1 += 1

print("\n\n4. Кол-во чисел, кратных 5:", end=" ")
count = 0
while number_1 < number_2:
    while number_1 % 5 == 0:
        count += 1
        number_1 += 1
    number_1 += 1
print(count)


print("\n\n Task 3:")
num1 = int(input("Введите начало диапазона: "))
num2 = int(input("Введите конец диапазона: "))
num_1 = num1
print("\nЧисла кратные 3:")
while num1 < num2:
    while num1 % 3 == 0:
        print(num1, "Fizz")
        num1 += 1
    num1 += 1
num1 = num_1
print("\nЧисла кратные 5:")
while num1 < num2:
    while num1 % 5 == 0:
        print(num1, "Buzz")
        num1 += 1
    num1 += 1

num1 = num_1
print("\nЧисла не кратные 3 и 5: ", end="")
while num1 < num2:
    while num1 % 5 != 0 and num1 % 3 != 0:
        print(num1, end=", ")
        num1 += 1
    num1 += 1



