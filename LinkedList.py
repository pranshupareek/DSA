class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def loopDetector(self):
        slow = self.head
        fast = self.head
        while 1:
            slow = slow.next
            fast = fast.next
            if fast == None:
                print('No Loop Found')
                dr= False
                break
            fast = fast.next

            if fast == None:
                print('No Loop Found')
                dr= False
                break
            elif slow.next == fast.next:
                print('\nLoop detected')
                dr= True
                break

        if dr:
            slow=self.head
            while slow.next!=fast.next:
                slow=slow.next
                fast=fast.next
            fast.next=None
            print('Loop removed')
            LinkedList.printList(self)

    def printList(self):
        temp = self.head
        i = 50
        while (temp) and i:
            i -= 1
            print(temp.data, end='')
            temp = temp.next
            if temp:
                print(end=', ')
            else:
                print()

    def loopMaker(self, i=3):
        temp = self.head
        temp2 = self.head
        while i:
            i -= 1
            temp = temp.next
        while temp2.next:
            temp2 = temp2.next
        temp2.next = temp

    def ins(self, data):
        eti = Node(data)
        if self.head is None:
            self.head = eti
            return
        laste = self.head
        while (laste.next):
            laste = laste.next
        laste.next = eti


# Driver Code
llist = LinkedList()
n = int(input("Enter number of insertion "))
print('Insert your data in link list')
for i in range(n):
    td = input()
    llist.ins(td)


#Adding Loop
llist.loopMaker(2)
#loop added successfully


llist.printList() #printing list


# Now will try to detect it
llist.loopDetector()
