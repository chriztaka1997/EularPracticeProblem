################################
#
# Longest Collatz sequence
#
################################
#TODO: Runtime Exceeded
def problem14():

    def collatz(num):
        copy_num = num
        list_of_collatz = [num]
        while copy_num != 1:
            if copy_num % 2 == 0:
                copy_num /= 2
            else:
                copy_num = 3 * copy_num + 1
            
            list_of_collatz.append(copy_num)

        return len(list_of_collatz)

    max_num_sequence = 0
    for number in range(1000000):
        max_num_sequence = max(max_num_sequence, collatz(number))
    
    return max_num_sequence

print(problem14())
