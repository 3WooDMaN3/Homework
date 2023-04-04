def phrase():
    tab = "\t"
    print(f"“Don't compare yourself with anyone in this world… if you do so, you are insulting yourself.”"
          f"\n{tab*19}Bill Gates")


def array(num1, num2):
    if num2 > num1:
        new_list = [i for i in range(num1, num2+1) if i % 2 == 0]
        print(new_list)


def min(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    print(f"Максимальный элемент = {min}")


def multiply(num1, num2, num3):
    for i in range(num1, num2+1):
        print(f"{i}*{num3} = {i*num3}")

def quantity(num):
    option = True
    count = 1
    el = 1
    while option:
        while True:
            el *= 10
            if num // el != 0:
                count += 1
            else:
                option = False
                break
    print(f"{num} содержит {count} чисел")

def palindrom(num):
    if num == num[::-1]:
        print(f"{num} является палиндромом")
    else:
        print(f"{num} не является палиндромом")

def get_sum(num1, num2):
    sum = 0
    elements = [i for i in range(num1, num2 + 1)]
    for i in elements:
        sum += i
    print(sum)


def main():
    selection = input("Введите номер который хотите посмотреть: ")
    if selection == "1":
        print("Я отправил скриншот github")

    if selection == "2":
        phrase()

    if selection == "3":
        num1 = int(input("Введите начало диапазона: "))
        num2 = int(input("Введите конец диапазона: "))
        array(num1, num2)

    if selection == "4":
        arr = [int(input(f"Введите {i} число: ")) for i in range(1, 6)]
        min(arr)

    if selection == "5":
        num1 = int(input("Введите начало диапазона: "))
        num2 = int(input("Введите конец диапазона: "))
        num3 = int(input("Введите число на которое хотите умножить: "))
        multiply(num1, num2, num3)

    if selection == "6":
        num = int(input("Введите число: "))
        quantity(num)

    if selection == "7":
        num = input("Введите число: ")
        palindrom(num)

    if selection == "8":
        num1 = int(input("Введите начало диапазона: "))
        num2 = int(input("Введите конец диапазона: "))
        get_sum(num1, num2)

    else:
        print("Такого номера нету")

    selection2 = input("\nХотите посмотреть другой номер?: ")

    if selection2 == "да" or selection2 == "yes":
        main()



if __name__ == '__main__':
    main()




