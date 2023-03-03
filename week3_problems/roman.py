test1 = "III"

test2 = "IV"

test3 = "VIII"

test4 = "XIV"

test5 = "CDXLIX"

test6 = "CCLIV"

# what I want

ready = ['CD', 'XL', "IX"]
nums = [400, 40, 9]


def romanToInt(roman):
    num_hash = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
                "LC": 90, "C": 100, "CD": 400, "D": 500,  "CM": 900, "M": 1000}

    numeral_string = roman
    counter = 0
    numeral_bits = []

    while counter < len(numeral_string):
        for num in num_hash.keys():
            index = numeral_string.find(num)
            if index != -1:
                numeral_bits.append(num)
                print(num)
                numeral_string = numeral_string[:index] + \
                    numeral_string[index+2:]

        counter += 1

    nums = []

    for num in list(set(numeral_bits)):
        nums.append(num_hash[num])

    return sum(nums)


print(romanToInt(test5))
