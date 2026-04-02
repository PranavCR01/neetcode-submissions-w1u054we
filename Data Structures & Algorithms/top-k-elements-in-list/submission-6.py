import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        high = {}

        for i in nums:
            high[i] = high.get(i, 0) + 1
        
        for num, count in high.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]

        
       