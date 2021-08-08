from math import sqrt


def next_iteration(z: complex, c: complex) -> complex:
    return z ** 2 + c


def distance_between(a: complex, b: complex) -> float:
    real_distance = a.real - b.real
    imaginary_distance = a.imag - b.imag
    return sqrt(real_distance ** 2 + imaginary_distance ** 2)


def _stability(z: complex, c: complex, count: int) -> int:
    z_next = next_iteration(z, c)
    distance = distance_between(z_next, z)
    if count == 200 or distance > 2:
        return count

    return _stability(z_next, c, count + 1)


def stability(z: complex) -> int:
    return _stability(0, z, 0)
