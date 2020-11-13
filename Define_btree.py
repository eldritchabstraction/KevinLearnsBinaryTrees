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
        rootlist=[root.right,root.left]
        while rootlist:
            newrootlist=[]
            levellist = []
            for x in rootlist:
                if x:
                    newrootlist=newrootlist+[x.left,x.right]
                    levellist=levellist + [x.val]
            print(levellist)
            rootlist = newrootlist
    def inorderiterative(self,root)-> object:
        print("Inorder traversal, iterative approach")
        rootlist=[root]
        i = 1
        while rootlist:
            if rootlist(i).left:
                rootlist = rootlist + rootlist(i).left
                i = i + 1
                continue
            print(rootlist(i).val)
            if rootlist(i).right:
                rootlist = rootlist + rootlist(i).right
                i = i + 1
                continue
            rootlist.pop(i)
            i = i - 1

rooted = TreeNode(1)
rooted.left = TreeNode(4)
rooted.right = TreeNode(2)
rooted.right.right = TreeNode(3)
print(rooted.preorderTraversal(rooted))
print(rooted.postorderTraversal(rooted))
print(rooted.inorderTraversal(rooted))
rooted.levelorderTraversal(rooted)
rooted.inorderiterative(rooted)
#for x in outputlist:
#    print(x)

