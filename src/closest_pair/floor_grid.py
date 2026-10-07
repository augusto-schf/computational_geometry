from src.geometry.utils import random_points2D
from math import floor
from random import shuffle

def create_dict (points, delta):
    # cria o dicionário do grid
    grid = {}
    #adiciona cada ponto na sua célula correspondente
    for p in points:
        coords_in_grid = (floor(p.x / delta), floor(p.y / delta))
        grid.setdefault(coords_in_grid, []).append(p)

    return grid

def nestedLoop(grid, delta, pair):
# para cada célula do GRID
    for index, cell in grid.items():
        # percorre todos os pontos dentro da célula
        adjacent_cells = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                adjacent_cells.append(grid.get((index[0] + i, index[1] +  j), []))
        
        for i in range(len(cell)):
            p_0 = cell[i]
            # percore todas células adjacentes no grid
            for cell_ in adjacent_cells:
                #para cada ponto percorre todos os seguintes pontos
                for j in range(len(cell_)):
                    p_1 = cell_[j]
                    # se estiver comparando o mesmo ponto com ele mesmo, retorna
                    if p_0 == p_1:
                        continue
                
                    dis = p_0.distance_to(p_1)
                    if dis < delta:
                        # se a distância for zero, para o loop
                        changed = True if dis != 0 else False
                        delta = dis
                        pair = (p_0,p_1)
                        return delta, pair
                    
    return delta, pair
def run(points):
    if len(points) < 2:
        return 0

    # remove pontos duplicados
    points = list(set(points))
    # embaralha os pontos
    shuffle(points)

    delta = points[0].distance_to(points[1])
    pair = (points[0], points[1])

    if len(points) == 2:
        return delta, pair
    
    changed = True

    while changed:
        # cria o grid
        grid = create_dict(points, delta)
        # para checar se mudou o delta ou não
        delta_, pair = nestedLoop(grid, delta, pair)

        if delta_ == delta:
            changed = False
        else:
            delta = delta_

    return delta, pair