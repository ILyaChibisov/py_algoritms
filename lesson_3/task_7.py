"""7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
(оба являться минимальными), так и различаться."""

import random

a = []
for i in range(random.randint(5, 15)):
    a.append(random.randint(0, 10))

print(f'Минимальные элементы в массиве {a} ->> {min(a)},', end='')

# удаляем минимальный элемент из массива

del a[a.index(min(a))]

print(min(a))
