class Node:
    def __init__(self, val, next = None):
        self.data = val
        self.next = next

class Queue:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(value)
        else:
            self.head = Node(value)

    def peek(self):
        return None if not self.head else self.head.data

    def pop(self):
        if not self.head:
            return None
        res = self.head
        self.head = self.head.next
        return res.data

    def empty(self):
        return not bool(self.head)

class MyStack:

    def __init__(self):
        self.elements = Queue()

    def push(self, x: int) -> None:
        new = Queue()
        new.push(x)
        while not self.elements.empty():
            new.push(self.elements.pop())
        self.elements = new

    def pop(self) -> int:
        return self.elements.pop()

    def top(self) -> int:
        return self.elements.peek()

    def empty(self) -> bool:
        return self.elements.empty()
