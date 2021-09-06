###########################
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
###########################
def problem7(num):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        else:
            return False

    if num == 1:
        return 2
    if num == 2:
        return 3
    num_of_prime = 2
    current_int = 4
    while num_of_prime != num:
        if is_prime(current_int):
            num_of_prime += 1
        current_int += 1
    return current_int - 1
