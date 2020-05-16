class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.root = None

    def isEmpty(self):
        return True if self.root is None else False

    def push(self,data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print(data, " is pushed to stack.")

    def pop(self):
        if self.isEmpty():
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data

st = Stack()

st.push(10)
st.push(15)
st.push(20)

print(st.pop(), " is popped out")
print(st.peek()," is peek of stack")


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

