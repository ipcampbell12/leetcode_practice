string1 = "a gentleman"
string2 = "elegant man"


string3 = "bored"
string4 = "robed"

string5 = "peach"
string6 = "cheap"

string7 = "rat"
string8 = "car"

string9 = "anagram"
string10 = "nagaram"
# my solutions


def isAnagram(input1, input2):

    input1_arr = sorted([char for char in input1])
    input2_arr = sorted([char for char in input2])

    return input1_arr == input2_arr


# print(isAnagram(string7, string8))

# solution using hashmaps


def isAnagram2(input1, input2):

    if len(input1) != len(input2):
        return False

    chars = sorted(list(set([*input1])))
    counts = [input1.count(char) for char in chars]
    hm = dict(zip(chars, counts))

    chars1 = sorted(list(set([*input2])))
    counts1 = [input2.count(char) for char in chars]
    hm1 = dict(zip(chars1, counts1))

    compas = []

    for char in hm.keys():
        if input1.count(char) == input2.count(char):
            compas.append(True)
        else:
            compas.append(False)

    return all(compas)


# print(isAnagram2(string7, string8))


# just iteratre though keys of one


# official solution

def isAnagram3(input1, input2):

    # check to make sure they are the same length
    if len(input1) != len(input2):
        return False

    # start with empty hasmaps
    countS, countT = {}, {}

    for i in range(len(input1)):
        countS[input1[i]] = 1 + countS.get(input1[i], 0)
        countT[input2[i]] = 1 + countT.get(input2[i], 0)

    for c in countS:
        if countS[c] != countT(c, 0):
            return False

    # if loo
    return True


print(isAnagram2(string9, string10))

# .get has default value of 0
# use .get incase it doesn't exist
