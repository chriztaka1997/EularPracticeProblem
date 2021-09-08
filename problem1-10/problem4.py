#####################################
#
# Largest palindrome product
#
#####################################
def problem4():

    def isPalindrome(num ):
        return num == num[::-1]

    max_num = [0, 0]
    max_pal = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(str(i*j)):
                if max(i*j, max_pal) == i*j:
                    max_pal = i*j
                    max_num[0] = i
                    max_num[1] = j
    return max_pal

print(problem4())
