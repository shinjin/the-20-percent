

class HashTable:
    def __init__(self):
        self.table = [[] for x in range(10)]
        self.load_factor = 0.75
        self.size = 0


    def get(self, key):
        def find_return(i1, i2):
            return self.table[i1][i2][1]

        return self.__find_by_key(key, find_return)


    def set(self, key, val):
        self.table[self.__hash(key)].append((key, val))
        self.size += 1

        # if float(self.size) / len(self.table) >= self.load_factor:
        #     self.__resize_table()


    def delete(self, key):
        def find_return(i1, i2):
            del self.table[i1][i2]
            self.size += 1

        self.__find_by_key(key, find_return)


    def __find_by_key(self, key, find_return):
        hkey = self.__hash(key)

        if not self.table[hkey]:
            raise KeyError(f"Key {key} does not exist")

        for i, v in enumerate(self.table[hkey]):
            if v[0] == key:
                return find_return(hkey, i)


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

        for i in self.table:
            for j in i:
                els.append(':'.join(str(x) for x in j))

        return '{' + ', '.join(els) + '}'
