# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def sumodd(array):
    l = len(array)
    count = 0
    for i in range(1, l, 2):
        count += array[i]
    return count


list = [2, 3, 5, 9, 3]
print(sumodd(list))
