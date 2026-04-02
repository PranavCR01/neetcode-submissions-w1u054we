class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_min = cur_max = 1

        for i in nums:
            temp = cur_max * i
            cur_max = max(i, cur_min * i, temp)
            cur_min = min(i, cur_min * i, temp)
            res = max(res, cur_max)
        
        return res
        
        