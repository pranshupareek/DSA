# Implementing queue using array

class arrayQueue:
    def __init__(self, cap=100):
        self.front = self.size = 0
        self.rear = cap - 1
        self.Q = [None] * cap
        self.cap = cap

    def isFull(self):
        return self.size == self.cap

    def isEmpty(self):
        return self.size == 0

    def enQueue(self, ele):
        if self.isFull():
            print('Full')
            return
        self.rear = (self.rear + 1) % self.cap
        self.Q[self.rear] = ele
        self.size = self.size + 1
        # print(ele, " is added to the Queue.")

    def deQueue(self):
        if self.isEmpty():
            print('Empty')
            return
        ele = self.Q[self.front]
        # print(ele, " is removed from the queue.")
        self.front = (self.front + 1) % self.cap
        self.size = self.size - 1

    def queueFront(self):
        if self.isEmpty():
            print('Empty')
            return
        return self.Q[self.front]
        # print(self.Q[self.front], " is in front of queue.")

    def queueRear(self):
        if self.isEmpty():
            print('Empty')
            return
        return self.Q[self.rear]
        # print(self.Q[self.rear], " is in the end of queue.")

    def printQueue(self):
        if self.isEmpty():
            print('Empty!')
        else:
            print('Your queue or stack is ', end="")
        for i in range(self.size):
            print(self.Q[(self.front + i) % self.cap], end="")
            if i != self.size - 1:
                print(end=", ")
            else:
                print('.')


# Implementation using LinkedList

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class llQueue:
    def __init__(self, cap=float('inf')):
        self.front = None
        self.rear = None
        self.size = 0
        self.cap = cap

    def isEmpty(self):
        return self.front is None

    def isFull(self):
        return self.size == self.cap

    def enQueue(self, ele):

        if self.isFull():
            print('Full!!')
            return
        self.size = self.size + 1
        tmp = node(ele)
        if self.front is None:
            self.front = self.rear = tmp
            # print(ele, ' is added to the queue.')
            return

        self.rear.next = tmp
        self.rear = tmp
        # print(ele, ' is added to the queue.')

    def deQueue(self):
        if self.isEmpty():
            print('Empty!!')
            return

        self.size = self.size - 1

        tmp = self.front
        # print(tmp.data, ' is removed from queue.')
        self.front = tmp.next

        if self.front is None:
            self.rear = None

    def queueFront(self):

        if self.isEmpty():
            print('Empty!!')
            return
        return self.front.data
        # print(self.front.data, ' is in the front.')

    def queueRear(self):

        if self.isEmpty():
            print('Queue is empty.')
            return
        return self.rear.data
        # print(self.rear.data, ' is in the last')

    def printQueue(self):

        if self.isEmpty():
            print('Empty!!')
            return

        temp = self.front
        print('Your queue or stack is ', end="")
        while temp.next is not None:
            print(temp.data, end=", ")
            temp = temp.next

        print(temp.data, end=". \n")


# # Driver code
#
# # q = arrayQueue(5)
# q = llQueue(5)
#
# q.enQueue(5)
# q.enQueue(8)
# q.enQueue(15)
# q.enQueue(19)
# q.queueFront()
# q.queueRear()
# q.printQueue()
# q.enQueue(55)
# q.deQueue()
# q.deQueue()
# q.deQueue()
# q.deQueue()
# q.deQueue()
# q.deQueue()
# q.deQueue()
# q.deQueue()
# q.enQueue(55)
# q.enQueue(60)
# q.queueFront()
# q.queueRear()
# q.printQueue()

# Implementing Stack using queue

class Stack:
    def __init__(self, cap=100):
        self.q1 = llQueue(cap)
        self.q2 = llQueue(cap)

    def push(self, ele):
        self.q2.enQueue(ele)
        while not self.q1.isEmpty():
            self.q2.enQueue(self.q1.queueFront())
            self.q1.deQueue()
        [self.q1, self.q2] = [self.q2, self.q1]


    def pop(self):
        self.q1.deQueue()

    def print(self):
        self.q1.printQueue()


stack = Stack()

stack.push(5)
stack.push(7)
stack.push(8)
stack.push(15)
stack.push(19)
stack.push(25)
stack.print()
print('push done')

stack.pop()
stack.pop()
stack.pop()

stack.print()