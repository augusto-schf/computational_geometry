from src.geometry.utils import random_points2D

def run(points):
    min_distance = points[0].distance_to_squared(points[1])
    point_a = points[0]
    point_b = points[1]

    for p in points:
        for p_ in points:
            if p == p_:
                continue

            if p.distance_to_squared(p_) < min_distance:
                point_a = p
                point_b = p_
                min_distance = p.distance_to_squared(p_)

    return (min_distance**0.5, point_a, point_b)