"""4. Определить, какое число в массиве встречается чаще всего."""

import random

a = []
b = []
result = []

for i in range(random.randint(6, 30)):
    a.append(random.randint(1, 10))

print(a)
for elem in a:
    count = 0
    for i in a:
        if elem == i:
            count += 1
    b.append(count)    # массив считает количество повторений для каждого элемента массива а

for i in range(len(b)):
    if b[i] == max(b):
        result.append(a[i])
        continue

print(f'{set(result)} - встречается чаще всего!')
