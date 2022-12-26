# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

num = input("Задайте список из нескольких чисел через пробел:   ").split()
print(num)
result = []
for i in range((len(num)+1)//2):
    result.append(int(num[i])*int(num[-(i+1)]))
print(f'Произведение пар чисел списка: {result}')
