class A:
    def __init__(self, dic={}):
        self._key = []
        self._val = []
        if dic != {}:
            for keys, values in dic.items():
                self._key.append(keys)
                self._val.append(values)
                
    def __repr__(self):
        dic = ""
        for i in range(len(self._key)):
            dic += "'{}': {}".format(self._key[i], self._val[i])
            if i != len(self._key) - 1:
                dic += ", "
        return "{" +  dic + "}"
    
    def __len__(self):
        return  len(self._key)
    
    def __getitem__(self, index):
        try:
            ind = self._key.index(index)
            return self._val[ind]
        except:
            return "Key doesn't exist!"
        
    def __setitem__(self, index, value):
        try:
            ind = self._key.index(index)
            self._val[ind] = value
        except:
            self._key.append(index)
            self._val.append(value)
        
    def __delitem__(self, index):
        try:
            ind = self._key.index(index)
            del(self._key[ind])
            del(self._val[ind])
        except:
            return "Key doesn't exist!"
        
    def __add__(self, other):
        if type(other) != A:
            print("Different type!")
            raise TypeError("unsupported operand type(s) for +: {} and {}".format(type(self), type(other)))
        else:
            new_A = A()
            new_A._key = self._key
            new_A._val = self._val
            for i in range(len(other)):
                new_A._key.append(other._key[i])
                new_A._val.append(other._val[i])
            return new_A
        
    def __contains__(self, value):
        for i in range(len(self._key)):
            if value == self._val[i]:
                return True
        return False
    
    def __iter__(self):
        return Iter(self._key)
        
    def keys(self):
        return self._key
    
    def values(self):
        return self._val
    
    def items(self):
        liste = []
        for i in range(len(self._key)):
            liste.append(("{}".format(self._key[i]), self._val[i]))
            #print(liste[i])
        return liste
    
    def sort(self):
        items = self.items()
        items.sort()
        self._key = []
        self._val = []
        for i in range(len(items)):
            self._key.append(items[i][0])
            self._val.append(items[i][1])
        return self
    
    def reverse(self):
        self._key.reverse()
        self._val.reverse()
        return self