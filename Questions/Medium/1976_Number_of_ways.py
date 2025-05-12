from typing import List
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        adj = [[] for _ in range(n)]
        for a, b, t in roads:
            adj[a].append((b, t))
            adj[b].append((a, t))
        
        min_time = [float('inf')] * n
        path_count = [0] * n
        min_time[0] = 0
        path_count[0] = 1
        
        queue = [(0, 0)]
        
        while queue:
            current_time, u = heapq.heappop(queue)
            
            if current_time > min_time[u]:
                continue 
            
            for v, weight in adj[u]:
                time_through_u = current_time + weight
                if time_through_u < min_time[v]:
                    min_time[v] = time_through_u
                    path_count[v] = path_count[u]
                    heapq.heappush(queue, (time_through_u, v))
                elif time_through_u == min_time[v]:
                    path_count[v] = (path_count[v] + path_count[u]) % MOD
        
        return path_count[n - 1]