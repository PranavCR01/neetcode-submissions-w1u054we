class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = 0
        right_max = 0
        best = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max,height[left])
                best += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max,height[right])
                best += right_max - height[right]
                right -= 1
        return best