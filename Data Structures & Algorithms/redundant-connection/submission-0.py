class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+ 1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)
            if rootA == rootB:
                return False
            parent[rootA] = rootB
            return True
        
        for i, j in edges:
            if not union(i,j):
                return [i,j]
            


        