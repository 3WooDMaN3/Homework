from random import *
length = int(input("Введите длину списка: "))
numbers1 = [randint(-100, 100) for i in range(length)]
numbers2 = [randint(-100, 100) for el in range(length)]
print("\nTask 1:")
new_list = []
new_list.extend(numbers1)
new_list.extend(numbers2)
new_list.sort()
print(f"Общий список -> {new_list}")

print("\nTask 2: ")
for i in new_list:
    if new_list.count(i) > 1:
        new_list.remove(i)
print(f"Общий список ез повторений -> {new_list}")

print("\nTask 3:")
overall_list = []
for i in numbers1:
    for el in numbers2:
        if i == el:
            overall_list.append(i)
if len(overall_list) == 0:
    print("Общих элементов нету")
else:
    print(overall_list)

print("\nTask 4: ")
for i in new_list:
    if new_list.count(i) > 1:
        for el in range(new_list.count(i)):
            new_list.remove(i)
print(f"Список элементов, содержащий уникальные элементы -> {new_list}")

print("\nTask 5: ")
new_list5 = [max(numbers1), min(numbers1), max(numbers2), min(numbers2)]
print(f"Список элементов, содержащий максимальные и минимальные значения -> {sorted(new_list5)}")





