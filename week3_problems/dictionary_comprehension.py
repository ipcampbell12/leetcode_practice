import random
import string

# A can only go with T and C and only go with G

bases = ["A", "T", "C", "G"]

# k is the length
strand1 = random.choices(bases, k=10)

# dictionary of lists
dna = {key: [value, ("T" if value == "A" else "A" if value ==
                     "T" else"C" if value == "G" else "G")] for (key, value) in enumerate(strand1)}
# print(dna)


# list of dictionaries
keys = ["id", "username", "password"]
users = ["ipcampbell12", "bagunda123", "Yourmom345", "lesli345"]

data = [{key: (i if key == "id" else users[i] if key == "username" else "".join(random.choices(string.printable, k=8)))
         for key in keys} for i in range(len(users))]

# password = "".join(random.choices(string.printable, k=8))

# print(password)

print(data)


# dictionary comprehensions can become easily convoluted and difficult to read
