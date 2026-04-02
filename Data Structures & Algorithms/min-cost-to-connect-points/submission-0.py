import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        heap = []
        heapq.heappush(heap, (0,0))
        total = 0

        while heap:
            m_dist, num = heapq.heappop(heap)
            if num in visited:
                continue
            visited.add(num)
            total += m_dist
            for j in range(len(points)):
                if j not in visited:
                    dist = abs(points[num][0] - points[j][0]) + abs(points[num][1] - points[j][1])
                    heapq.heappush(heap, (dist, j))
            
        
        
        return total

            
                
        