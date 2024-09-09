import matplotlib.pyplot as plt #Instalar la librería matplotlib con: pip install matplotlib
import numpy as np
from collections import deque

# Definimos el estado final deseado
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Movimientos posibles del puzzle
MOVES = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

# Función para encontrar la posición del '0' (el espacio vacío)
def find_zero(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return i, j

# Función para mover el espacio vacío
def move(state, direction):
    new_state = [row[:] for row in state]
    zero_row, zero_col = find_zero(state)
    move_row, move_col = MOVES[direction]
    new_row, new_col = zero_row + move_row, zero_col + move_col
    
    if 0 <= new_row < 3 and 0 <= new_col < 3:
        # Intercambiar el valor
        new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
        return new_state
    return None

# Función para verificar si el estado es el objetivo
def is_goal(state):
    return state == goal_state

# Búsqueda en profundidad (DFS)
def dfs(initial_state):
    stack = [(initial_state, [])]
    visited = set()
    
    while stack:
        state, path = stack.pop()
        state_tuple = tuple(tuple(row) for row in state)
        
        if state_tuple in visited:
            continue
        
        visited.add(state_tuple)
        
        if is_goal(state):
            return path
        
        for direction in MOVES:
            new_state = move(state, direction)
            if new_state and tuple(tuple(row) for row in new_state) not in visited:
                stack.append((new_state, path + [new_state]))

    return None

# Función para visualizar el tablero
def plot_puzzle(state):
    plt.imshow(state, cmap="Blues", interpolation="nearest")
    plt.xticks([]), plt.yticks([])
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0:
                plt.text(j, i, str(state[i][j]), ha="center", va="center", color="black", fontsize=20)
    plt.show()

# Estado inicial del puzzle
initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [7, 8, 6]]

# Resolver el puzzle
solution = dfs(initial_state)

# Mostrar el estado inicial
print("Estado inicial:")
plot_puzzle(initial_state)

# Mostrar los movimientos hasta la solución
if solution:
    for i, step in enumerate(solution):
        print(f"Movimiento {i + 1}:")
        plot_puzzle(step)
else:
    print("No se encontró solución.")
