import random
import timeit


class Node:
    right = None
    left = None
    val = 0

    def __init__(self, val):
        self.val = val


class binarySearchTree:
    root = None

    def __init__(self):
        pass

    def insertion(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.addNode(self.root, val)

    def addNode(self, root, val):
        if val > root.val:
            if root.right is not None:
                self.addNode(root.right, val)
            else:
                root.right = Node(val)
        if val < root.val:
            if root.left is not None:
                self.addNode(root.left, val)
            else:
                root.left = Node(val)

    def search(self, val):
        if self.root is None:
            return False
        else:
            return self.checkNode(self.root, val)

    def checkNode(self, root, val):
        if root.val > val:
            if root.left is None:
                return False
            else:
                return self.checkNode(root.left, val)
        elif root.val < val:
            if root.right is None:
                return False
            else:
                return self.checkNode(root.right, val)
        else:
            return True

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


def generateRandArray():
    arr = []
    for i in range(10000):
        ran = random.randint(0, 100000)
        arr.append(ran)
    return arr


def generateSequentialArray():
    arr = []
    for i in range(10000):
        arr.append(i)
    return arr


tree = binarySearchTree()
array = generateRandArray()

for a in array:
    tree.insertion(a)

tree.inorder(tree.root)


def test():
    tree.search(10001)


def test1():
    check = False
    testValue = 10001
    for i in range(len(array)):
        if testValue == array[i]:
            check = True
            print("Found number")
            break
    print("Not Found")
    return check


print(timeit.Timer(test).repeat(number=1))
print(timeit.Timer(test1).repeat(number=1))
