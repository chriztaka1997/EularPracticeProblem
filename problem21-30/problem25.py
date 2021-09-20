########################
#
# 1000-digit Fibonacci number
#
#############################
def problem25(digit):
    
    fib = [1,1]
    index = 2
    while len(str(fib[-1])) < digit:
        fib.append(fib[0] + fib[1])
        fib.pop(0)
        index += 1

    return index


print(problem25(1000))
