"""8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
матрицу. """

import random

b = []
c = []

for i in range(4):
    a = []
    for j in range(4):
        a.append(random.randint(0, 10))
    c.append(a)
    b.append(sum(a))
c.append(b)

print('Выводим полученную матрицу:')
for i in c:
    print(i)