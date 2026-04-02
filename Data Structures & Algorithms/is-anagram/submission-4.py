
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_S = {}
        count_T = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count_S[s[i]] = count_S.get(s[i], 0) + 1
            count_T[t[i]] = count_T.get(t[i], 0) + 1

        return count_S == count_T  