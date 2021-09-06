##################################
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#
##################################
def problem10():

    def is_prime(num):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        else:
            return False

    LIMIT = 2000000
    total = 0
    for i in range(2, LIMIT):
        if is_prime(i):
            total += i
    return total
