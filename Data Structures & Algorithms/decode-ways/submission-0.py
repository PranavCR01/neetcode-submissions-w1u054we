class Solution:
    def numDecodings(self, s: str) -> int:
        one = 1 if s[0] != '0' else 0
        two = 1 

        for i in range(1, len(s)):
            temp = 0
            if s[i] != '0':
                temp += one
            if i >0 and 10 <= int(s[i - 1 : i + 1]) <= 26:
                temp += two
            
            two = one
            one = temp
        return one

        