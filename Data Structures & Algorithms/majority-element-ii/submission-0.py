class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_map = {}
        res = []

        for i in nums:
            num_map[i] = num_map.get(i, 0) + 1

        for num, count in num_map.items():
            if count > len(nums) // 3:
                res.append(num)
        return res

                


        