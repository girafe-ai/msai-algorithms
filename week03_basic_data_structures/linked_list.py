class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        # creating service node:
        self.head = ListNode(None, None)
        self.tail = self.head
        self.len = 0

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

    def push_front(self, val):
        return self.insert(self.head, val)

    def push_back(self, val):
        return self.insert(self.tail, val)

    def remove(self, node):
        if not isinstance(node, ListNode):
            raise TypeError("Expected node to be"
                            "ListNode instance")
        if self.len < 1:
            raise ValueError('Trying to remove item from empty list')
        prev_node = self.head
        while prev_node is not None and prev_node.next != node:
            prev_node = prev_node.next
        if prev_node is not None:
            prev_node.next = node.next
            self.len -= 1
            if prev_node.next is None:
                self.tail = prev_node
            return node.val
        else:
            raise ValueError('Node provided to remove()'
                             'was not found in the list')

    def pop_back(self):
        return self.remove(self.tail)

    def pop_front(self):
        # self.head.next may be Null. It is checked in self.remove()
        return self.remove(self.head.next)

    def __len__(self):
        # This function is for using len(x).
        return self.len

    # Following functions are just for easier debugging and testing:

    def get_node_by_index(self, i):
        # Service node is supposed to be node 0
        if i < 0:
            i += self.len + 1
        if not (0 <= i <= self.len):
            raise IndexError('List index out of range')
        res = self.head
        for i in range(i):
            res = res.next
        return res

    def insert_by_index(self, i, val):
        prev_node = self.get_node_by_index(i)
        return self.insert(prev_node, val)

    def remove_by_index(self, i):
        node = self.get_node_by_index(i)
        self.remove(node.next)

    def __getitem__(self, i):
        # This function is for using x[i].
        # We add 1 because self.get_node_by_index(0) returns service node
        return self.get_node_by_index(i + 1).val

    def __repr__(self):
        # This function is for visualization.
        # It allows to use print() for List
        max_show = 10
        show_len = min(len(self), max_show)
        elements_repr = list(map(str, [self[i] for i in range(show_len)]))
        if len(self) > max_show:
            elements_repr.append('...')
        return f'List({len(self)} elements): [{", ".join(elements_repr)}]'


if __name__ == '__main__':
    x = LinkedList()
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
    x.insert_by_index(-2, 'Text')
    print(x)
    x.remove_by_index(2)
    print(x)
    x.pop_front()
    print(x)
    x.pop_back()
    print(x)
    x.push_back('Back')
    print(x)
