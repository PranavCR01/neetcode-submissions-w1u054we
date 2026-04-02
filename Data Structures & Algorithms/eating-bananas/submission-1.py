import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hour = sum(math.ceil(pile/mid) for pile in piles)
            if hour <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res


        