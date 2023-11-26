class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.queue[0]
            self.queue = self.queue[1:]
            return item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0


def main():
 queue = Queue()

 queue.push(5)
 queue.push(10)
 queue.push(15)

 print(queue.peek())

 print(queue.pop())
 print(queue.pop())
 print(queue.pop())

 print(queue.is_empty())

if __name__ == "__main__":
    main()