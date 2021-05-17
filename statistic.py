from typing import List
from collections import Counter


Vector = List[float]


def _median_odd(xs: Vector) -> float:
    """ if len(xs) is odd, the median is the middle item"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: Vector) -> float:
    """if len(xs) is even its the average of the middle two elements"""

    sorted_xs = sorted(xs)
    mid = len(xs) // 2
    return (sorted_xs[mid -1] + sorted_xs[mid]) / 2

def median(v: Vector) -> float:
    """finds the middle-most value """

    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


assert median([1,10,2,9,5]) == 5
assert median([1,7,8,10]) == (7+8) / 2

def quantile(xs: Vector, p: float) -> float:
    """returns the pth-percentle"""
    p_index = int(p * len(xs))

    return sorted(xs)[p_index]
grades = [95,80, 75,62,62]


assert quantile(grades, 0.10) == 62
assert quantile(grades, 0.25) == 62
assert quantile(grades, 0.75) == 80
assert quantile(grades, 0.90) == 95


def mode (xs: Vector) -> Vector:
    """returns vector(list) of most common"""

    counts = Counter(xs)

    m_count = max(counts.values())

    return [xs_i for xs_i, count in counts.items() if count == m_count]


assert mode(grades) == [62]

def dat_range(xs: Vector) -> float:

    return max(xs) - min(xs)

assert dat_range(grades) == 33