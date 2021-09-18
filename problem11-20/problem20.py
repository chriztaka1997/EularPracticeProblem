##############################
#
# Factorial digit sum
#
##############################
import math


def problem20():
    ans_int = math.factorial(100)
    return sum(int(num) for num in str(ans_int))


print(problem20())
