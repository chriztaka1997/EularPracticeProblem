#############################
#
# Digit Fifth Power
#
#############################
def problem30():
    
    def digit_power(num):
        return sum(int(digit)**5 for digit in str(num))

    return sum(i for i in range(2, 1000000) if i == digit_power(i))


print(problem30())
