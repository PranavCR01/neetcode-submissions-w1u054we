class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
            
        def helper(houses):
            if len(houses) == 1:
                return houses[0]
            two = houses[0]
            one = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                temp = max(one, two + houses[i])
                two = one
                one = temp
            return one
        
        return max(helper(nums[1:]), helper(nums[:-1]))
            


        
            
        
        
        
        