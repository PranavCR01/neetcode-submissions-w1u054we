"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(row, col, size):
            val = grid[row][col]
            isLeaf = True
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != val:
                        isLeaf = False
                        break
        
            if isLeaf:
                return Node(val, True, None, None, None, None)
        
            half = size // 2
            return Node(
                val, False,
                helper(row, col, half),
                helper(row, col + half, half),
                helper(row + half, col, half),
                helper(row + half, col + half, half )
            )

        return helper(0,0, len(grid))


        