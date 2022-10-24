"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import random

a = []

for i in range(random.randint(6, 10)):
    a.append(random.randint(1, 10))
print("Данный массив:")
print(a)

max_index = a.index(max(a))
min_index = a.index(min(a))

a[max_index], a[min_index] = a[min_index], a[max_index]

print("Новый массив:")
print(a)
