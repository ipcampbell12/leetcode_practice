# dictionary memory storage
# maps key to element in list- use hash function to get index of that elmenent
# hash function converts key into index in the array
# string index instead of integer index
# dictionaryis python speciifc implementation of has tables
# hash function
# uses ascii letters - find ascii value for each letter in word
# divide sum of ascii values for letters by size of array with mod operation

# look up by key is O(1) and so is insertion/deletion - average complexity

# hash function
def get_hash(key):
    return sum([ord(char) for char in key]) % 100


# print(get_hash('march 6'))

# hash class


class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        return sum([ord(char) for char in key]) % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


hm = HashTable()
hm['march 6'] = 130

print(hm['march 6'])

del hm['march 6']
print(hm['march 6'])
