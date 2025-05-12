from typing import List
from collections import defaultdict, deque

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        rows, cols = len(targetGrid), len(targetGrid[0])
        color_bounds = {}

        for i in range(rows):
            for j in range(cols):
                color = targetGrid[i][j]
                if color not in color_bounds:
                    color_bounds[color] = [i, j, i, j]
                else:
                    color_bounds[color][0] = min(color_bounds[color][0], i)
                    color_bounds[color][1] = min(color_bounds[color][1], j)
                    color_bounds[color][2] = max(color_bounds[color][2], i)
                    color_bounds[color][3] = max(color_bounds[color][3], j)

        graph = defaultdict(set)
        indegree = defaultdict(int)

        for color, (r1, c1, r2, c2) in color_bounds.items():
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    inner_color = targetGrid[i][j]
                    if inner_color != color and inner_color not in graph[color]:
                        graph[color].add(inner_color)
                        indegree[inner_color] += 1

        all_colors = set(color_bounds.keys())
        queue = deque([c for c in all_colors if indegree[c] == 0])
        printed = 0

        while queue:
            current = queue.popleft()
            printed += 1
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return printed == len(all_colors)