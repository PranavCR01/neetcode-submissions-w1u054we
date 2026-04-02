class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, best = 0, 0 
        window = set()

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            best = max(best, r - l + 1)
        return best



        