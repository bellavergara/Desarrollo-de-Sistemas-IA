
"""
# Examen de Desarrollo de Sistemas IA


Problema 1:
Se tienen dos jarras de agua de capacidades X y Y litros.
Se pueden realizar las siguientes acciones:
● Llenar una jarra completamente.
● Vaciar una jarra.
● Pasar agua de una jarra a otra hasta que una se vacíe o la otra se llene.
El estado del sistema se representa como (a, b) donde a es el contenido de la jarra X y b el
de la jarra Y.
El estado inicial es (0, 0).
Objetivo: Usando DFS, encontrar si es posible medir exactamente Z litros en alguna de las
jarras y, en caso afirmativo, devolver la secuencia de movimientos.
"""
from collections import deque

def resolver_jarras(x_cap, y_cap, objetivo):
    visitados = set()
    camino = []

    def dfs(estado):
        if estado in visitados:
            return False
        visitados.add(estado)
        camino.append(estado)

        a, b = estado
        if a == objetivo or b == objetivo:
            return True

        # movimientos: llenar, vaciar, pasar
        movs = [
            (x_cap, b),  # llenar X
            (a, y_cap),  # llenar Y
            (0, b),      # vaciar X
            (a, 0)       # vaciar Y
        ]

        # pasar de X a Y
        t = min(a, y_cap - b)
        movs.append((a - t, b + t))

        # pasar de Y a X
        t = min(b, x_cap - a)
        movs.append((a + t, b - t))

        for nuevo in movs:
            
            if dfs(nuevo):
                return True

        camino.pop()
        return False

    if dfs((0, 0)):
        return camino
    else:
        return None


"""
Problema 2:
Un caballero está atrapado en un calabozo representado por una matriz m x n donde cada
celda puede contener:
● Un número negativo que representa daño(pérdida de salud),
● Un cero que representa una celda vacía, o
● Un número positivo que representa orbes mágicos que aumentan su salud.
El caballero comienza en la esquina superior izquierda (posición (0,0)) y debe llegar hasta
la esquina inferior derecha (m-1, n-1) para rescatar a la princesa.
Sólo puede moverse hacia la derecha o hacia abajo en cada paso.
Si en cualquier momento la salud del caballero cae a cero o menos, muere y el camino no
es válido.
El objetivo es determinar la mínima salud inicial que debe tener el caballero para garantizar
que puede llegar al final con vida.
"""

def salud_minima_calabozo(matriz):
    m = len(matriz)
    n = len(matriz[0])
    dp = [[0] * n for _ in range(m)]

    # partir desde la meta
    dp[-1][-1] = max(1, 1 - matriz[-1][-1])

    # ultima fila
    for j in range(n - 2, -1, -1):
        dp[-1][j] = max(1, dp[-1][j + 1] - matriz[-1][j])

    # ultima columna
    for i in range(m - 2, -1, -1):
        dp[i][-1] = max(1, dp[i + 1][-1] - matriz[i][-1])

    # rellenar
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            mejor_sig = min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] = max(1, mejor_sig - matriz[i][j])

    return dp[0][0]


"""
Problema 3:
Se cuenta con un conjunto de estaciones de servicio ubicadas en un plano cartesiano.
Cada estación tiene una cantidad fija de gasolina que se repone al vehículo al llegar a ella.
Un vehículo debe viajar de una estación inicial a otra estación destino pasando por
estaciones intermedias si es necesario. El vehículo consume una cantidad de gasolina
específica para desplazarse entre estaciones conectadas directamente.
Se proporciona:
Un grafo donde cada nodo representa una estación de servicio con sus coordenadas (x, y)
y la cantidad de gasolina que repone.
Las aristas del grafo indican la conexión entre estaciones y el consumo de gasolina
necesario para viajar entre ellas.
Objetivo:
Diseñar un algoritmo que determine si es posible llegar desde una estación inicial a una
estación destino sin quedarse sin gasolina en el camino, considerando que el vehículo
comienza con un tanque vacío y repone gasolina solo al llegar a una estación. Además, el
algoritmo debe devolver una ruta válida en caso de existir.


"""
def ruta_con_gasolina(stations, costs, inicio, destino):
    start_gas = stations[inicio]['gas'] if inicio in stations else 0
    q = deque([(inicio, start_gas, [inicio])])
    visitados = set()

    while q:
        actual, gas, camino = q.popleft()
        if actual == destino:
            return camino

        estado = (actual, gas)
        if estado in visitados:
            continue
        visitados.add(estado)

        # explorar vecinos
        for vecino, consumo in costs.get(actual, {}).items():
            if gas >= consumo:
                nuevo_gas = gas - consumo + stations[vecino]['gas']
                q.append((vecino, nuevo_gas, camino + [vecino]))
            else:
                # si no alcanza, no podemos ir a ese vecino ahora
                pass

    return None


"""
Problema 4:
Se tiene una red de transporte representada como un grafo no dirigido.
● Cada nodo representa un almacén.
● Cada arista representa una ruta directa entre dos almacenes, con un valor entero
que indica el peso máximo permitido para los vehículos en esa ruta.
Un camión de carga debe transportar un paquete desde un almacén origen hasta un
almacén destino.
El camión tiene un peso fijo W (que incluye el paquete).
El camión sólo puede pasar por rutas en las que el límite de peso sea mayor o igual a W.
Objetivo: Usando búsqueda por anchura o profundidad, determinar si existe un camino
válido desde el almacén origen hasta el almacén destino que respete las restricciones de
peso. En caso afirmativo, devolver una ruta posible.
"""

def ruta_valida_peso(grafo, origen, destino, peso):
    q = deque([(origen, [origen])])
    visitados = set()

    while q:
        actual, camino = q.popleft()
        if actual == destino:
            return camino
        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino, limite in grafo.get(actual, {}).items():
            if limite >= peso:
                q.append((vecino, camino + [vecino]))

    return None


# ejercicios de repaso examen" 