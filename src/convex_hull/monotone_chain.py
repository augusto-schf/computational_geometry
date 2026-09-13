from src.geometry.utils import orientation, random_points2D
from src.geometry.Point2D import Point2D
from math import atan2

def run(points = random_points2D(10)):
    # variáveis ambiente necessárias
    # remove duplicatas e organiza os pontos da esquerda em cima para direita embaixo
    points = sorted(list(set(points)), key = lambda p : (p.x, p.y))
    
    p0 = points[0] # escolhe o primeiro ponto do upper_bound
    remaining = [p for p in points if p != p0]
    upper_bound = [p0]

    for p in remaining: # caso tenha que rotacionar para a direita, remove o do meio
        while len(upper_bound) > 1 and orientation(upper_bound[-2], upper_bound[-1], p) > 0:
            upper_bound.pop()
        upper_bound.append(p)

    rpoints = reversed(points)
    p0 = points[0]
    remaining = [p for p in points if p != p0]
    lower_bound = [p0]

    for p in remaining: # caso tenha que rotacionar para a esquerda, remove o do meio
        while len(lower_bound) > 1 and orientation(lower_bound[-2], lower_bound[-1], p) < 0:
            lower_bound.pop()
        lower_bound.append(p)

    # junta as duas listas removendo a duplicata
    hull = lower_bound[1:] + list(reversed(upper_bound[:-1]))
    return hull