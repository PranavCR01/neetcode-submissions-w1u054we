import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        heap = []
        visited = set()
        distance = {}

        for u, v, w in times:
            adj[u].append((v, w))

        heapq.heappush(heap, (0,k))

        while heap:
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            distance[node] = cost
            
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(heap,(cost + weight, neighbor))
            
        if len(visited) != n:
            return -1
        return max(distance.values())

            
        


        