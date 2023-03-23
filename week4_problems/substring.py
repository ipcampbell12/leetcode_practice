mystr = 'AABBBAB'


def getMinLegnth(seq):
    hm = {"AB", "BB"}

    stack = []

    for index, char in enumerate(seq):
        stack.append(char)
        if index + 1 == len(seq):
            break
        else:
            combo = char + seq[index+1]
            if char and seq[index+1] in stack and combo in hm:
                stack.remove(char)
                stack.remove(seq[index+1])

    return stack


    # abbab
print(getMinLegnth(mystr))

# test = "aabbbab"
# print(test[0:1])
