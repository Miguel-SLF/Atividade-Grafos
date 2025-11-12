from collections import deque

def bfs_padrao(graph, start_node):

    print("\n--- Iniciando BFS Padrão ---")
    visited = set()        
    queue = deque([start_node]) 
    visited.add(start_node)
    
    visit_order = [] 

    print(f"Estado Inicial:")
    print(f"  Fila: {list(queue)}")
    print(f"  Visitados: {visited}")
    print("-" * 25)

    while queue:
        current_node = queue.popleft()
        visit_order.append(current_node)
        
        print(f"Processando Nó: '{current_node}'")
        print(f"  Fila (após retirar): {list(queue)}")
        print(f"  Visitados (atual): {visited}")

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"    -> Adicionando vizinho '{neighbor}'")
        
        print(f"  Fila (após adicionar vizinhos): {list(queue)}")
        print("-" * 25)
                
    print("Fila vazia. Fim do BFS Padrão.")
    return visit_order

def bfs_menor_caminho(graph, start_node, end_node):

    print("\n--- Iniciando BFS Menor Caminho ---")
    
    queue = deque([(start_node, [start_node])])
    
    visited = {start_node}

    print(f"Estado Inicial:")
    print(f"  Fila: {list(queue)}")
    print(f"  Visitados: {visited}")
    print("-" * 25)

    while queue:
        # 3a. Retirar o primeiro item da fila
        (current_node, path) = queue.popleft()

        print(f"Processando Nó: '{current_node}'")
        print(f"  Caminho atual: {' -> '.join(path)}")
        print(f"  Fila (após retirar): {list(queue)}")
        print(f"  Visitados (atual): {visited}")

        # 3b. Verificar se o vértice... é o destino
        if current_node == end_node:
            print(f"\nDestino '{end_node}' encontrado!")
            return path
        
        # 3d. Obter os vizinhos do vértice
        for neighbor in graph.get(current_node, []):
            
            # Verificar se o vizinho não foi visitado
            if neighbor not in visited:

                visited.add(neighbor) 
                
                new_path = list(path)
                new_path.append(neighbor)
                queue.append((neighbor, new_path))
                print(f"    -> Adicionando vizinho '{neighbor}'")

        print(f"  Fila (após adicionar vizinhos): {list(queue)}")
        print("-" * 25)

    # 4. Retornar vazio (nenhum caminho encontrado)
    print(f"Fila vazia. Caminho de '{start_node}' para '{end_node}' não encontrado.")
    return None

# --- Exemplo de Uso ---
if __name__ == "__main__":
    
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }

    # Teste da Busca em Largura para Menor Caminho 
    start_node_caminho = 'A'
    end_node_caminho = 'G'
    
    caminho = bfs_menor_caminho(grafo, start_node_caminho, end_node_caminho)
    
    if caminho:
        print(f"\nResultado Final:")
        print(f"Menor caminho de '{start_node_caminho}' para '{end_node_caminho}':")
        print(" -> ".join(caminho))
    else:
        print(f"\nResultado Final:")
        print(f"Não foi encontrado caminho de '{start_node_caminho}' para '{end_node_caminho}'.")
