# store linked list at every location
# multiple keys can share same hash value - O(n)

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        return sum([ord(char) for char in key]) % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False
        # check if key exists
        for idx, element in enumerate(self.arr[h]):
            # the condition checks if you already have that element
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            # if key does not exist at this index
            self.arr[h].append((key, val))

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
