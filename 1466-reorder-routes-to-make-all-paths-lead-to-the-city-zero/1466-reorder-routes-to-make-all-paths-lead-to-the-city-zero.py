from collections import defaultdict

class Solution:
    def minReorder(self, n, connections):
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))  # original direction
            graph[b].append((a, 0))  # reverse direction

        visited = set()

        def dfs(city):
            visited.add(city)
            changes = 0

            for nei, cost in graph[city]:
                if nei not in visited:
                    changes += cost
                    changes += dfs(nei)

            return changes

        return dfs(0)