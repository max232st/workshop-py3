# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = int(input('Введите число: '))

string = ''
while num != 0:
    left = num % 2
    string = str(left) + string
    num //= 2

print(f'Число в двоичной системе =  {string}')
