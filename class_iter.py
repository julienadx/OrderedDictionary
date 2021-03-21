class Iter:
    def __init__(self, liste):
        self.liste = liste
        self.pos  = -1
        self.max = len(liste)-1
    def __next__(self):
        if self.pos == self.max:
            raise StopIteration
        self.pos += 1
        return self.liste[self.pos]