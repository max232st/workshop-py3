# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

userList = list(map(int, input('Введите числа списка через пробел: ').split()))
print(f'Cписок: {userList}')

sumListNum = 0

for i in range(1, len(userList), 2):
    sumListNum = sumListNum + userList[i]

print(f'Сумма элементов на нечетных позициях: {sumListNum}')
