# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kk(self,root):
        if not root:
            return 
        self.kk(root.left)
        self.k-=1
        if self.k==0:
            self.res=root.val
            return 
        self.kk(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k=k
        self.res=None
        self.kk(root)
        return self.res    
