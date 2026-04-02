import math

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(capacity):
            current_load = 0
            days_needed = 1

            for weight in weights:
                if current_load + weight > capacity:
                    days_needed += 1
                    current_load = 0
                current_load += weight
            return days_needed
    

        l, r = max(weights), sum(weights)
        res = max(weights)

        while l <= r:
            mid = (l + r) // 2
            if canShip(mid) <= days:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res






        

        