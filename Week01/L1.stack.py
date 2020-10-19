class Stack:
    def __init__(self, max_len):
        self.data = [None] * max_len
        self.len = 0

    def push(self, val):
        self.data[self.len] = val
        self.len += 1

    def front(self):
        return self.data[self.len - 1]

    def pop(self):
        res = self.front()
        self.len -= 1
        return res

    def clear(self):
        self.len = 0

    def __len__(self):
        # This function is for using len(x).
        return self.len

    def __repr__(self):
        # This function is for visualization.
        # It allows to use print() for Stack
        items = ''
        if len(self) >= 2:
            if len(self) == 2:
                dots = ''
            else:
                dots = '..., '
            items = f'{self.data[0]}, {dots}{self.front()}'
        elif len(self) == 1:
            items = f'{self.front()}'
        return f'Stack ({len(self)} items): [{items}]'


if __name__ == '__main__':
    x = Stack(1000)
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
    print('!', x.pop())
    print(x)
