#  Implemente a Busca em Profundidade em cima de uma das implementações de grafos 
# (lista de adjacência, matriz de adjacência ou lista de arestas) que você desejar.


def _dfs_recursivo(graph, current_node, visited, visit_order):
    visited.add(current_node)
    visit_order.append(current_node)
    print(f"Visitando: {current_node}")

    for neighbor in sorted(graph.get(current_node, [])):
        if neighbor not in visited:
            _dfs_recursivo(graph, neighbor, visited, visit_order)


def busca_em_profundidade_padrao(graph, start_node=None):
    print("\n--- Iniciando Busca em Profundidade (DFS) Padrão ---")
    visited = set()
    visit_order = []
    
    all_vertices = set(graph.keys())
    for neighbors in graph.values():
        all_vertices.update(neighbors)
        
    vertices_a_percorrer = []
    if start_node and start_node in all_vertices:
        vertices_a_percorrer.append(start_node)
    
    for u in sorted(all_vertices):
        if u not in vertices_a_percorrer:
            vertices_a_percorrer.append(u)

    for u in vertices_a_percorrer:
        if u not in visited:
            if len(visited) > 0:
                 print(f"\n--- Continuando DFS para nova componente a partir de {u} ---")
            else:
                print(f"--- Início da busca em {u} ---")
            
            _dfs_recursivo(graph, u, visited, visit_order)

    print("\nFim do DFS Padrão.")
    return visit_order

if __name__ == "__main__":
    
    grafo_exemplo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F'],
        'H': [],
        'I': ['J'],
        'J': ['I']
    }

    start_node_dfs = 'A'
    ordem_visita = busca_em_profundidade_padrao(grafo_exemplo, start_node_dfs)
    
    print(f"\nGrafo: {grafo_exemplo}")
    print(f"Iniciando em: {start_node_dfs}")
    print(f"Ordem de Visitação (DFS): {ordem_visita}")