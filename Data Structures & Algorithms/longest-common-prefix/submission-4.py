class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        res = ""
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            for word in strs:
                if i >= len(word) or word[i] != shortest[i] :
                    return res
            res += shortest[i]
        return res
