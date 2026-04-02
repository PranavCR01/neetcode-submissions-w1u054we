
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num_map = {}

        for i in nums:
            num_map[i] = num_map.get(i, 0) + 1

        for num, count in num_map.items():
            if count > len(nums) // 2:
                return num 





        
            

        