# Implementation using LinkedList

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        # print(data, " is pushed to stack.")

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def printStack(self):
        if self.isEmpty():
            print('Empty')
            return
        print('Stack is ', end="")
        temp = self.root
        while temp.next is not None:
            print(temp.data, end=" ")
            temp = temp.next

    def peek(self):
        if self.isEmpty():
            return -1
        return self.root.data


# st = Stack()
#
# st.push(10)
# st.push(15)
# st.push(20)
#
# print(st.pop(), " is popped out")
# print(st.peek()," is peek of stack")


# # Implementing with array
#
# from sys import maxsize
#
# def createStack():
#     stack = []
#     return stack
#
# def isEmpty(stack):
#     return len(stack)==0
#
# def push(stack, ele):
#     stack.append(ele)
#     print('Pushed ', ele ,' to stack')
#
# def pop(stack):
#     if isEmpty(stack):
#         return str(-maxsize-1)
#     return stack.pop()
#
# def peek(stack):
#     if isEmpty(stack):
#         return str(-maxsize-1)
#     return stack[len(stack)-1]
#
# st = createStack()
#
# push(st, 5)
# push(st, 9)
# push(st, 15)
# print(pop(st),' popped')
# print(pop(st),' popped')
# print(peek(st))
# print(pop(st),' popped')
# print(pop(st),' popped')

# Check for balanced parenthesis
def checkBalance(str):
    stack = Stack()
    ob = ['{', '[', '(', '<']
    cb = ['}', ']', ')', '>']

    isBalanced = False
    for i in range(len(str)):
        if str[i] in ob:
            stack.push(ob.index(str[i]))
        else:
            p = stack.pop()
            if p == cb.index(str[i]):
                isBalanced = True
                continue
            else:
                isBalanced = False
                break

    if not stack.isEmpty():
        isBalanced = False
    if isBalanced:
        print('String', str, 'is Balanced.')
    else:
        print('String', str, 'is not balanced')


# str = input()
#
# checkBalance(str)


# Implementing two stack in an array

class twostack:
    def __init__(self, cap=10):
        self.arr = [None] * cap
        self.top1 = -1
        self.top2 = cap
        self.cap = cap

    def push1(self, ele):
        if not self.top1 + 1 < self.top2:
            print('Overflow!!')
            return
        self.top1 = self.top1 + 1
        self.arr[self.top1] = ele

    def push2(self, ele):
        if not self.top1 + 1 < self.top2:
            print('Overflow!!')
            return
        self.top2 = self.top2 - 1
        self.arr[self.top2] = ele

    def pop1(self):
        if self.top1 == -1:
            print('Underflow!!')
            return
        ele = self.arr[self.top1]
        self.top1 = self.top1 - 1
        return ele

    def pop2(self):
        if self.top2 == self.cap:
            print('Underflow!!')
            return
        ele = self.arr[self.top2]
        self.top2 = self.top2 + 1
        return ele

    def print1(self):
        if self.top1 == -1:
            print('Underflow!!')
            return
        for i in range(self.top1):
            print(self.arr[i], end=", ")
        print(self.arr[self.top1], end=".\n")

    def print2(self):
        if self.top2 == self.cap:
            print('Underflow!!')
            return
        for i in range(self.cap - 1, self.top2, -1):
            print(self.arr[i], end=", ")
        print(self.arr[self.top2], end=".\n")


# cs = twostack(5)
# cs.push1(10)
# cs.push1(15)
# cs.push1(13)
# cs.pop1()
# cs.push2(3)
# cs.push2(9)
# cs.print1()
# cs.print2()


# Implementing k stacks in an array of length n

class kStack:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.arr = [None] * self.n
        self.top = [-1] * self.k
        self.free = 0
        self.next = [i + 1 for i in range(self.n)]
        self.next[self.n - 1] = -1

    def isEmpty(self, sn):
        return self.top[sn] == -1

    def isFull(self):
        return self.free == -1

    def push(self, item, sn):
        if self.isFull():
            print('Full!!')
            return

        insert_at = self.free
        self.free = self.next[self.free]
        self.arr[insert_at] = item
        self.next[insert_at] = self.top[sn]
        self.top[sn] = insert_at

    def pop(self, sn):
        if self.isEmpty(sn):
            print('Empty!!')
            return

        popped = self.top[sn]
        self.top[sn] = self.next[popped]
        self.next[popped] = self.free
        self.free = popped
        return self.arr[popped]

    def printStack(self, sn):
        if self.isEmpty(sn):
            print('Empty!!')
            return

        temp = self.top[sn]
        while temp != -1:
            print(self.arr[temp], end=" ")
            temp = self.next[temp]


# # Driver code
#
# kstacks = kStack(3, 10)
#
# # Push some items onto stack number 2.
# kstacks.push(15, 2)
# kstacks.push(45, 2)
#
# # Push some items onto stack number 1.
# kstacks.push(17, 1)
# kstacks.push(49, 1)
# kstacks.push(39, 1)
#
# # Push some items onto stack number 0.
# kstacks.push(11, 0)
# kstacks.push(9, 0)
# kstacks.push(7, 0)
#
# print("Popped element from stack 2 is " +
#       str(kstacks.pop(2)))
# print("Popped element from stack 1 is " +
#       str(kstacks.pop(1)))
# print("Popped element from stack 0 is " +
#       str(kstacks.pop(0)))
#
# kstacks.printStack(0)


# Stock market problem (Nearest greater element on the left)

def stockM(arr):
    s = Stack()
    s.push(0)
    sc = [1]

    for i in range(1, len(arr)):
        sp = s.peek()
        while not s.isEmpty() and arr[i] > arr[s.peek()]:
            s.pop()
            sp = s.peek()
        s.push(i)
        sc.append(i - sp)
    return sc


# # arr = [10, 5, 2, 7, 18, 15, 16, 17]
# # arr = [10, 20 , 30]
# arr = [3, 2, 1]
# print(stockM(arr))


# Nearest greater element in right

def greaterInRight(arr):
    s = Stack()
    s.push(0)
    n = len(arr)
    gr = [None] * n
    for i in range(1, n):
        sp = s.peek()
        if arr[i] < arr[sp]:
            s.push(i)
            continue
        while arr[i] > arr[s.peek()]:
            sp = s.pop()
            gr[sp] = arr[i]
        s.push(i)

    while not s.isEmpty():
        sp = s.pop()
        gr[sp] = -1

    return gr


# arr = [5, 10, 7, 8, 3, 2, 12]
# arr = [10,20,30]
arr = [30, 20, 10]
print(greaterInRight(arr))