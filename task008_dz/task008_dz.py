# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(my_list)
listNew = []

for item in my_list:
    listNew.append(round(item % 1, 3))
    for item in listNew:
        if item == 0:
            listNew.remove(0)
print(max(listNew) - min(listNew))
