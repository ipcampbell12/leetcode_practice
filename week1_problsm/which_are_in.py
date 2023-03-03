a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']


def in_array(array1, array2):

    shared = []

    counter = 0

    while counter < len(array1):
        for word in array2:
            check = array1[counter]
            if word.find(check) != -1:
                shared.append(check)

        counter += 1

    return sorted(list(set(shared)))


print(in_array(a1, a2))
