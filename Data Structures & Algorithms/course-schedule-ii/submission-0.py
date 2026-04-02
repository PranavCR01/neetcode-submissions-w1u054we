class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = {i: [] for i in range(numCourses)}
        visiting = set()
        visited = set()
        res = []

        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite) 

        def dfs(node):
            if node in visiting:
                return False
            
            if node in visited:
                return True

            visiting.add(node)

            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            visiting.discard(node)
            visited.add(node)
            res.append(node)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
                
            
            
            