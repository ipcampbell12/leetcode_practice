dict1 = {"a": 2, "b": 5, "c": 6, "d": 7}
dict2 = {"a": 2, "b": 5, "c": 6, "t": 1}


def check_if_same(input1, input2):
    for char in input1:
        if input1[char] != input2.get(char, 0):
            return False

    return True


print(check_if_same(dict1, dict2))

# if input1[char] != input2[char]:
#KeyError: 'd'
