from random import randint
# array = []
# length = int(input("Введите длину списка: "))
# for i in range(length + 1):
#     array.append(randint(-100, 100))
# print(array)
# print("\nTask 3 (max and min):")
# highest = array[0]
# for i in array:
#     if i > highest:
#         highest = i
# lowest = array[0]
# for i in array:
#         if i < lowest:
#             lowest = i
# print(f"{highest} is the highest number and {lowest} is the lowest number")
# print("\nTask 3 (sum of negative and positive):")
#
# sum_of_positive, sum_of_negative, nulls = 0, 0, 0
# for i in array:
#     if i > 0:
#         sum_of_positive += i
#     elif i < 0:
#         sum_of_negative += i
#     else:
#         nulls += 1
# print(f"Sum of positive numbers is {sum_of_positive}, sum of negative is {sum_of_negative}, the number of nulls is {nulls}")
#
# print("\nTask 4:")
# new_list = []
# new_length = int(input("Введите суммарное кол-во элементов: "))
# for i in range(new_length + 1):
#     new_list.append(int(input("Введите число, которое будет внесено в список: ")))
# print("\nСПИСОК СОЗДАН!\n")
# find = int(input("Введите некоторое число: "))
# count = 0
# for i in new_list:
#     if i == find:
#         count += 1
# print(f"Всего {count} таких же элементов!")
#
# print("\nTask 5:\n")


list_elements = [randint(-100, 100), randint(-100, 100),
                 randint(-100, 100), randint(-100, 100),
                 randint(-100, 100)]
print(list_elements)
sum = 0
new_list = sum[i for i in list_elements if i > 0]


