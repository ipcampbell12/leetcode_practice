from itertools import permutations

nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 2, 8, 5, 3]
target3 = 6

nums4 = [5, 2, 8, 3, 4]
target4 = 11

nums5 = [4, 2, 2, 7, 8]
target5 = 4


def two_sum(nums, targ):
    for perm in permutations(nums, 2):
        if sum(perm) == targ:
            (a, b) = perm
            idx_a = nums.index(a)
            idx_b = nums.index(b)
            if idx_a == idx_b:
                idx_b = nums.index(b, idx_a+1)
            return [idx_a, idx_b]


print(two_sum(nums4, target4))
print(two_sum(nums5, target5))
print(two_sum(nums3, target3))
print(two_sum(nums2, target2))
print(two_sum(nums1, target1))
