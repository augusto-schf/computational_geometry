from src.geometry.utils import random_points2D
from src.closest_pair.brute_force import run as run_brute_force

def run(points):
    # ordena os pontos usando a coordenada X como referência primária 
    # e a coordenada Y como referência secundária
    points = sorted(points, key=lambda p: (p.x, p.y))

    # define o ponto mais intermediário entre todos
    middle_index = int(len(points) * 0.5)
    middle_point = points[middle_index]

    # separa todos pontos usando o ponto intermediário como divisor
    first_part = points[middle_index:]
    second_part = points[:middle_index]

    # encontra o mínimo da esquerda e o mínimo da direita
    min_left = run_brute_force(first_part)
    min_right = run_brute_force(second_part)

    # define o mínimo entre os dois
    epsilon = min(min_left[0], min_right[0])

    # verifica quais pontos próximos da fronteira entre esquerda e direita
    # estão aptos a serem utilizados
    to_check = []
    for p in first_part:
        if middle_point.x - epsilon <= p.x <= middle_point.x + epsilon:
            to_check.append(p)

    # se tivermos mais que dois ponto na fronteira, checamos todas distâncias entre eles
    # e retornamos a menor distância encontrada no geral
    if len(to_check) >= 2:
        min_middle = run_brute_force(to_check)
    else:
        return min_right if min_right[0] < min_left[0] else min_left
 
    if min_middle[0] < epsilon:
        return min_middle
    else:
        return min_right if min_right[0] < min_left[0] else min_left