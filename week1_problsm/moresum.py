nums1 = [2, 7, 11, 15]
target1 = 9
# [0, 1]

nums2 = [3, 2, 4]
target2 = 6
# [1, 2 ]


nums3 = [3, 2, 8, 5, 3]
target3 = 6
# [0, 4]

nums4 = [5, 2, 8, 3, 4]
target4 = 11
# [2, 3]

nums5 = [4, 2, 2, 7, 8]
target5 = 4
# [1, 2]


nums6 = [2, 1, 5, 3]
target6 = 4
# [1, 3]


def two_sum_two_pass(arr, targ):
    hm = dict(zip([num for num in arr], list(range(len(arr)))))

    for num, index in enumerate(arr):
        comp = targ - num
        if comp in hm and comp != num:
            return [index, hm[comp]]


print(two_sum_two_pass(nums4, target4))


def two_sum(arr, targ):
    hm = {}

    indeces = []

    for index, num in enumerate(arr):
        if targ - num in hm:
            indeces.append(hm[targ-num])
            indeces.append(index)
            hm[num] = index
        else:
            hm[num] = index

    return indeces


def two_sum(arr, targ):
    hm = {}

    for index, num in enumerate(arr):
        diff = targ - num
        if diff in hm:
            return [hm[diff], index]
        hm[num] = index


# print(two_sum(nums1, target1))
# print(two_sum(nums2, target2))
# print(two_sum(nums3, target3))
# print(two_sum(nums4, target4))
# print(two_sum(nums5, target5))
# print(two_sum(nums6, target6))


# Conceptual break down
# value we are looking for is the difference between the target and the current value
# build a hashmap where key is index and value is elment - map each value to its index
# don't want to add everything to hash map at once
# problem with that: would check the same value you are checking  - > would have to compare index of current two with index of two that's in are hashamp


# clever way - hash map starts out as empty
# after visiting element, add it to the hash map
# do the same for next element, add element and index to hash map
# just need one pass
# when we visit first of summable elements, hashmap will only be porition of array we have visited already -values that came before first value
# once we arrive at second element that sums up to our target, we will have already visited the second element and it will be in our hashmap
