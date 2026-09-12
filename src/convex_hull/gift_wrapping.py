from src.geometry.utils import orientation, random_points2D
from src.geometry import Point2D

def run(points = random_points2D(10)):
    start = min(points, key= lambda p : p.x) # começo
    current = start # ponto atual inicial
    hull = [start] # o fecho convexo final

    # função auxiliar
    def find_next_point(now, points):
        candidate = points[0] # candidato inicial

        for p in points: # itera os pontos
            # caso o novo ponto esteja a esquerda do atual-candidato,
            # atualiza o candidato por ele
            if orientation(now, candidate, p) > 0 or candidate == now:
                candidate = p

        return candidate

    # loop principal do algoritmo
    while True:
        # procura o próximo ponto
        current = find_next_point(current, points)
        # caso ele seja o inicial, finalizamos o algoritmo
        if current == start:
            break
        hull.append(current)
    return hull