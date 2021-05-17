from typing import List, Tuple, Callable
import math
from vectors import Vector

Vector = List[float]
Matrix = List[List[float]]


def shape(A: Matrix) -> Tuple[int, int]:
    """Returns (rows of A, collumns of A)"""

    num_rows = len(A)
    num_cols = len(A[0]) # elements in first row

    return num_rows, num_cols

assert shape([[1,2,3],[4,5,6]]) == (2,3)

def get_row(A: Matrix, i: int) -> Vector:
    """ returns the i-th row of A (as a vector)"""
    return A[i]

def get_col(A: Matrix, j: int) -> Vector:
    """ Return the j-th collumn of A as a vector"""
    return [a[j] for a in A]

assert get_col([[1,2,3],[4,5,6]], 2) == [3,6]


def make_matrix(n_rows: int, n_cols: int, fn: Callable[[int, int], float])-> Matrix:
    """Returns a num_rows x num_cols matrix
       whose (i,j)-th entry is entry_fn(i, j)"""
    return [[fn(i, j)
             for j in range(n_cols)] 
                for i in range(n_rows)]


def identity_matrix(n: int) -> Matrix:
    """ Returs n x n identity matrix """ 
    return make_matrix(n,n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(5) == [
                                [1, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 1, 0],
                                [0, 0, 0, 0, 1]
                            ]
