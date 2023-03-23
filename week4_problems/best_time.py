# the problem is using 1 based indexing instead of 0 based indexing -> The index of the first element is 1 instead of 0

# you want to find the highest possible difference between 2 elements, but the lower element needs to be before the higher element

# DSA
# search

# need to increment both start and next
# not looking for lowest or highest
# def best_time(prices):

#     stack = []

#     start = 0
#     next = start + 1

#     while start < len(prices):
#         if next == len(prices):
#             stack.append(prices[start])
#         elif prices[start] < prices[next]:
#             print(f"start at {start} is {prices[start]}")
#             print(f"next at {next} is {prices[next]}")
#             stack.append(prices[start])

#         start += 1
#         next += 1

#     return stack


def best_time(prices):
    test = prices.copy()
    start = len(test)-1
    next = start - 1

    while start > 0:
        if start == 0:
            break
        elif test[start] < test[next]:
            test.pop(start)
        start -= 1
        next -= 1

    if len(test) <= 1:
        return 0

    # remove first element if higher than all the rest
    for price in prices:
        if prices[0] > price:
            prices.pop(0)

    for price in prices:
        if prices[-1] < price:
            prices.pop(-1)

    return max(prices) - min(prices)


input1 = [7, 1, 5, 3, 6, 4]
# all successive elements are higher
# should return 5

input2 = [7, 6, 4, 3, 1]
# all successive elements are lower
# should return 0

input3 = [4, 5, 2, 3, 9]
# should output 7

input4 = [2, 4, 7, 8, 9]
# should output 7

input5 = [2, 9, 7, 3, 4]
# should output 7

input6 = [2, 4, 1]
# should return 2

print(best_time(input6))


def check_if_less(prices):
    start = len(prices)-1
    next = start - 1

    while start > 0:
        if start == 0:
            break
        elif prices[start] < prices[next]:
            print(prices[start])
            prices.pop(start)
        start -= 1
        next -= 1

    return len(prices)


# input2 = [7, 6, 4, 3, 1]
# print(check_if_less(input2))
