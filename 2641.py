# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        stack = [[root]]
        # stack = [[1,2], [3,4]]
        while stack:
            level_sum = 0
            
            next_level = []
            
            for part in stack:
                for node in part:
                    level_sum += node.val
            
            
            for part in stack:
                part_sum = 0
                for node in part:
                    part_sum += node.val
                
                
                for node in part:
                    tmp = []
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                    if level_sum >= part_sum:
                        node.val = level_sum - part_sum
                    if tmp:
                        next_level.append(tmp)
                
                    
            stack = next_level
        
        return root
                        
                    
                    
                