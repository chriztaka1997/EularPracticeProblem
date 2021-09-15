####################################
#
# Lattice paths
#
####################################
import math


def problem15():
    grid_size = 20
    return math.factorial(2 * grid_size)/math.factorial(grid_size)**2


print(problem15())
