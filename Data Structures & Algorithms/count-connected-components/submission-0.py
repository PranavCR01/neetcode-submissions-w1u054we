class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        visited = set()
        count = 0

        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        def dfs(node):
            if node in visited:
                return None
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
                
        return count


        