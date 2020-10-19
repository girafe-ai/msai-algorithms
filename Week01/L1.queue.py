class Queue:
    def __init__(self, max_len):
        self.max_len = max_len
        self.data = [None] * self.max_len
        self.first = 0
        self.last = 0
        self.len = 0

    def push(self, val):
        self.data[self.last] = val
        self.len += 1
        self.last += 1
        if self.last == self.max_len:
            self.last = 0

    def front(self):
        if len(self) > 0:
            return self.data[self.first]
        else:
            raise IndexError

    def pop(self):
        res = self.front()
        self.first += 1
        self.len -= 1
        if self.first == self.max_len:
            self.first = 0
        return res

    def clear(self):
        self.first = 0
        self.last = 0
        self.len = 0

    def __len__(self):
        # This function is for using len(x).
        return self.len

    def __repr__(self):
        # This function is for visualization.
        # It allows to use print() for Queue
        items = ''
        if len(self) >= 2:
            if len(self) == 2:
                dots = ''
            else:
                dots = '..., '
            items = f'{self.data[self.last - 1]}, {dots}{self.front()}'
        elif len(self) == 1:
            items = f'{self.front()}'
        return f'Queue ({len(self)} items): [{items}]'


if __name__ == '__main__':
    x = Queue(3)
    x.push(1)
    print(x)
    x.push(2)
    print(x)
    x.push(10)
    print(x)
    print('!', x.pop())
    print(x)
    print('!', x.pop())
    print(x)
    x.push(100)
    print(x)
    print('!', x.pop())
    print(x)
    x.push(-10)
    print(x)
    print('!', x.pop())
    print(x)
    print('!', x.pop())
    print(x)
