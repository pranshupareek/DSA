INT_MAX = 4294967296
INT_MIN = -4294967296

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
        return checkChilderSum(root.right)
    elif root.right==None and root.data==root.left.data:
        return checkChilderSum(root.left)
    elif root.data==root.left.data+root.right.data:
        return checkChilderSum(root.left) and checkChilderSum(root.right)
    else:
        return False

def printNodesatlvlK(root,k):

    if root==None:
        return
    if k==1:
        print(root.data,end=' ')
        return
    else:
        printNodesatlvlK(root.left,k-1)
        printNodesatlvlK(root.right,k-1)

def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh,rh)+1

def checkBST(root,minn=INT_MIN,maxx=INT_MAX):
    if root is None:
        return True

    if root.data<minn or root.data>maxx:
        return False

    return checkBST(root.left,minn,root.data-1) and checkBST(root.right,root.data+1,maxx)


#Driver code

root = node(15)
root.left=node(7)
root.right=node(25)
root.left.left=node(5)
root.left.right=node(12)
root.right.left=node(16)
root.right.right=node(27)
print('\nInorder: ',end="")
printInorder(root)
print('\nPostorder: ',end="")
printPostorder(root)
print('\nPreorder: ',end="")
printPreorder(root)
print()
h=height(root)
print('Height: ',h)

if checkChilderSum(root):
    print('Yes, It follow children Sum')
else:
    print('Noo, It dont follow children Sum')

print('Node lvl Element: ',end="")
printNodesatlvlK(root,3)
print()


if checkBST(root):
    print('yes, it is a BST')
else:
    print('Noo, it is not a BST')
