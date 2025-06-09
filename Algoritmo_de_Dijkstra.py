import heapq

def dijkstra(grafo, nodo_inicio):
    """
    Encuentra los caminos más cortos desde un nodo inicial usando el algoritmo de Dijkstra
    
    Args:
        grafo (dict): Diccionario que representa el grafo {nodo: {vecino: peso}}
        nodo_inicio (str/int): Nodo desde donde comenzar la búsqueda
    
    Returns:
        distancias (dict): Distancias mínimas desde el nodo inicial
        caminos (dict): Caminos más cortos desde el nodo inicial
    """
    # Inicializar distancias con infinito y camino vacío
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[nodo_inicio] = 0
    caminos = {nodo: [] for nodo in grafo}
    caminos[nodo_inicio] = [nodo_inicio]
    
    # Usamos una cola de prioridad (min-heap)
    cola = [(0, nodo_inicio)]
    
    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)
        
        # Si encontramos una distancia mejor, saltamos
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        # Explorar vecinos
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            # Actualizar si encontramos un camino más corto
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                caminos[vecino] = caminos[nodo_actual] + [vecino]
                heapq.heappush(cola, (distancia, vecino))
    
    return distancias, caminos

# Grafo de ejemplo (modificable)
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Configuración
nodo_inicio = 'A'  # Puedes cambiar este valor

# Ejecutar algoritmo
distancias, caminos = dijkstra(grafo, nodo_inicio)

# Mostrar resultados
print("--- Resultados del Algoritmo de Dijkstra ---")
print(f"Nodo inicial: {nodo_inicio}\n")

print("Distancias mínimas:")
for nodo, distancia in distancias.items():
    print(f"{nodo}: {distancia}")

print("\nCaminos más cortos:")
for nodo, camino in caminos.items():
    print(f"{nodo}: {' → '.join(camino)}")