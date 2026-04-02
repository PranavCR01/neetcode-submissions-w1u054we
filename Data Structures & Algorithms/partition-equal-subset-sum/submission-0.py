class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        dp = {0}

        for num in nums:
            next_dp = set()
            for s in dp:
                next_dp.add(s)
                next_dp.add(s + num)
            dp = next_dp
            if target in dp:
                return True
        
        return False