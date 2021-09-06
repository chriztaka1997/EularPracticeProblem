###############################
#
# Special Pythagorean triplet
#
###############################
def problem9(num):
    for a in range(1, num//2):
        for b in range(1, num//2):
            c = a**2 + b**2
            if a**2 + b**2 == c and a + b + c**0.5 == num:
                return int(a*b*(c**0.5))
