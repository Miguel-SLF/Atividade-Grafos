#Em grupos de 2 a 4 alunos, implemente um algoritmo que trabalhe grafos utilizando Lista de Adjacência onde seja possível:
# ● Inserir e remover vértices
# ● Inserir e remover arestas
# ● Calcular e exibir o grau de cada vértice
# ● Verificar se existe uma aresta que vai de um vértice para o outro
# ● Listar todos os Vizinhos de um vértice
# ● Verificar se um determinado percurso é possível


def criar_grafo():
    return {}


def inserir_vertice(grafo: dict, vertice: str):
    if vertice not in grafo: 
        grafo.update({ vertice: set() })
        return
    return print("\nEste vértice já existe no grafo !\n")


def inserir_aresta(grafo: dict, origem: str, destino: str, nao_direcionado: bool =False):
    if origem in grafo and destino in grafo:
        if nao_direcionado:
            grafo[origem].add(destino)
            grafo[destino].add(origem)
        else:
            grafo[origem].add(destino)
        return
    return print("Vértice não existe no grafo !")


def vizinhos(grafo: dict, vertice: str):
    return grafo.get(vertice, {})


def listar_vizinhos(grafo: dict, vertice: str):
  lista_vizinho = {}
  
  if vertice in grafo:
    lista_vizinho = vizinhos(grafo=grafo, vertice=vertice)
  return lista_vizinho


def exibir_grafo(grafo: dict):
    if grafo == {}: return print("Grafo está vazio !")
    
    print("Vértice -> Seus Vizinhos")
    for ver, viz in grafo.items():
        print(f"{ver} -> {viz}")
    return


def remover_aresta(grafo: dict, origem: str, destino: str, nao_direcionado=False):
    if origem in grafo and destino in grafo:
        if nao_direcionado and origem in grafo[destino] and destino in grafo[origem]:
            grafo[origem].remove(destino)
            grafo[destino].remove(origem)
            return

        if not nao_direcionado and destino in grafo[origem]:
            grafo[origem].remove(destino)
            return
    return print("Aresta não existe no grafo ou está incorreta !")


def remover_vertice(grafo, vertice):
    if vertice in grafo:
        grafo.pop(vertice)
        
        for ver, viz in grafo.items():
            if vertice in viz:
                grafo[ver].discard(vertice)
        return
    return print("\nEste vértice não existe ou já foi removido !\n")


def existe_aresta(grafo, origem, destino):
    if destino in grafo[origem]: return True
    return False


def grau_vertices(grafo, nao_direcionado: bool =True):
    graus = {}

    for ver in grafo: graus[ver] = {"In": 0, "Out": 0, "Total": 0}

    if nao_direcionado:
        for ver in grafo:
            vizinhos = listar_vizinhos(vertice=ver, grafo=grafo)
            graus[ver]["In"] = len(vizinhos)
            graus[ver]["Out"] = len(vizinhos)
            graus[ver]["Total"] = graus[ver]["In"] 
    else:
        for ver in grafo:
            for ver_aux in grafo: 
              if ver in listar_vizinhos(vertice=ver_aux, grafo=grafo): graus[ver]["In"] += 1
            graus[ver]["Out"] = len(listar_vizinhos(vertice=ver, grafo=grafo))
            graus[ver]["Total"] = graus[ver]["In"] + graus[ver]["Out"]
    
    return graus
    

def percurso_valido(grafo, caminho):
    if grafo == {}: return False
        
    if len(caminho) < 2:
        return caminho[0] in grafo
    
    for i in range(0, len(caminho)-1):
        if caminho[i] in grafo:
            if existe_aresta(grafo, caminho[i], caminho[i+1]): 
                continue
            else: 
                return False
            
    return True


def main():
    grafo_criado = criar_grafo()
    
    while True:
        try:
            print("---------------- Grafos ----------------")
            print("1 - Mostrar o grafo.")
            print("2 - Inserir vértice.")
            print("3 - Remover vértice.")
            print("4 - Inserir aresta.")
            print("5 - Remover aresta.")
            print("6 - Exibir grau do grafo.")
            print("7 - Exibir se aresta existe.")
            print("8 - Caminho existe.")
            print("0 - Sair.")
            
            opc = int(input("Digite a opção desejada: "))
            
            
            if opc == 1:
                exibir_grafo(grafo=grafo_criado)
            
            elif opc == 2:
                vertice_digitado = str(input("Digite o vértice: "))
                inserir_vertice( grafo=grafo_criado, vertice=vertice_digitado )
                
            elif opc == 3:
                vertice_digitado = str(input("Digite o vértice: "))
                remover_vertice( grafo=grafo_criado, vertice=vertice_digitado )

            elif opc == 4:
                aresta_origem = str(input("Digite o vértice de origem: "))
                aresta_destino = str(input("Digite o vértice de destino: "))
                nao_direcionado = True if str(input("Esta aresta é não direcionado: ")).lower() == "sim" else False
                inserir_aresta( grafo=grafo_criado, origem=aresta_origem, destino=aresta_destino, nao_direcionado=nao_direcionado )
            
            elif opc == 5: 
                aresta_origem = str(input("Digite o vértice de origem:"))
                aresta_destino = str(input("Digite o vértice de destino:"))
                nao_direcionado = True if str(input("Esta aresta é não direcionado:")).lower() == "sim" else False
                remover_aresta( grafo=grafo_criado, origem=aresta_origem, destino=aresta_destino, nao_direcionado=nao_direcionado )
                
            elif opc == 6:                 
                nao_direcionado = True if str(input("Este grafo é não direcionado:")).lower() == "sim" else False
                grau = grau_vertices( grafo=grafo_criado, nao_direcionado=nao_direcionado )
                print("Vértice -> {In, Out, Total}")
                for i in grau.items():
                  print(i)
                
            elif opc == 7: 
                aresta_origem = str(input("Digite o vértice de origem:"))
                aresta_destino = str(input("Digite o vértice de destino:"))
                
                if existe_aresta( grafo=grafo_criado, origem=aresta_origem, destino=aresta_destino):
                    print("Essa aresta existe !")
                else:
                    print("Essa aresta não existe !")
            
            elif opc == 8: 
                caminho = []
                armazenar = True
                
                while armazenar:
                    print(f"Seu caminho atual -> {caminho}")
                    vertice = str(input("Digite o vértice para seu caminho 'fim - Parar de ler': "))
                    if vertice != 'fim': 
                        caminho.append(vertice)
                    else: 
                        armazenar = False  
                
                print("Caminho existe !") if percurso_valido( grafo=grafo_criado, caminho=caminho) else print("Caminho não existe !")
            
            elif opc == 0:
                break
                
            else:
                print("Opção fora das disponíveis !")
        except:
            print("Opção Inválida !")


if __name__ == "__main__":
    main()