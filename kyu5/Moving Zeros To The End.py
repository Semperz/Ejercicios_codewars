#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


def move_zeros(lst):
    for valor in lst:
        if valor == 0:
            lst.remove(0)
            lst.append(0)
    return lst