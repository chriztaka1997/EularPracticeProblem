#############################
#
# Amicable numbers
#
#############################
# TODO: still not finish, have not understand the problem
def problem21():

    def list_of_div(num):
        return [i for i in range(1, num//2 + 1) if num % i == 0]

    first_number = sum(list_of_div(10000))
    second_number = sum(list_of_div(first_number))
    return first_number + second_number if first_number != second_number else 0


print("This problem is in progress")
# print(problem21())
