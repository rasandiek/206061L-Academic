class Pair:
    def __init__(self, k, val):
        self.key = k
        self.value = val


# Creating the HashTable class
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Creating the insert/ add function
    def insert(self, k, val):
        h = hash(k)
        p = h % self.size

        if self.table[p] is None:
            self.table[p] = (k, val)
        else:
            pass

    # Creating the search function
    def search(self, k):
        h = hash(k)
        p = h % self.size

        if self.table[p] is None:
            return False
        elif self.table[p][0] == k:
            return self.table[p][1]

        else:
            return False


t = HashTable(20)
t.insert('206061', 'Rasandie')
t.insert('206014', 'Radeesh')
t.insert('206123', 'Pabodini')
t.insert('206088', 'Vihanga')
t.insert('206050', 'Nuwanga')

result = t.search('206014')
if result is False:
    print("Key not Found")
    print("Try Again")
    print("On Repeat")
else:
    print(result)