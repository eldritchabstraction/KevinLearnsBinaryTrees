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



rooted = TreeNode(1)
rooted.left = TreeNode(4)
rooted.right = TreeNode(2)
rooted.right.right = TreeNode(3)
print(rooted.preorderTraversal(rooted))
print(rooted.postorderTraversal(rooted))
print(rooted.inorderTraversal(rooted))
#for x in outputlist:
#    print(x)

