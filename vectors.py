from typing import List, ValuesView
import math

Vector = List[float]

# vector arithmetics

# check if two vectors are equal
def two_vector_eq(v: Vector, w: Vector) -> AssertionError:
    """Checks if two vectors are equal"""
    assert len(v) == len(w), "vectors not equal"

 # check if all vectors in a list are equal       
def list_vector_eq(v: List[Vector], n_ellements:int ) -> AssertionError:
    """check if all vectors in a list are equal"""
    # n_ellements = len(v[0])
    assert all(len(w) == n_ellements for w in v), "list of vectors not equal"


# vector addition
def add(v: Vector, w: Vector) -> Vector:
    """Adds two vectors component wise [v_1+w_1,...,v_n+w_n]"""
    two_vector_eq(v,w)
    return [v_i + w_i for v_i, w_i in zip(v,w)]


assert add([1,2,3], [1,2,3]) == [2,4,6]

# vector subtraction
def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts two vectors component wise [v_1-w_1,...,v_n-w_n]"""

    two_vector_eq(v,w)

    return [v_i - w_i for v_i, w_i in zip(v,w)]

assert subtract([2,4,6], [1,2,3]) == [1,2,3]


# add a list of same size vectors
def vector_sum(vectors: List[Vector]) -> Vector:

    #chek if vector not empty
    assert vectors, "no vector privided"

    n_ellements = len(vectors[0])
    list_vector_eq(vectors, n_ellements)
    
    return[sum(vector[i] for vector in vectors) for i in range(n_ellements)]

assert vector_sum([[1,2],[3,4],[5,6],[7,8]]) == [16,20]

def scalar_mult(v:Vector, c:float) -> Vector:
    assert v, "No vector supplied"

    return [c * v_i for v_i in v]

assert scalar_mult([1,2,3], 2.0) == [2,4,6]

def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)

    return scalar_mult(vector_sum(vectors), 1/n)

assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]

def dot(v: Vector, w: Vector):
    """v_1 * w_1 + .... + v_n * v_n"""
    two_vector_eq(v,w)

    return sum(v_i * w_i for v_i, w_i in zip(v,w))


assert dot([1,2,3],[4,5,6]) == 32 # 1 * 4 + 2 * 5 + 3 * 6

# -------------------------------------------------------
# written so i could understand sum of squares , dot , distance and magnitude
def square_vector(v: Vector) -> Vector:
    """returns square of each element [v_1*v_1, v_2*v_2]"""
    assert v, "No vector supplied"

    return [i * i for i in v]

assert square_vector([2,3]) == [4,9]
# ----------------------------------------------------

def sum_of_squares(v: Vector) -> float:
    """Returns v_1 * v_1 + ... + v_n * v_n"""
    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14 # 1*1 + 2*2 + 3*3


def magnitude(v: Vector) -> float:
    """returns magnitude of v"""

    return math.sqrt(sum_of_squares(v))


assert magnitude([3,4]) == 5

# --------------------------------------------------
#long method
def squared_distance(v: Vector, w: Vector) -> float:
    """Computes (v_1 - w_1)**2+ ... (v_n -w_n)**2"""
    return sum_of_squares(subtract(v, w))

def vector_distance(v: Vector, w: Vector)-> float:
    return math.sqrt(squared_distance(v, w))

# ----------------------------------------------------


def distance(v: Vector, w: Vector) -> float:
    return magnitude(subtract(v,w))