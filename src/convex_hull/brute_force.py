from src.geometry.utils import orientation, random_points2D
from src.geometry import Point2D

# variáveis ambiente necessárias
points = random_points2D(10)
start = min(points, key= lambda p : p.x)
current = start
hull = [start]

def find_next_point(now, points):
    candidate = points[0]

    for p in points:
        if orientation(now, candidate, p) < 0 or candidate == now:
            candidate = p

    return candidate
    
# loop principal do algoritmo
while True:
    current = find_next_point(current, points)
    if current == start:
        break
    hull.append(current)

from src.convex_hull.utils import plot_convex_hull
print(hull)
plot_convex_hull(points,hull)