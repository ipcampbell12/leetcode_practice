mint = 56789


def max_rot(n):
    mint_list = [*str(n)]

    left = mint_list.pop(0)
    mint_list.append(left)

    left1 = mint_list.pop(1)
    mint_list.append(left1)

    left2 = mint_list.pop(2)
    mint_list.append(left2)

    left3 = mint_list.pop(3)
    mint_list.append(left3)

    return int("".join(mint_list))


print(max_rot(mint))
