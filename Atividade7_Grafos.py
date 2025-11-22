class GrafoCiclosDFS:

    def __init__(self):
        self.adj = {}
        self.encontrou_ciclo = False

    def adicionar_vertice(self, u):
        if u not in self.adj:
            self.adj[u] = []

    def adicionar_aresta(self, u, v, direcionado=False):
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)

        if v not in self.adj[u]:
            self.adj[u].append(v)

        if not direcionado:
            if u not in self.adj[v]:
                self.adj[v].append(u)

    def _dfs_ciclos_recursivo(self, u, visitados, pai):
        visitados.add(u)
        print(f"Explorando: {u} (Pai: {pai})")

        for v in self.adj.get(u, []):
            if self.encontrou_ciclo:
                return True

            if v not in visitados:

                if self._dfs_ciclos_recursivo(v, visitados, u):
                    return True
            
            elif v != pai:
                self.encontrou_ciclo = True
                print(f" CICLO ENCONTRADO!  A aresta ({u}, {v}) forma um ciclo (pois {v} não é o pai {pai} de {u}).")
                return True 
        
        return False 


    def detectar_ciclos(self):

        print("\n--- Iniciando Detecção de Ciclos via DFS ---")
        visitados = set()
        self.encontrou_ciclo = False

        for u in sorted(self.adj.keys()):
            if u not in visitados:
                if self._dfs_ciclos_recursivo(u, visitados, None): 
                    print("\nResultado: O grafo contém um ciclo.")
                    return True

        print("\nResultado: O grafo não contém ciclos.")
        return False


g_ciclo = GrafoCiclosDFS()

g_ciclo.adicionar_aresta('A', 'B')
g_ciclo.adicionar_aresta('A', 'C')
g_ciclo.adicionar_aresta('B', 'D')
g_ciclo.adicionar_aresta('C', 'E')
g_ciclo.adicionar_aresta('D', 'F')
g_ciclo.adicionar_aresta('E', 'F') 
g_ciclo.adicionar_aresta('F', 'G')

g_ciclo.adicionar_vertice('H') 
g_ciclo.adicionar_aresta('I', 'J')

g_ciclo.detectar_ciclos()