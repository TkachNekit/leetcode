# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Recursive"""

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)
        return arr

    """Non recursive"""

    def iterativeInorderTraversal(self, root: TreeNode) -> list[int]:
        res, stack = [], []
        curr = root
        while True:
            if curr != None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
            else:
                break
        return res
