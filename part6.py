class PeekableIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.iterable:
            raise StopIteration
        else:
            self.counter += 1
            return self.iterable[self.counter]


        
    def peek(self):
        pass
        
    def has_next(self):
        pass

