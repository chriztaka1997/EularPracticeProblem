################################
#
# Highly divisible triangular number
#
################################
# TODO: RuntimeError: Exceeded runtime
def problem12():
    
    def divisors(number):
        number_of_divisor = 0
        for i in range(1, number + 1):
            if number % i == 0:
                number_of_divisor += 1
        return number_of_divisor


    triangle_number = 1
    while divisors(triangle_number) <= 500:
        triangle_number += (triangle_number + 1)

    return triangle_number

print(problem12())
