#####################################
# IN PROGRESS
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
#####################################
def problem3(num):
    def is_prime(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True
        else:
            return False
    largest = 0
    for i in range(1, int(num**0.5)):
        if num % i == 0:
            if is_prime(i): largest = i
    return largest
