class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            adj[course].append(prerequisite)
        
        visited = set()
        visiting = set()

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
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True





        