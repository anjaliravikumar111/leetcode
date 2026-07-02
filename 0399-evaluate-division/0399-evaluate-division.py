from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)

        # Build graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def dfs(src, target, visited):
            if src not in graph or target not in graph:
                return -1.0

            if src == target:
                return 1.0

            visited.add(src)

            for nei, weight in graph[src]:
                if nei not in visited:
                    result = dfs(nei, target, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        ans = []

        for src, target in queries:
            ans.append(dfs(src, target, set()))

        return ans