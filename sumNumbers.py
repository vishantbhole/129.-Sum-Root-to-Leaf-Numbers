from typing import Optional

# 129. Sum Root to Leaf Numbers
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        #Time = O(n)
        #Space = O(H) where H is the height of tree
        def dfs(cur, num):
            if not cur:
                return 0
            num = num * 10 + cur.val

            if not cur.left and not cur.right:
                 return num
            return dfs(cur.left, num) + dfs(cur.right, num)

        return dfs(root, 0)



def main():
    # Example: root = [1,2,3] => 12 + 13 = 25
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(Solution().sumNumbers(root))  # 25
