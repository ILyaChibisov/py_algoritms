"""1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до
9. """

result = []
for i in range(2, 10):
    count = 0
    for j in range(2, 100):
        if j % i == 0:
            count += 1
    result.append(count)

# выводим результаты:
for i in range(2, 10):
    print(f'{result[i-2]} чисел делятся на {i}')