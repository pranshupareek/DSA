class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

# class tree:
#     def __init__(self):
#         self.root=None
#
#     def inorder(self):
#

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.data,end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data,end=" ")

def checkChilderSum(root):
    if root==None:
        return True
    elif root.left==None and root.right==None:
        return True
    elif root.left==None and root.data==root.right.data:
        return True
    elif root.right==None and root.data==root.left.data:
        return True
    elif root.data==root.left.data+root.right.data:
        lc=checkChilderSum(root.left)
        rc=checkChilderSum(root.right)
    else:
        return False
    if lc==False or rc==False:
        return False
    else:
        return True


def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh,rh)+1

#Driver code

root = node(5)
root.left=node(2)
root.right=node(3)
root.left.left=node(1)
root.left.right=node(1)
root.right.left=node(2)
root.right.right=node(1)

printInorder(root)
print()
printPostorder(root)
print()
printPreorder(root)
print()
h=height(root)
print(h)

if checkChilderSum(root):
    print('Yes It follow children Sum')
else:
    print('Noo')