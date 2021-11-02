"""6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

number_letter = int(input("Введите номер буквы от a до z: "))

if number_letter in range(ord("z") - ord("a") - 1):
    print(chr(ord("a") + number_letter - 1))
else:
    print('Введен неправильный номер!')
