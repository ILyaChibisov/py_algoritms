"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""

import random

a = []

column = (random.randint(3, 4))
row = (random.randint(3, 4))

for i in range(row):
    b = []
    for j in range(column):
        b.append(random.randint(0, 10))
    a.append(b)

print(f'Данная матрица: {row} на {column}')
for i in a:
    print(i)

b = [min(row[i] for row in a) for i in range(column)]
print(f' Максимальный элемент среди минимальных элементов столбцов матрицы: {max(b)}')
