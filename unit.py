import math
from random import expovariate


def exp(mat):
    return math.ceil(expovariate(1 / mat) * 60)
