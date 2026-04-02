class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for i, j in counts.items():
            if j >= 2:
                return True
        return False




        