from src.geometry.utils import random_points2D
from src.closest_pair.brute_force import run as run_brute_force
from src.closest_pair.utils import plot_closest_pair

def run(points):
    # caso base (n <= 3)
    if len(points) <= 3:
        return run_brute_force(points)
    
    # ordenar por x
    points = sorted(points, key=lambda p : p.x)

    # encontrar o ponto do meio
    middle_point_idx = len(points) // 2
    middle_point = points[middle_point_idx]

    # separar em esquerda e direita
    left_part  = points[:middle_point_idx]
    right_part = points[middle_point_idx:]

    # pegar o minimo da esquerda e o minimo da direita
    min_left, points_left = run(left_part)
    min_right, points_right = run(right_part)
    delta = min(min_left, min_right)

    # filtrar os pontos que se encontram mais próximos que o delta
    points2check = sorted(filter(lambda p : abs(p.x - middle_point.x) <= delta, points), key=lambda p : p.y)
    min_center = delta
    closest_pair = points_right if min_right < min_left else points_left

    # percorre os pontos válidos
    for i in range(len(points2check)):
        p1 = points2check[i]
        # checa os próximos pontos da sequência a até no máximo 7 pontos de distância
        for j in range(i+1, min(i+8, len(points2check))):
            p2 = points2check[j]
            d = p1.distance_to_squared(p2)**0.5

            # se a distância for a nova menor, atualiza as informações atuais
            if d < min_center:
                min_center = d
                closest_pair = (p1,p2)

    return min(min_left, min_right, min_center), closest_pair