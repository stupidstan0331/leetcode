# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.sumOfLeftLeaves_tools(root.left, True) + self.sumOfLeftLeaves_tools(root.right, False)

    def sumOfLeftLeaves_tools(self, root, isleft = True):
        if root == None:
            return 0
        if isleft:
            if root.left == None and root.right == None:
                return root.val
            else:
                return self.sumOfLeftLeaves_tools(root.left, True) + self.sumOfLeftLeaves_tools(root.right, False)
        else:
            return self.sumOfLeftLeaves_tools(root.left, True) + self.sumOfLeftLeaves_tools(root.right, False)


#      3
#    9  20
#   null,null 15, 7