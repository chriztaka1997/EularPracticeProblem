#######################
#
# Reciprocal cycles
#
#######################
def problem26(denum):
    
    def reciprocal_cycles(num):

        seen = {}
        x = 1
        while (x % num not in seen) and (x % num != 0):
            seen[x % num] = True
            x = x * 10

        return len(seen)

    num_fraction_list = []
    for i in range(1, denum):
        num_fraction_list.append(reciprocal_cycles(i))

    return num_fraction_list.index(max(num_fraction_list)) + 1


print(problem26(1000))
