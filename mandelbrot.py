from math import sqrt
from typing import List

import numpy as np
from nptyping import ndarray

BLACK = [0, 0, 0]
DARK_BLUE = [37, 91, 148]
LIGHT_BLUE = [45, 132, 224]
YELLOW = [224, 192, 33]
DARK_PURPLE = [90, 7, 148]
LIGHT_PURPLE = [141, 22, 224]


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


def make_pixels(stability_counts: List[int]) -> ndarray:
    return np.array([stability_to_rgb(s) for s in stability_counts], dtype=np.uint8)


def stability_to_rgb(s: int) -> ndarray:
    if s == 200:
        return BLACK
    elif s > 100:
        return LIGHT_PURPLE
    elif s > 50:
        return DARK_PURPLE
    elif s > 23:
        return LIGHT_BLUE
    elif s > 3:
        return YELLOW
    else:
        return DARK_BLUE
