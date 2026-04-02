class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(0, len(s)):
            if dp[i] == True:
                for word in wordDict:
                    if s[i : i + len(word)] == word:
                        dp[i + len(word)] = True
        return dp[len(s)]

        
        