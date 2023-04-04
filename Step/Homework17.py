from random import randint


def my_sort_for_binary_search(list, trigger):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    print(binary_search(list, trigger))


def binary_search(arr, trigger):
    low_border = 0
    high_border = len(arr)-1

    while low_border <= high_border:  # 0-7 5 -7 0-3
        middle = (low_border+high_border)//2  # 4
        if arr[middle] == trigger:
            return middle
        elif arr[middle] < trigger:
            low_border = middle + 1  # low = 5
        else:
            high_border = middle - 1  # high 3

    return -1


arr = [32, 32, 2, 41, 3, 8, 85, 45]
my_sort_for_binary_search(arr,8)




# Задания


def my_sort(list):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def output(list1, list2):
    for i in range(len(list1)):
        print(f"Название: {list1[i]} | Год издания: {list2[i]}")


def output_task1(list1, list2):
    for i in range(len(list1)):
        print(f"Номер идентификатора: {list1[i]} | Номер телефона: {list2[i]}")



def main():
    print("\n\n!!Notes!!")
    print("1 - сортировка по названию книг/идентификационным кодам")
    print("2 - сортировка по годам выпуска/номерам телефона")
    print("3 - вывод списка книг с их названиями и годом издательства/пользователей с кодами и телефонами")
    choose_task = int(input("Введите номер задания: "))
    selection = int(input("Введите номер меню(1, 2, 3, другое число - выход): "))
    if choose_task == 1:
        # Данные из задания 1
        # Идентификационный код
        list_codes = [randint(10000000, 99999999) for i in range(10)]
        # номер телефона
        list_phones = ["+99451" + str(randint(1000000, 1999999)) for j in range(10)]
        if selection == 1:
            print(my_sort(list_codes))
        elif selection == 2:
            print(my_sort(list_phones))
        elif selection == 3:
            print(output_task1(list_codes, list_phones))

    if choose_task == 2:
        # Данные из задания 2
        list_names = ["Мастер и Маргарита", "Собачье сердце", "Двенадцать стульев",
                      "Хоббит", "Алиса в стране чудес", "Остров сокровищ",
                      "Том Сойер", "Властелин Колец", "Никитос печатает..."]
        list_dates = [randint(1900, 2023) for i in range(len(list_names))]
        if selection == 1:
            print(my_sort(list_names))
        elif selection == 2:
            print(my_sort(list_dates))
        elif selection == 3:
            print(output(list_names, list_dates))


main()