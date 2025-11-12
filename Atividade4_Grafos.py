def bfs_lista_de_arestas(lista_arestas, vertice_inicial):
    fila = [vertice_inicial]
    na_fila = {vertice_inicial} 


    visitados = []
    
    while fila:
        vertice_atual = fila.pop(0)
        na_fila.remove(vertice_atual)

        if vertice_atual not in visitados:
            visitados.append(vertice_atual)
        

        vizinhos = []
        for u, v in lista_arestas:
            if u == vertice_atual:
                vizinhos.append(v)
            elif v == vertice_atual:
                vizinhos.append(u)
        
        for vizinho in vizinhos:
            
            esta_na_fila = (vizinho in na_fila)
            
            foi_visitado = (vizinho in visitados)

            if not esta_na_fila and not foi_visitado:
                fila.append(vizinho)
                na_fila.add(vizinho)

    return visitados

# --- Exemplo de Uso ---

# Grafo:
# 0 -- 1 -- 3
# |    |
# 2 -- 4

arestas = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4),
    (1, 4)
]

vertice_de_inicio = 3
ordem_visita = bfs_lista_de_arestas(arestas, vertice_de_inicio)

print(f"Grafo (Lista de Arestas): {arestas}")
print(f"Iniciando em: {vertice_de_inicio}")
print(f"Ordem de Visitação (BFS): {ordem_visita}")

