class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        visited = set()

        if len(edges) != n - 1:
            return False

        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node, parent):
            if node in visited:
                return False            
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True
        dfs(0,-1)
        if len(visited) != n:
            return False
        return True



        