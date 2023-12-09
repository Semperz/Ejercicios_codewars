#Given an array of ones and zeroes, convert the equivalent binary value to an integer.


def binary_array_to_number(numero):
    x = 0
    y = 0
    for i,valor in enumerate(numero[::-1]):
        y = (valor * 2 ** i)
        x = x + y
    return x