class Node:
    def __init__(self, val, next = None):
        self.data = val
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head:
            curr = Node(value, self.head)
            self.head = curr
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

class MyQueue:

    def __init__(self):
        self.elements = Stack()

    def push(self, x: int) -> None:
        if self.elements.empty():
            self.elements.push(x)
            return
        new = Stack()
        while not self.elements.empty():
            new.push(self.elements.pop())
        new.push(x)
        while not new.empty():
            self.elements.push(new.pop())

    def pop(self) -> int:
        return self.elements.pop()

    def peek(self) -> int:
        return self.elements.peek()

    def empty(self) -> bool:
        return self.elements.empty()
