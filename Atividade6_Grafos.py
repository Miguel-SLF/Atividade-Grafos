class GrafoDFS:
    def __init__(self):
        self.adj = {}

    def adicionar_vertice(self, u):
        if u not in self.adj:
            self.adj[u] = []

    def adicionar_aresta(self, u, v, direcionado=False):

        self.adicionar_vertice(u)
        self.adicionar_vertice(v)

        # Adiciona a aresta u -> v
        if v not in self.adj[u]:
            self.adj[u].append(v)

        if not direcionado:
            if u not in self.adj[v]:
                self.adj[v].append(u)

    def _dfs_recursivo(self, u, visitados):
        visitados.add(u)
        print(f"Visitando: {u}")

        for v in self.adj.get(u, []):
            if v not in visitados:
                self._dfs_recursivo(v, visitados)

    def busca_em_profundidade_padrao(self, no_inicial=None):


        visitados = set()  
        
        vertices_a_percorrer = []
        if no_inicial and no_inicial in self.adj:
            vertices_a_percorrer.append(no_inicial)
        
        for u in sorted(self.adj.keys()):
            if u not in vertices_a_percorrer:
                vertices_a_percorrer.append(u)

        for u in vertices_a_percorrer:
            if u not in visitados and u in self.adj:
                if len(visitados) > 0:
                     print(f"\n--- Continuando DFS para nova componente a partir de {u} ---")
                else:
                    print(f"--- Início da busca em {u} ---")

                self._dfs_recursivo(u, visitados)


g = GrafoDFS()

g.adicionar_aresta('A', 'B')
g.adicionar_aresta('A', 'C')
g.adicionar_aresta('B', 'D')
g.adicionar_aresta('C', 'E')
g.adicionar_aresta('D', 'F')
g.adicionar_aresta('E', 'F')
g.adicionar_aresta('F', 'G')

g.adicionar_vertice('H') 

g.adicionar_aresta('I', 'J')

print("Grafo criado:")
print(g.adj)

g.busca_em_profundidade_padrao('A')