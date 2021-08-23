#####################################
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#
#####################################
def problem4():

    def isPalindrome(num: str):
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
