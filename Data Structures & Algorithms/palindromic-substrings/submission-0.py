class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        res = ""

        for i in range(len(s)):

            r, l = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            r, l = i + 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count 
            


        