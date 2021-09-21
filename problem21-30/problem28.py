################################
#
# Number Spiral Diagonals
#
################################
from sys import argv


def problem28(size):

    sum_of_diag = 1
    sum_of_diag += sum(4 * i**2 - 6 * (i -1) for i in range(3, size + 1, 2))
    return sum_of_diag


# print(problem28(int(argv[1])))
print(problem28(1001))
