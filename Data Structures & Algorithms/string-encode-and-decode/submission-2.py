class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            encoded = str(len(word)) + '#' + word
            res.append(encoded)
        return "".join(res)
    
    # def decode(self, string):
    #     res = []
    #     i = 0

    #     while i < len(string):
    #         j = i
    #         while string[j] != '#':
    #             j += 1
    #         length = int(string[i : j])
    #         word = string[j + 1 : j + 1 + length]
    #         i = j + 1 + length
    #         res.append(word)
    #     return res


    def decode(self, string):
        res = []
        i = 0

        while i < len(string):
            j = i
            while string[j] != '#':
                j += 1
            length = int(string[i : j])
            word = string[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length
        return res






