'''
Iterator objects in python conform to the iterator protocol, 
which basically means they provide two methods: __iter__() and next(). 
The __iter__ returns the iterator object and is implicitly called at the start of loops. 
The next() method returns the next value and is implicitly called at each loop increment. 
next() raises a StopIteration exception when there are no more value to return, 
which is implicitly captured by looping constructs to stop iterating
'''

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

# the __iter__ always returns back 'self'
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def Main():
    rev = Reverse('Rabinovitch')
    for char in rev:
        print (char)

if __name__ == '__main__':
    Main()

