#################################
#
# Number Letter counts
#
#################################
def problem17():


    def number_naming(num):

        ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        if 0 <= num < 20:
            return ONES[num]
        
        elif 20 <= num < 100:
            return TENS[num // 10] + (ONES[num % 10] if (num % 10 != 0) else "")

        elif 100 <= num < 1000:
            return ONES[num // 100] + "hundred" + (("and" + number_naming(num % 100)) if (num % 100 != 0) else "")

        elif 1000 <= num < 1000000:
            return number_naming(num // 1000) + "thousand" + (number_naming(num % 1000) if (num % 1000 != 0) else "")

        else:
            raise ValueError()


    return sum(len(number_naming(i)) for i in range(1,1001))

print(problem17())
