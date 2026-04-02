from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a , b = len(s1), len(s2)

        if a > b:
            return False
        
        char1 = Counter(s1)
        char2 = Counter(s2[:a])

        for i in range(0, (b-a)):
            if char1 == char2:
                return True
            char2[s2[i + a]] += 1
            char2[s2[i]] -= 1
            if char2[s2[i]] == 0:
                del char2[s2[i]]
        return char1 == char2
             





