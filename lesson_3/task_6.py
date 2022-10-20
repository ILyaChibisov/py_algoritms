"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

import random

a = []
b = []
for i in range(random.randint(5, 15)):
    a.append(random.randint(0, 10))

if a.index(max(a)) > a.index(min(a)) + 1:
    step_1 = a.index(max(a))
    step_2 = a.index(min(a)) + 1
    b = a[step_2:step_1]
    print(f'Сумма элементов между максимальным и минимальным в массиве {a} равна {sum(b)}')

elif a.index(min(a)) > a.index(max(a)) + 1:
    step_1 = a.index(min(a))
    step_2 = a.index(max(a)) + 1
    b = a[step_2:step_1]
    print(f'Сумма элементов между максимальным и минимальным в массиве {a} равна {sum(b)}')

else:
    print(f'Сумма элементов между максимальным и минимальным в массиве {a} равна 0')
