# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# - 45 -> 101101    3 -> 11        2 -> 10

def division_by_2(number):        # делим число на основание 2, добаваляем в строку
    if number == 0 or number == 1:
        return str(number)
    return str(number % 2) + division_by_2(number // 2)


def from_10_to_2(number):       # переворачиваем строку, переводим в целое
    return int((division_by_2(number))[::-1])

print(from_10_to_2(45))
print(from_10_to_2(3))
print(from_10_to_2(2))
