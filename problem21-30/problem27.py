#############################
#
# Quadratic primes
#
#############################
def problem27():

    def is_prime(num):

        if num <= 1:
            return False

        for i in range(2, int(num / 2) + 1):

            if num % i == 0:
                return False

        return True


    def quadratic_formula(a, b, x):
        return x**2 + a * x + b


    def consecutive_prime(a, b):
        start = 0
        num = quadratic_formula(a, b, start)
        while is_prime(num):
            start += 1
            num = quadratic_formula(a, b, start)
        return start
    
    max_combination = [0,0]
    max_consecutive = 0
    for a in range(-999, 1000):
        for b in range(2, 1000):
            current_consecutive = consecutive_prime(a, b)
            if current_consecutive > max_consecutive:
                max_combination[0] = a
                max_combination[1] = b
                max_consecutive = current_consecutive

    return max_combination[0] * max_combination[1]


print(problem27())
