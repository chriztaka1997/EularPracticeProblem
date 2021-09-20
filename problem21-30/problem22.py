######################
#
# Names Scores
#
######################
def problem22():

    with open('p022_names.txt','r') as file:
        names = file.readlines()

    names = names[0].replace("'", "")
    names = names.split(",")

    ans = sum((i + 1) * (ord(char) - ord('A') + 1)
            for (i, name) in enumerate(sorted(names))
            for char in name.replace('"', ''))
    return ans


print(problem22())
