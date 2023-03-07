input1 = "()"
# good

input2 = "()[]{}"

input3 = "(]"
# good

input4 = "([)]"
# good

input5 = "([])"
# good

input6 = "{()[]}"


reversed = ")][("


def is_valid(s):
    hm = {"(": ")", "{": "}", "[": "]", ")": "(", "}": "{", "]": "["}

    # make sure opposite parenthese can be found in the s
    for char in s:
        if hm.get(char, 0) not in s:
            return False

    # check if they are in order
    reversed = [hm.get(char) for char in s[::-1]]

    return "".join(reversed) == s


# print(is_valid(reversed))

input7 = "{([)]}"
# good


def is_valid2(s):
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]

    hm = {}

    for char in s:
        if char in opening:
            hm[char] = ("o", opening.index(char))
        else:
            hm[char] = ("c", closing.index(char))

    order = [hm[deal][1] for deal in hm]

    return order


# print(is_valid2(input2))

# can't start with a closing bracket, have to start with opening parentheses

# remove parens from list as they are closed - want to end up with an empty list

# removing from top of the list - sounds like a stack

# closing parentheses always matched to the most recent opening parentheses

# stack plus hashmap


valid = "([])"

invalid = "{([)]}"

more_invalid = "([)]"

more_valid = "()[]{}"


def is_valid3(s):
    hm = {")": "(", "}": "{", "]": "["}

    stack = []

    for char in s:
        if char in hm:
            if stack and stack[-1] == hm[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return True if not stack else False


print(is_valid3(valid))
print(is_valid3(more_valid))
print(is_valid3(more_invalid))
print(is_valid3(invalid))
