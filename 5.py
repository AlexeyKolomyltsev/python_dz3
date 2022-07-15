# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fib_positive(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    return fib_positive(n-1) + fib_positive(n-2)


def fib(n):
    fib_array = []
    for i in range(-n, n + 1):
        if i < 0:
            fib_array.append(round((-1)**(i+1) * fib_positive(-i)))
        # elif i == 0:
        #     fib_array.append(0)
        else:
            fib_array.append(fib_positive(i))
    return(fib_array)


print(fib(10))
