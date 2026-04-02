class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        
        def dfs(sub):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                sub.append(nums[i])
                dfs(sub)
                sub.pop()
                used[i] = False

        dfs([])                  
        return res
        