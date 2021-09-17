###############################
#
# Power digit sum
#
###############################
def problem16():
    value_int = 2**1000
    list_int = [int(digit) for digit in str(value_int)]
    return sum(list_int)


print(problem16())
