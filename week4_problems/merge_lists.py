list1 = [1, 2, 4]
list2 = [1, 3, 4]


def mergeTwoLists(l1, l2):
    return sorted(l1 + l2)


print(mergeTwoLists(list1, list2))
