

palindrome1 = 512343215
palindrome2 = 3841483
palindrome3 = 678929876
not_palindrome1 = 1234
not_palindrome2 = 4567634
not_palindrome3 = 678929476
not2 = -121
ispal = 121


# def check(pal, middle, left, right):
#     if left < middle:
#         left += 1
#         right -= 1
#         print(
#             f"Checking {pal[left]} on the left and {pal[right]} on the right")
#         return pal[left] == pal[right]


def is_pal(x):
    pal = str(x)
    middle_index = len(pal)//2
    left = 0
    right = -1
    bool_list = []

    while left < middle_index:
        print(
            f"Checking {pal[left]} on the left and {pal[right]} on the right")
        bool_list.append(pal[left] == pal[right])
        left += 1
        right -= 1

    print(bool_list)
    return all(bool_list)


# print(is_pal(palindrome1))
# print(is_pal(palindrome2))
# print(is_pal(not_palindrome1))
# print(is_pal(not_palindrome2))
# print(is_pal(not2))

# my_pal = [2, 4, 5, 8, 9]

# num = 1
# slice = my_pal[-3]
# print(slice)


def is_palindrome(x):

    # Edge cases: return false if the given number
    # 1)is negative
    # 2) ends in zero and is not 0
    if x < 0 or x % 10 == 0 and x != 0:
        return False

    reversed_num = 0

    while reversed_num < x:
        reversed_num = reversed_num * 10 + x % 10
        # First iteration: reversed_num = 0 * 10 + 121 % 10 -> 1
        # Second iteration: reversed_num = 1 * 10 + 12.1 % 10 -> 12.1

        print(reversed_num)
        x /= 10
        # First iteration: x = 121
        # Second iteration: x = 12.1
        # now reversed_num = x, so break out of while loop

    # now the original number is the same as the reversed number, so that means it is a palindrome
    # not sure if I understand the x == reversed_num/10
    return x == reversed_num or x == reversed_num/10


print(is_palindrome(121))
