print("Task 1: ")
a = 126.7658791
total_tonnes = int(a)
find_kg = (a % 126)*1000
total_kg = int(find_kg)
find_gr = (find_kg % total_kg)*1000
total_gr = int(find_gr)
print("Итого:", total_tonnes, "тонн,", total_kg, "килограмм и", total_gr, "грамм.")


print("\nTask 2: ")
a = "3.141592"
pi = float(a)
# Пусть для короткой записи радиус == R
R = 4
formula = (pi * R ** 2)
print("Точное значение:", formula)
print("Приближенное значение:", int(formula))


print("\nTask 3: ")
num1 = 50
num2 = 10
# x = конечное значение
x = num1 / 100 * num2
print("Точное значение:", x)
print("Приближенное значение:", int(x))

