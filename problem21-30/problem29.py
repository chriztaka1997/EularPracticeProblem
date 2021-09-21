############################
#
# Distinct powers
#
############################
from sys import argv


def problem29(upper_limit):

    distinct_result = []
    for a in range(2, upper_limit + 1):
        for b in range(2, upper_limit + 1):
            distinct_result.append(a**b)

    return len(set(distinct_result))


# print(problem29(int(argv[1])))
print(problem29(100))
