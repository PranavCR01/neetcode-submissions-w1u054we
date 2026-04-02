class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        one = max(nums[0], nums[1])
        two = nums[0]

        for i in range(2, len(nums)):
            temp = max(one, two + nums[i])
            two = one
            one = temp
            
        return one

        