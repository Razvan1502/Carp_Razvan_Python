class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
queue = Queue()

queue.push(5)
queue.push(10)
queue.push(15)

print("Queue size:", queue.size())

print("Popped:", queue.pop())
print("Peek:", queue.peek())

print("Popped:", queue.pop())
print("Popped:", queue.pop())

print("Peek:", queue.peek())
