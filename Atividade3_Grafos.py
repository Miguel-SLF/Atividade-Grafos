from collections import deque


def criar_grafo():
    vertice = []
    aresta = []
    
    return vertice, aresta



def inserir_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        print(f"Vértice '{vertice}' inserido.")
    return vertices, arestas


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        vertices, arestas = inserir_vertice(vertices, arestas, origem)
    if destino not in vertices:
        vertices, arestas = inserir_vertice(vertices, arestas, destino)
    
    aresta_principal = (origem, destino)

    if aresta_principal not in arestas:
        arestas.append(aresta_principal)
        print(f"Aresta ({origem}, {destino}) inserida.")
    
    if nao_direcionado and origem != destino:
        aresta_inversa = (destino, origem)
        if aresta_inversa not in arestas:
            arestas.append(aresta_inversa)
            print(f"Aresta ({destino}, {origem}) inserida (Não-Direcionado).")
            
    return vertices, arestas


def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
        print(f"Vértice '{vertice}' removido.")
        
        novas_arestas = [
            (u, v) for u, v in arestas if u != vertice and v != vertice
        ]
        arestas = novas_arestas
        print("Arestas associadas removidas.")
            
    return vertices, arestas


def remover_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    aresta = (origem, destino)
    
    if aresta in arestas:
        arestas.remove(aresta)
        print(f"Aresta ({origem}, {destino}) removida.")
    
    if nao_direcionado:
        aresta_inversa = (destino, origem)
        if aresta_inversa in arestas:
            arestas.remove(aresta_inversa)
            print(f"Aresta ({destino}, {origem}) removida (Não-Direcionado).")

    return vertices, arestas



def calcular_grau(arestas, vertice):
    grau = 0
    for u, v in arestas:
        if u == vertice or v == vertice:
            grau += 1
    return grau


def exibir_graus(vertices, arestas, nao_direcionado=False):
    print("\n--- Graus dos Vértices (Lista de Arestas) ---")
    
    for vertice in vertices:
        if nao_direcionado:
            grau_bruto = sum(1 for u, v in arestas if u == vertice or v == vertice)
            grau = grau_bruto // 2 
            print(f"{vertice}: Grau {grau}")
        else:
            grau_saida = sum(1 for u, v in arestas if u == vertice)
            grau_entrada = sum(1 for u, v in arestas if v == vertice)
            
            print(f"{vertice}: Saída={grau_saida}, Entrada={grau_entrada} (Total={grau_saida + grau_entrada})")


def existe_aresta(arestas, origem, destino):
    aresta = (origem, destino)
    if aresta in arestas:
        return True
    
    if (destino, origem) in arestas: 
        return True

    return False


def listar_vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        return []

    vizinhos = set()
    for u, v in arestas:
        if u == vertice:
            vizinhos.add(v)
        elif v == vertice:
            vizinhos.add(u)
            
    return list(vizinhos)


def percurso_possivel(vertices, arestas, inicio, fim):
    if inicio not in vertices or fim not in vertices:
        return False
    if inicio == fim:
        return True

    visitados = {inicio}
    fila = deque([inicio])

    while fila:
        atual = fila.popleft()

        for vizinho in listar_vizinhos(vertices, arestas, atual):
            if vizinho == fim:
                return True 
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    
    return False


def main():
    NAO_DIRECIONADO = True
    
    vertices, arestas = criar_grafo()

    print("--- 1. Inicialização e Inserção ---")
    
    vertices, arestas = inserir_vertice(vertices, arestas, "A")
    vertices, arestas = inserir_vertice(vertices, arestas, "B")
    vertices, arestas = inserir_vertice(vertices, arestas, "C")
    vertices, arestas = inserir_vertice(vertices, arestas, "D")
    
    vertices, arestas = inserir_aresta(vertices, arestas, "A", "B", NAO_DIRECIONADO)
    vertices, arestas = inserir_aresta(vertices, arestas, "B", "C", NAO_DIRECIONADO)
    vertices, arestas = inserir_aresta(vertices, arestas, "A", "D", NAO_DIRECIONADO)
    
    vertices, arestas = inserir_vertice(vertices, arestas, "E")

    print("\nEstado do Grafo Inicial:")
    print(f"Vértices: {vertices}")
    print(f"Arestas (Lista Completa): {arestas}")

    exibir_graus(vertices, arestas, NAO_DIRECIONADO)

    print("\n--- 4. Verificar se existe uma aresta ---")
    
    origem1, destino1 = "A", "B"
    print(f"Existe aresta {origem1} -> {destino1}? {existe_aresta(arestas, origem1, destino1)}")

    origem2, destino2 = "C", "D"
    print(f"Existe aresta {origem2} -> {destino2}? {existe_aresta(arestas, origem2, destino2)}")

    print("\n--- 5. Listar todos os Vizinhos de um vértice ---")
    
    print(f"Vizinhos de 'A': {listar_vizinhos(vertices, arestas, 'A')}")
    print(f"Vizinhos de 'E': {listar_vizinhos(vertices, arestas, 'E')}")

    print("\n--- 6. Verificar se um determinado percurso é possível ---")
    
    print(f"Percurso de 'C' para 'D' é possível? {percurso_possivel(vertices, arestas, 'C', 'D')}") 
    print(f"Percurso de 'A' para 'E' é possível? {percurso_possivel(vertices, arestas, 'A', 'E')}")
    
    
    print("\n--- 7. Remoção de Aresta e Vértice (Revisado) ---")
    
    vertices, arestas = remover_aresta(vertices, arestas, "A", "D", NAO_DIRECIONADO)
    
    vertices, arestas = remover_vertice(vertices, arestas, "E")
    
    vertices, arestas = remover_vertice(vertices, arestas, "D")
    
    
    print("\n--- Estado Final Após Remoções ---")
    print(f"Vértices: {vertices}")
    print(f"Arestas (Lista Completa): {arestas}") 
    
    exibir_graus(vertices, arestas, NAO_DIRECIONADO)
    
    print(f"\nPercurso de 'C' para 'A' é possível (após remoções)? {percurso_possivel(vertices, arestas, 'C', 'A')}")


if __name__ == "__main__":
    main()