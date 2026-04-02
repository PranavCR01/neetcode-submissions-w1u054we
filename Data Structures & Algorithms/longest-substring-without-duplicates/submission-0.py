class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, best = 0,0
        last_seen ={}

        for right in range(len(s)):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1

            last_seen[s[right]] = right
            best = max(best, right - left + 1)

        return best


        