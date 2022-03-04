class Queue():
    def __init__(self) -> None:
        self.queue = []
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    def get_front(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def get_back(self):
        if self.is_empty():
            return None
        return self.queue[self.rear - 1]

    def de_queue(self):
        if self.rear > self.front:
            tmp = self.queue[self.front]
            self.front += 1
            return tmp
        else:
            return None

    def en_queue(self, item):
        self.queue.append(item)
        self.rear += 1


class Stack(object):
    def __init__(self) -> None:
        super().__init__()
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)

    def length(self):
        return len(self.stack)

    def top(self):
        return self.stack[-1]
