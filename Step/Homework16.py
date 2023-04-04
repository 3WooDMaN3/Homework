# map() - позволяет обрабатывать одну или несколько последовательностей с использованием заданной функции.
# reduce()- когда требуется обработать список значений таким образом, чтобы свести процесс к единственному результату,
# filter()- определяет нужно ли исключить конкретный элемент из последовательности или нет(если да  то фильтрует последовательность, если нет ничего не делает)
# zip()- oбъединяет отдельные элементы из каждой последовательности в итерируемую последовательность

'''   Функция reduce   '''


def my_reduce(function, list_el):
    result = 0
    for iterable in list_el:
        result += function(iterable)
    return result


list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_reduce(lambda element: element, list_))




'''   Функция фильтр'''
''' Дополнительно я использовал функцию, которая вычисляет является число простым, если да, то выводит True.
 Т.к filter реагирует только на данный boolean'''

def my_filter(function, list_el):
    new_list = []
    for iterable in list_el:
        if function(iterable) == True:
            new_list.append(iterable)
    return new_list


def prime_numbers(iterable):
    count = 0
    for el in range(1, iterable+1):
        if iterable % el == 0:
            count += 1
    if count == 2:
        return True


list_el = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_filter(prime_numbers, list_el))



'''             Функция zip            '''
"""Мне казалось что вы упомянули что нельзя использовать доп функции(такие как min(), max(), sum и т.д.)
Поэтому я Сделал свою функцию, которая вычисляет список в котором минимальное кол-во элементов и использует результат в функции zip"""
def my_zip(min_length, list_1, list_2):
    new_array = []
    array = []
    #(lst[i:i + n] for i in range(0, len(lst), n))
    for i in range(0, min_length):
        array.append(list_1[i])
        array.append(list_2[i])
    for i in range(0, len(array), 2):
        new_array.append(array[i:i+2])

    return new_array


def min_length(list_1, list_2):
    count = 0
    count1 = 0
    for i in range(len(list_1)):
        count1 += 1
    for j in range(len(list_2)):
        count += 1
    if count1 < count:
        minimal = count1
    else:
        minimal = count
    return minimal

list_1 = [26, 33, 45]
list_2 = [43, 31, 23, 34, 53, 53, 46, 86, 58, 85]
print(my_zip(min_length(list_1, list_2), list_1, list_2))



'''          Через гинераторы            '''

# MAP


def my_map(function,list_el):
    new_list = [function(iterable) for iterable in list_el]
    return new_list


list_el = [1,2,3,4,5,6,7,8,9,10]
print(my_map(lambda element: element*2,list_el))


# Filter


def my_filter(function, list_el):
    new_list = [iterable for iterable in list_el if function(iterable) == True]
    return new_list


def prime_numbers(iterable):
    count = 0
    for el in range(1, iterable+1):
        if iterable % el == 0:
            count += 1
    if count == 2:
        return True


list_el = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_filter(prime_numbers, list_el))
