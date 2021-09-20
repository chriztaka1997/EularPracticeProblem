##########################
#
# Non abundant Sum
#
##########################
# TOOO: Runtime exceeded, solution might be wrong
def problem23():

    def list_divisor(num):
        return_list = []
        for i in range(1, (num//2) + 1):
            if num % i == 0:
                return_list.append(i)
        return return_list


    def is_abundant(num):
        list_of_divisor = list_divisor(num)
        return True if sum(list_of_divisor) > num else False


    def is_two_abundant(num):
        for (i,x) in enumerate(list_of_abundant):
            for (j, y) in enumerate(list_of_abundant):
                if i != j and i+j == num:
                    return True
        return False

    upper_limit = 28123
    list_of_abundant = []
    list_of_non_abundant = []

    for num in range(1, upper_limit):
        if is_abundant(num):
            list_of_abundant.append(num)

            if not is_two_abundant(num):
                list_of_non_abundant.append(num)

        else:
            list_of_non_abundant.append(num)

    return sum(list_of_non_abundant)


# print(problem23())
print("Problem in progress")
