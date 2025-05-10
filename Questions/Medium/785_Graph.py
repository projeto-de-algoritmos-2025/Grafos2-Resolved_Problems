from typing import List

# Classe para representar a estrutura Union-Find (ou Disjoint Set Union)
class UnionFind:
    def __init__(self, size):
        # Inicializa o vetor de pais: cada nó é seu próprio pai no início
        self.parent = list(range(size))
    
    def find(self, u):
        # Encontra o representante (raiz) do conjunto do elemento u
        # Aplica compressão de caminho para tornar futuras buscas mais rápidas
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Compressão de caminho
        return self.parent[u]
    
    def union(self, u, v):
        # Une os conjuntos de u e v, se forem diferentes
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv  # Faz com que o representante de u aponte para o de v

# Classe com o método principal para verificar se o grafo é bipartido
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)  # Número de vértices no grafo
        uf = UnionFind(n)  # Inicializa a estrutura Union-Find

        for u in range(n):
            for v in graph[u]:
                # Se u e v (vizinhos) estiverem no mesmo conjunto, então o grafo não é bipartido
                if uf.find(u) == uf.find(v):
                    return False
                # Une todos os vizinhos de u entre si, começando pelo primeiro
                # Isso garante que todos os vizinhos fiquem em um mesmo grupo
                if graph[u]:
                    uf.union(graph[u][0], v)
        
        # Se nenhum conflito for encontrado, o grafo é bipartido
        return True
