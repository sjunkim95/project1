class PeekableIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.counter
        if self.counter >= len(self.iterable):
       # if self.counter >= self.iterable:
            raise StopIteration
        else:
            self.counter += 1
           # return self.counter
            return self.iterable[self.index]

    def peek(self):
        #return self.iterable[self.counter+1]
        if self.counter >= len(self.iterable):
           # return self.counter
           return self.iterable[self.counter + 1]
        else:
            raise StopIteration("Index is out of range")

    def has_next(self):
        #if self.counter >= len(self.iterable):
        if self.counter >= len(self.iterable):
            return False
        else:
            return True

if __name__ == '__main__':
     run = PeekableIterator([1,2,3,4,5,6])

     for i in run:
         print(i)
         print(run.has_next())

     #print("peek는", run.peek())





