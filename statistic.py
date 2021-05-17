from typing import List

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