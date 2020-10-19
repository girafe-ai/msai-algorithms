class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push_front(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.len += 1

    def insert(self, previous_node, val):
        if not isinstance(previous_node, ListNode):
            raise TypeError("Expected previous_node to be"
                            "ListNode instance")
        new_node = ListNode(val, previous_node.next)
        previous_node.next = new_node
        self.len += 1
        if new_node.next is None:
            self.tail = new_node
        return new_node

    def push_back(self, val):
        return self.insert(self.tail, val)

    def get_node_by_index(self, i):
        if not (0 <= i < self.len):
            raise IndexError('List index out of range')
        res = self.head
        for i in range(i):
            res = res.next
        return res

    def insert_by_index(self, i, val):
        if isinstance(i, int):
            if i < 0:
                i += self.len + 1
            if i == 0:
                return self.push_front(val)
            else:
                prev_node = self.get_node_by_index(i - 1)
                return self.insert(prev_node, val)
        else:
            TypeError("Expected i to be integer")

    def __len__(self):
        # This function is for using len(x).
        return self.len

    def __getitem__(self, i):
        # This function is for using x[i].
        return self.get_node_by_index(i).val

    def __repr__(self):
        # This function is for visualization.
        # It allows to use print() for List
        show_len = min(len(self), 10)
        elements_repr = list(map(str, [self[i] for i in range(show_len)]))
        if len(self) > 10:
            elements_repr.append('...')
        return f'List({len(self)} elements): [{", ".join(elements_repr)}]'


if __name__ == '__main__':
    x = List()
    x.push_front(1)
    print(x)
    x.push_front(10)
    print(x)
    x.push_front(100)
    print(x)
    x.push_front(1000)
    print(x)
    x.insert_by_index(2, 5)
    print(x)
    x.insert_by_index(1, 7)
    print(x)
    x.insert_by_index(-1, 70)
    print(x)
    x.insert_by_index(-1, 80)
    print(x)
    x.insert_by_index(-2, None)
    print(x)
