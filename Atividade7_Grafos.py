# Implemente a detecção de ciclos utilizando Busca em Profundidade

def _dfs_ciclos_recursivo(graph, current_node, visited, parent_map):
    visited.add(current_node)
    print(f"Explorando: {current_node} (Pai: {parent_map.get(current_node, 'Nenhum')})")

    for neighbor in sorted(graph.get(current_node, [])):

        if neighbor not in visited:
            parent_map[neighbor] = current_node
            if _dfs_ciclos_recursivo(graph, neighbor, visited, parent_map):
                return True
        
        elif neighbor != parent_map.get(current_node):
            print(f" *** CICLO ENCONTRADO! *** A aresta ({current_node}, {neighbor}) forma um ciclo.")
            return True 
    
    return False


def detectar_ciclos_dfs(graph):
    print("\n--- Iniciando Detecção de Ciclos via DFS ---")
    
    all_vertices = set(graph.keys())
    for neighbors in graph.values():
        all_vertices.update(neighbors)
        
    visited = set()
    parent_map = {} 

    for u in sorted(all_vertices):
        if u not in visited:
            parent_map[u] = None 
            if _dfs_ciclos_recursivo(graph, u, visited, parent_map): 
                print("\nResultado Final: O grafo contém um ciclo.")
                return True

    print("\nResultado Final: O grafo não contém ciclos.")
    return False

if __name__ == "__main__":
    
    grafo_com_ciclo = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'], 
        'D': ['B', 'C', 'E'],
        'E': ['D', 'F'],
        'F': ['E']
    }

    print("Grafo 1 (Com Ciclo):", grafo_com_ciclo)
    detectar_ciclos_dfs(grafo_com_ciclo)
    
    print("\n" + "=" * 50 + "\n")
    
    grafo_sem_ciclo = {
        '0': ['1', '2'],
        '1': ['0', '3', '4'],
        '2': ['0', '5'],
        '3': ['1'],
        '4': ['1'],
        '5': ['2'],
    }
    
    print("Grafo 2 (Sem Ciclo):", grafo_sem_ciclo)
    detectar_ciclos_dfs(grafo_sem_ciclo)