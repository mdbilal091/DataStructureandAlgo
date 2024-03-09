from collections import deque
class Queue:
    def __init__(self):
        self.queueitem = deque()

    def is_empty(self):
        return not self.queueitem
        #return len(self.queueitem) == 0

    def enqueue(self, queueitem):
        self.queueitem.append(queueitem)

    def dequeue(self):
        return self.queueitem.popleft()

    def peek(self):
        return self.queueitem[0]

    def size(self):
        return len(self.queueitem)

    def __str__(self):
        return str(self.queueitem)



if __name__ == "__main__":
    q = Queue()
    print(q)

    q.enqueue("THis")
    q.enqueue("is")
    q.enqueue("my")
    q.enqueue("first")
    q.enqueue("queue")
    print(q)

    q.dequeue()

    print(q)

    print(q.size())
    print(q.peek())



