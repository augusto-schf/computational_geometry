from src.geometry.utils import random_points2D, orientation
from src.convex_hull.utils import plot_convex_hull

# optimização de convex hull usando orientação de pontos numa reta
def optimize(points):
    # encontro os pontos extremos que com certeza estão no convex hull
    left   = points[0]
    right  = points[0]
    up     = points[0]
    bottom = points[0]

    # O(n)
    for p in points:
        if p.x < left.x or p.x == left.x and p.y > left.y:
            left = p

        if p.x > right.x or p.x == right.x and p.y > right.y:
            right = p

        if p.y > up.y or p.y == left.y and p.x < up.x:
            up = p

        if p.y < bottom.y or p.y == bottom.y and p.x < bottom.x:
            bottom = p

    # itero, se o ponto estiver no poligono contendo os quatro pontos extremos, então ele não
    # faz parte do convex hull com certeza, então podemos apaga-lo da lista
    result = []
    for p in points:
        if p in [left, right, up, bottom]:
            result.append(p)
        elif orientation(bottom, right, p) < 0 or orientation(right, up, p) < 0 or orientation(up, left, p) < 0 or orientation(left, bottom, p) < 0:
            result.append(p)

    # retornamos o resultado final, dessa forma diminuimos o n de n log n da complexidade
    # com um simples processamento prévio de complexidade n
    # ficamos com n + h log h, com h = total - pontos ignorados
    return result