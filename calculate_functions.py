from scipy.integrate import quad
from numpy import sqrt


def prepare(value: str) -> str:
    return value.replace(',', '.') if ',' in value else value


def func(z: float, r: float, h: float) -> float:
    return sqrt(z * (2 * r - z)) / sqrt(z + h)


def calc(r: float, h: float) -> float:
    return quad(func, 0, 2 * r, args=(r, h))[0]

