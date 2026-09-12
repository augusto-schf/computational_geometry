from src.geometry.utils import orientation, random_points2D
from src.geometry.Point2D import Point2D
from math import atan2

# variáveis ambiente necessárias
points = random_points2D(10) # pontos aleatórios
p0 = min(points, key= lambda p : (p.y, p.x)) # começo
hull = [p0] # o fecho convexo final

def polar_angle_and_dist(p : Point2D):
    angle = atan2(p[1] - p0[1], p[0] - p0[0])
    dist  = Point2D.distance_squared(p0, p)
    return (angle, dist)

remaining = [p for p in points if p != p0]
remaining.sort(key=polar_angle_and_dist)

for p in remaining:
    while len(hull) > 1 and orientation(hull[-2], hull[-1], p) < 0:
        hull.pop()
    hull.append(p)

# plot do gráfico
from src.convex_hull.utils import plot_convex_hull
print(hull)
plot_convex_hull(points,hull)