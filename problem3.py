#####################################
# IN PROGRESS
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
#####################################
def problem3(num):
    largest = 0
    for i in range(1, int(num**0.5)):
        if num % i == 0:
            largest = i
    return largest
