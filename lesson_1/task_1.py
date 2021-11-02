""" 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь."""

# выполнил без использование массивов)
# вводим переменные:
value = 0
count = 0

# делаем проверку ввода коректных значений пользователем
while count == 0:
    try:
        value = int(input('Введите трехзначное число: '))
        if 99 < value < 1000:
            count = 1
        else:
            print('Число должно быть трехзначным, повторите заново!')
    except ValueError:
        print('Неверно введены данные, повторите заново!')

# получаем цифру каждого разряда отдельно
digit_1 = value // 100
digit_2 = (value % 100) // 10
digit_3 = (value % 100) % 10

# выводим результаты вычислений:
print(f'Cумма цифр трехзначного числа: {digit_1 + digit_2 + digit_3}')
print(f'Произведение цифр трехзначного числа: {digit_1 * digit_2 * digit_3}')