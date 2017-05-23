
def reverse(data):
    for index in range(len(data)):
        yield data[len(data) - 1 - index]
# a more pythonic way for the above generator function:
#def reverse(data):
#    for index in range(len(data)-1,-1,-1):    #this range will start in len(data)-1, will stop at -1 and will setp by -1 with each iteration
#        yield data[index]


def Main():
    reverse_generator = reverse('Rabinovitch')
    for char in reverse_generator:
        print (char)

    #a generator expression:
    data = 'Rabinovitch'
    print(list(data[index] for index in range(len(data)-1, -1, -1)))


if __name__ == '__main__':
    Main()