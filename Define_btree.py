# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def preorderTraversal(self,root) -> object:
        res = []
        if root:
            res.append(root.val)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
    def postorderTraversal(self,root) -> object:
        res = []
        if root:
            res = res + self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.val)
        return res
    def inorderTraversal(self,root) -> object:
        res = []
        if root:
            res = res + self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res
    def levelorderTraversal(self,root)-> object:
        print("Level order list:")
        print([root.val])
        rootlist = [root.left, root.right]
        while rootlist:
            newrootlist = []
            levellist = []
            for x in rootlist:
                if x:
                    newrootlist = newrootlist + [x.left, x.right]
                    levellist = levellist + [x.val]
            print(levellist)
            rootlist = newrootlist

    def inorderiterative(self,root) -> object:
        print("Inorder traversal, iterative approach")
        rootlist = Stack([root])
        i=10
        while i>0:
            i=i-1
            x = rootlist.read()
            if x.left:
                rootlist.stacking(x.left)
                continue
            print(x.val)
            if x.right:
                rootlist.stacking(x.right)
                continue

    def binarysearchtreesearch(self,root,target):
        x=root
        path = []
        while x.val != target:
            if x.val > target:
                x=x.left
                path = path + "left"
                continue
            if x.val < target:
                x=x.right
                path = path + "right"
            if x.left == None:
                break
            if x.right == None:
                break
        if x.val == target:
            print(target, " found through path:", path)
        if x.val != target:
            print(target, " was not found within list")




class Stack(object):
    def __init__(self,x=[]):
        self.list=x
    def stacking(self,new):
        self.list.insert(0,new)
    def offload(self):
        top=self.list.pop(0)
        return top
    def read(self):
        x = self.list[0]
        return x


class Queue(object):
    def __init__(self, x=[]):
        self.list = x
    def queueup(self,new):
        self.list = self.list.insert(len(self.list)-1, new)
    def offload(self):
        nextup = self.list.pop(0)
        return nextup
    def read(self):
        x=self.list[0]
        return x

def stacktest(x,y):
    assert y == x
def emptylisttest(x):
    assert x == []
def btTraversaltest(x,y):
    assert x == y

#Testing if stacks work
teststack = Stack([1,2,3,4,5])
popstack1=teststack.offload()
print(popstack1)
stacktest(popstack1,1)
popstack2=teststack.offload()
stacktest(popstack2,2)
print(teststack.offload())
print(teststack.offload())
print(teststack.offload())
emptylisttest(teststack.list)
teststack.stacking(1)
popstack3=teststack.offload()
stacktest(popstack3,1)
emptylisttest(teststack.list)

rooted = TreeNode(1)
rooted.left = TreeNode(4)
rooted.right = TreeNode(2)
rooted.right.right = TreeNode(3)
print(rooted.preorderTraversal(rooted))
btTraversaltest(rooted.preorderTraversal(rooted),[1,4,2,3])
print(rooted.postorderTraversal(rooted))
btTraversaltest(rooted.postorderTraversal(rooted),[4,3,2,1])
print(rooted.inorderTraversal(rooted))
btTraversaltest(rooted.inorderTraversal(rooted),[4,1,2,3])
rooted.levelorderTraversal(rooted)
rooted.inorderiterative(rooted)#given up

#Setting up a bst
bst=TreeNode(8,TreeNode(4),TreeNode(12))
bst.left.left=TreeNode(2,TreeNode(1),TreeNode(3))
bst.left.right=TreeNode(6,TreeNode(5),TreeNode(7))
bst.right.left=TreeNode(10,TreeNode(9),TreeNode(11))
bst.right.right=TreeNode(14,TreeNode(13),TreeNode(15))

#trying out my bsts
bst.binarysearchtreesearch(rooted,3)
#need to figure out how to record path, maybe using chars instead of strings
