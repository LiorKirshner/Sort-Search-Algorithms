class Queue:
    def __init__(self):
        self.Q = list()

    def is_empty(self):
        return len(self.Q) == 0

    def top(self):
        return self.Q[0]

    def enqueue(self, value):
        self.Q.append(value)

    def dequeue(self):
        popped_value = self.Q.pop(0)
        return popped_value

    def queue_sort(self):
        temp_q = Queue()

        while not self.is_empty():
            min_value = self.dequeue()
            for i in range(len(self.Q)):
                if self.top() < min_value:
                    self.enqueue(min_value)
                    min_value = self.dequeue()
                else:
                    self.enqueue(self.dequeue())
            temp_q.enqueue(min_value)

        self.Q = temp_q.Q


def main():
    q = Queue()
    q.enqueue(9)
    q.enqueue(14)
    q.enqueue(34)
    q.enqueue(5)
    q.enqueue(12)
    q.enqueue(1)
    q.queue_sort()
    print(q.Q)


if __name__ == '__main__':
    main()