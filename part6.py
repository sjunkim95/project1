class PeekableIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        # if self.counter >= len(self.iterable):
        if self.counter >= self.iterable:
            raise StopIteration
        else:
            self.counter += 1
            return self.counter
        #  return self.iterable[self.counter]

    def peek(self):
        #return self.iterable[self.counter+1]
        return self.counter

    def has_next(self):
        #if self.counter >= len(self.iterable):
        if self.counter >= self.iterable:
            return False
        else:
            return True

#if __name__ == '__main__':
# run = PeekableIterator([1, 2, 3, 4, 5, 6, 7])
#print(run.has_next())
