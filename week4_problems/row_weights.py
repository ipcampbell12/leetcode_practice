
test1 = [13, 27, 49]

test2 = [50, 60, 70, 80]

test3 = [70, 58, 75, 34, 91]


def rowWeights(arr):
    evens = [num for index, num in enumerate(arr) if index % 2 == 0]

    odds = [num for index, num in enumerate(arr) if index % 2 != 0]

    return (sum(evens), sum(odds))


print(rowWeights(test1))


# even index go in one
# odd index go in the other one
