"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
если введено число 3486, то надо вывести число 6843."""

user_digit = int(input(" Введите натуральное число: "))
new_digit = 0

# тут не сильно мучался, получилось сразу)

while user_digit != 0:
    new_digit += user_digit % 10
    if user_digit // 10 != 0:
        new_digit *= 10
    user_digit //= 10

print(f'Новое число: {new_digit}')
