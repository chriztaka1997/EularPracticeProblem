#############################
#
# Lexicographic permutations
#
#############################
import itertools


def problem24(word, nth):
    ans = itertools.permutations(word, len(word))

    ans = ["".join(char) for char in ans]

    return sorted(ans)[nth - 1]


print(problem24("0123456789", 1000000))
