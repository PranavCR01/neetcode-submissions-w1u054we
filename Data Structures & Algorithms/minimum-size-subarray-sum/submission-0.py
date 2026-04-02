class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, count, add = 0, 0, 0
        res = float('inf')

        for r in range(len(nums)):
            add += nums[r]
            while add >= target:
                res = min(res, r - l + 1)
                add -= nums[l]
                l += 1
        return res if res != float('inf') else 0
        