from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Adiciona índice original das arestas
        indexed_edges = [(u, v, w, i) for i, (u, v, w) in enumerate(edges)]
        indexed_edges.sort(key=lambda x: x[2])  # Ordena por peso

        # Função que retorna o custo da MST usando Prim
        def prim(n, edge_list, banned=set(), forced_edge=None):
            graph = defaultdict(list)
            for u, v, w, i in edge_list:
                if i not in banned:
                    graph[u].append((w, v, i))
                    graph[v].append((w, u, i))
            
            total_cost = 0
            visited = set()
            heap = []

            if forced_edge:
                u, v, w, i = forced_edge
                total_cost += w
                visited.update([u, v])
                for x, y in [(u, v), (v, u)]:
                    for w2, nei, idx in graph[x]:
                        if nei not in visited:
                            heapq.heappush(heap, (w2, nei, idx))
            else:
                visited.add(0)
                for w, v, i in graph[0]:
                    heapq.heappush(heap, (w, v, i))

            while heap and len(visited) < n:
                w, u, i = heapq.heappop(heap)
                if u not in visited:
                    visited.add(u)
                    total_cost += w
                    for w2, v, j in graph[u]:
                        if v not in visited:
                            heapq.heappush(heap, (w2, v, j))

            if len(visited) < n:
                return float('inf')  # grafo desconexo
            return total_cost

        # Custo da MST original
        original_cost = prim(n, indexed_edges)

        critical = []
        pseudo_critical = []

        for u, v, w, i in indexed_edges:
            # Testa se é crítica
            cost_without = prim(n, indexed_edges, banned={i})
            if cost_without > original_cost:
                critical.append(i)
            else:
                # Testa se é pseudo-crítica
                cost_with = prim(n, indexed_edges, forced_edge=(u, v, w, i))
                if cost_with == original_cost:
                    pseudo_critical.append(i)

        return [critical, pseudo_critical]
