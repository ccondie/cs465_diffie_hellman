from math import floor


def modex(x, y, n):
    """
    :param x: the base
    :param y: the exponent
    :param n: the mod variable
    :return: x^y mod n
    """
    if y == 0:
        return 1

    z = modex(x, floor(y / 2), n)
    z2 = z * z
    z2_mod_n = z2 % n

    if y % 2 == 0:
        return z2_mod_n
    else:
        x_mod_n = x % n
        return (x_mod_n * z2_mod_n) % n
