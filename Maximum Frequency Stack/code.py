class Node:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next

class FreqStack:

    def __init__(self):
        self.freqs = {}
        self.head = None

    def push(self, val: int) -> None:
        if val in self.freqs:
            self.freqs[val] += 1
        else:
            self.freqs[val] = 1
        if not self.head:
            self.head = Node(val)
        first_node = Node(val, self.head)
        self.head = first_node

    def pop(self) -> int:
        if not self.head.next:
            res = self.head.data
            self.head = None
            self.freqs = {}
            return res
        max_fq = max(self.freqs.values())
        node = self.head
        if self.freqs[self.head.data] == max_fq:
            self.freqs[self.head.data] -= 1
            res = self.head.data
            self.head = self.head.next
            return res
        while self.freqs[node.next.data] != max_fq:
            node = node.next
        res = node.next.data
        self.freqs[node.next.data] -= 1
        node.next = node.next.next
        return res
