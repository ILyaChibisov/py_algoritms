"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
сумму его цифр."""

import random

# генерируем список натуральных чисел 5-20 штук
n = random.randint(5, 20)
a = []

for i in range(n - 1):
    a.append(random.randint(0, 1000))

print(f'Наша последовательность чисел: {" ".join(map(str, a))}')


def sum_digit(digit):
    """
    Подсчёт суммы цифр числа
    """
    count = 0
    while digit != 0:
        if digit // 10 != 0:
            count += digit % 10
            digit //= 10
            if digit // 10 == 0:
                count += digit % 10
                break
    return count


our_digit = a[0]
sum_our_digit = sum_digit(a[0])

for i in range(n-1):
    if sum_digit(a[i]) > sum_our_digit:
        our_digit = a[i]
        sum_our_digit = sum_digit(a[i])
    else:
        pass

print(f'Искмое число: {our_digit} сумма его цифр: {sum_our_digit}')
