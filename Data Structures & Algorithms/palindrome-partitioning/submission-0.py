class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def is_palin(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def dfs(start):
            if start == len(s):
                res.append(path.copy())
                return 
            
            for end in range(start, len(s)):
                if is_palin(start, end):
                    path.append(s[start: end + 1])
                    dfs(end + 1)
                    path.pop()
        
        dfs(0)
        return res
            

        