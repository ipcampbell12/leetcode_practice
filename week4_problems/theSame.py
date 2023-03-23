import math
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

c = [121, 144, 19, 161, 19, 144, 19, 11]
d = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]

e = [76, 46, 48, 58, 96, 69, 91, 45, 51, 84, 23, 63, 24, 35]
f = [3364, 3969, 2025, 2601, 5784, 8281, 576,
     529, 2116, 9216, 4761, 1225, 2304, 7056]


def comp(array1, array2):

    if array1 == None or array2 == None:
        return False

    if len(array1) != len(array2):
        return False

    arr1 = sorted([abs(num) for num in array1])
    test_arr = [int(math.sqrt(num)) for num in sorted(array2)]

    return test_arr == arr1


print(comp(e, f))
