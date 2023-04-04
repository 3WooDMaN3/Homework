def power(x, y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x*power(x, y-1)


def Fibonacci(num):

    if num == 0:
        return 0
    elif num == 1:
        print("Сумма последовательности Фибоначи = ", end="")
        return num + num

    else:

        return num + Fibonacci(num - 1)


n = 0
def square(length, symbol):
    global n
    n += 1
    if length == 1 or n == length:
        return (symbol + "  ") * length
    else:
        return (symbol + "  ") * length + "\n" + square(length, symbol)


def square_pol(length, symbol):
    global n
    n += 1
    if n == length+1:
        return "\t\t\t...Код выполнен...\t\t"
    elif 1 < n < length:
        return (symbol + ("\t") * (length - 1) + symbol) + "\n" + square_pol(length, symbol)

    else:
        return (symbol + "\t") * length + "\n" + square_pol(length, symbol)


def game():
    from random import randint
    pick = True
    select = 0
    while pick:
        num1 = 0
        random_number = randint(-500, 500)
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


def crate_matrix():
    n = int(input("Введите кол-во строк: "))
    m = int(input("Введите кол-во столбцов: "))
    new_array = []
    for i in range(m):
        array = [int(input(f"Введите элемент: ")) for i in range(0, n)]
        new_array.append(array)

    # произведение элементов
    print("\tПолучим матрицу: ")
    result_of_multiply = 1
    result_of_sum = 0
    for i in range(len(new_array)):
        for j in range(len(new_array)):
            print(new_array[i][j], end="\t\t")
            result_of_multiply *= new_array[i][j]
            result_of_sum += new_array[i][j]
        print("\n")
    print(f"Произведение всех чисел = {result_of_multiply}")
    print(f"Сумма всех чисел = {result_of_sum}")


def main():
    selection = input("Введите номер который хотите посмотреть: ")
    if selection == "1":
        num1 = int(input("Введите число: "))
        num2 = int(input("Введите степень: "))
        print(power(num1, num2))

    elif selection == "2":
        num = int(input("Введите число: "))
        print(Fibonacci(num))

    elif selection == "3":
        selection_1 = input("Введите True or False: ")
        if selection_1 == "True":
            length = int(input("Введите высоту: "))
            symbol = input("Введите символ: ")
            print(square(length, symbol))
        else:
            length = int(input("Введите выстоу: "))
            symbol = input("Введите символ: ")
            print(square_pol(length, symbol))

    elif selection == "4":
        game()

    elif selection == "5":
        crate_matrix()


    else:
        print("Такого номера нету")

    selection2 = input("\nХотите посмотреть другой номер?: ")

    if selection2 == "да" or selection2 == "yes":
        main()


if __name__ == '__main__':
    main()