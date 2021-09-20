#############################
#
# Amicable numbers
#
#############################
# TODO: Wrong answer
def problem21():

    def list_of_div(num):
        return [i for i in range(1, num//2 + 1) if num % i == 0]

    def is_amicable(num):
        first_number = sum(list_of_div(num))
        second_number = sum(list_of_div(first_number))
        return first_number + second_number if first_number != second_number else 0
    
    return_value = 0
    for i in range(1, 10000):
        return_value += is_amicable(i)

    return return_value

print("This problem is in progress")
# print(problem21())
