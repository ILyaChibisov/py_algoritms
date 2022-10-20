"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""
import random

a = []
b = []
result = []
for i in range(random.randint(10, 15)):
    a.append(random.randint(-10, 2))

print(a)

for i in a:
    if i < 0:
        b.append(i)

result = [i for i in range(len(a)) if a[i] == max(b)]
print(f'{max(b)} - максимальный элемент')
print(*result, sep=",", end=' ')
print('- индексы позиции в списке')

