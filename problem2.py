#####################################
#
# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.
#
#####################################
def problem2():

    def switch(a, b):
        return b, a+b

    total = 2
    last_two = 1
    last_one = 2
    while last_one < 4000000:
        if (last_one+last_two) % 2 == 0:
            total += last_one+last_two
        last_two, last_one = switch(last_two, last_one)
    return total
