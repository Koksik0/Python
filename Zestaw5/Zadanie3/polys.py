def add_poly(poly1, poly2) -> list:
    """
    :return: poly1 + poly2
    """
    length1 = len(poly1)
    length2 = len(poly2)
    max_length = max(length1, length2)
    result = []
    for x in range(max_length):
        wsp1 = poly1[x] if x < length1 else 0
        wsp2 = poly2[x] if x < length2 else 0
        result.append(wsp1 + wsp2)
    return result


def sub_poly(poly1, poly2) -> list:
    """
    :return: poly1 - poly2
    """
    len1, len2 = len(poly1), len(poly2)
    max_len = max(len1, len2)
    result = [0] * max_len

    for i in range(len1):
        result[i] += poly1[i]
    for i in range(len2):
        result[i] -= poly2[i]

    return result


def mul_poly(poly1, poly2):
    """
    :return: poly1 * poly2
    """
    result = [0] * (len(poly1) + len(poly2) - 1)
    for x in range(len(poly1)):
        for y in range(len(poly2)):
            result[x + y] += poly1[x] * poly2[y]
    return result


def is_zero(poly) -> bool:
    """
    :return: True if all coefficients of the polynomial are zero
    """
    result = True
    for x in poly:
        if x != 0:
            return False
    return result


def eq_poly(poly1, poly2) -> bool:
    """
    :return: True if poly1 == poly2
    """
    if len(poly1) != len(poly2):
        return False
    for x in range(poly1):
        if poly1[x] != poly2[x]:
            return False
    return True


def eval_poly(poly, x0) -> float:
    """
    :return: Value of the polynomial at point x
    """
    result = 0
    for coefficient in reversed(poly):
        result = result * x0 + coefficient
    return result


def combine_poly(poly1, poly2) -> list:
    """
    :return: poly1(poly2)
    """
    temp = []
    for x in range(1, len(poly1)):
        if poly1[x] != 0:
            temp2 = pow_poly(poly2, x)
            temp2 = [y * poly1[x] for y in temp2]
            temp.append(temp2)
        else:
            temp.append([0])
    result = temp[0]
    for x in range(1, len(temp)):
        result = add_poly(result, temp[x])
    result[0] += poly1[0]
    return result


def pow_poly(poly, n) -> list:
    """
    :return: poly^n
    """
    temp = poly
    for x in range(n - 1):
        temp = mul_poly(temp, poly)
    return temp


def diff_poly(poly) -> list:
    """
    :return: d/dx(poly)
    """
    result = [poly[1]]
    for x in range(2, len(poly)):
        if poly[x] != 0:
            result.append(poly[x] * x)
        else:
            result.append(0)
    return result
