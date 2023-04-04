from random import randint
from math import sqrt

'''Первые 6 заданий'''
'''1'''
def ZeroDivisionError_():
    num1 = int(input())
    num2 = int(input())
    try:
        res = num1/num2
        print(res)
    except ZeroDivisionError:
        print("Dont devide by zero")
#ZeroDivisionError_()


'''2'''
def sqrt_(num):
    try:
        new_num = int(num)
        result = sqrt(new_num)
        print(f"Корень из {new_num} = {result}")
    except ValueError:
        print("Нельзя вычислить корень из отрицательного числа!")
        print("Нельзя вводить строку!")
#num1 = input("Введите число: ")
#sqrt_(num1)


"""3"""
def arrays_max_value(array):
    maxim = array[0]
    try:
        for i in range(len(array)+1):
            if array[i] > maxim:
                maxim = array[i]
        return maxim
    except IndexError:
        print("Индекс вышел за пределы списка")
        return maxim
elements = [randint(1, 10) for i in range(5)]
#print(elements)
#print(arrays_max_value(elements))


"""4"""
def type_(x, y):
    try:
        if "." in x: new_x = float(x)
        else: new_x = int(x)

        if "." in y: new_y = float(y)
        else: new_y = int(y)

        result = new_x + new_y
        print(result)
    except ValueError:
        print("Вы ввели строку!")
#num_1 = input("Введите элемент: ")
#num_2 = input("Введите элемент: ")
#type_(num_1, num_2)


"""5"""
def string(stroka, digits):
    try:
        return stroka + digits
    except TypeError:
        return f"Ошибка! Сложить str и int нельзя!"
#stroka = input("Введите строку: ")
#num = int(input("Введите число: "))
#print(string(stroka, num))


'''6'''
def convert_type(element):
    select = input("Введите тип данных в который хотите преобразовать: ")
    if select == "bool":
        return bool(element)
    elif select == "int":
        try:
            return int(element)
        except ValueError:
            return "Преобразовать невозможно!"
    elif select == "str":
        try:
            return str(element)
        except ValueError:
            return "Преобразовать невозможно!"
    elif select == "float":
        try:
            return float(element)
        except ValueError:
            return "Преобразовать невозможно!"
    elif select == "complex":
        try:
            return complex(element)
        except ValueError:
            return "Преобразовать невозможно!"
    else:
        return "Вы ошиблись!"
#el = input("Введите элемент: ")
#print(convert_type(el))





'''Остальные 5 заданий'''
'''1'''
def find_zero(arr):
    try:
        for i in arr:
            if 0 not in arr:
                raise Exception("No zero elements")
            else:
                print(i)
                if i == 0:
                    break
    except Exception as e:
        print(e)
#array1 = [randint(0, 10) for i in range(10)]
#find_zero(array1)


'''2'''
def age(num):
    try:
        if num > 0: print(f"Вам {num} лет")
        else: raise Exception("Age is less than 0")
    except Exception as e: print(e)
#num = int(input("Введите возраст: "))
#age(num)


'''3'''
def sum(arr):
    try:
        result = 0
        for i in arr:
            if type(i) == int or type(i) == float: result += i
            else: raise Exception(f"Ошибка: {i} - строка")
        print(result)
    except Exception as e:
        print(e)
array = [32, "dsjad", 3, "djksahd", 3.4]
#sum(array)


'''4'''
def ConvertStringToDigit(string):
    try:
        digit = int(string)
        return digit
    except Exception:
        return f"{string} - нельзя перевести в число!"
#str_ng = input("Введите строку: ")
#print(ConvertStringToDigit(str_ng))


'''5'''
def sqrt_new(num):
    try:
        if num > 0: return num**0.5
        else: raise Exception(f"Ошибка: {num} <= 0")
    except Exception as e: return e
number = int(input("Введите число: "))
print(sqrt_new(number))