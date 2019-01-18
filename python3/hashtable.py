

class HashTable:
    """ A minimal hash table implementation.

        Usage:

        h = HashTable(10)
        h.set('a', 1)
        h.set('b', 2)
        h.get('a')
        1
        str(h)
        '{a:1, b:2}'
    """

    def __init__(self, capacity=100):
        self.table = [[] for x in range(capacity)]
        self.load_factor = 0.75
        self.size = 0


    def get(self, key):
        def find_return(slot, i):
            return self.table[slot][i][1]

        return self.__find_by_key(key, find_return)


    def set(self, key, val):
        self.table[self.__hash(key)].append((key, val))
        self.size += 1

        if float(self.size) / len(self.table) >= self.load_factor:
            self.__resize_table()


    def delete(self, key):
        def find_return(slot, i):
            del self.table[slot][i]
            self.size -= 1

        self.__find_by_key(key, find_return)


    def __find_by_key(self, key, find_return):
        slot = self.__hash(key)

        if not self.table[slot]:
            raise KeyError(f"Key {key} does not exist")

        for i, v in enumerate(self.table[slot]):
            if v[0] == key:
                return find_return(slot, i)


    def __hash(self, key):
        return hash(key) % len(self.table)


    def __resize_table(self):
        self.table.extend([[] for x in range(len(self.table) * 2)])


    def __getitem__(self, key):
        return self.get(key)


    def __setitem__(self, key, val):
        self.set(key, val)


    def __delitem__(self, key):
        return self.delete(key)


    def __repr__(self):
        els = []

        for slot in self.table:
            for i in slot:
                els.append(':'.join(str(x) for x in i))

        return '{' + ', '.join(els) + '}'
