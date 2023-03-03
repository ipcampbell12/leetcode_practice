nums1 = [2, 7, 11, 15]
target1 = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6

nums4 = [5, 2, 8, 3, 4]
target4 = 11


def two_sum(nums, targ):
    outer_start = 0
    outer_next = outer_start + 1

    while outer_next < len(nums):
        start = outer_start
        next = start + 1

        while next < len(nums):
            result = nums[start] + nums[next]

            print(f"{nums[start]} and {nums[next]} are equal to {result}")

            if result == targ:
                return [start, next]
            else:
                next += 1

        outer_start += 1


print(two_sum(nums4, target4))
