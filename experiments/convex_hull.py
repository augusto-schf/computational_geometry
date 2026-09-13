# teste de casos degenerados
from src.convex_hull.monotone_chain import run
nome_do_algoritmo = "Monotone_Chain"

from src.geometry.utils import random_points2D
from src.convex_hull.utils import plot_convex_hull

# 3 pontos colineares
try:
    points = random_points2D(2)
    points += [(points[0] + points[1])*0.5]
    plot_convex_hull(points, run(points))
except Exception as Error:
    print(f"Erro    - {nome_do_algoritmo} - (1) 3 pontos colineares")
    print(Error)
else:
    print(f"Sucesso - {nome_do_algoritmo} - (1) 3 pontos colineares")

# 2 pontos iguais
try: 
    points = random_points2D(10)
    points += [points[0], points[5]]
    plot_convex_hull(points, run(points))
except Exception as Error:
    print(f"Erro    - {nome_do_algoritmo} - (1) 2 pontos iguais")
    print(Error)
else:
    print(f"Sucesso - {nome_do_algoritmo} - (1) 2 pontos iguais")

# 20 pontos
try: 
    points = random_points2D(20)
    plot_convex_hull(points, run(points))
except Exception as Error:
    print(f"Erro    - {nome_do_algoritmo} - (1) 20 pontos")
    print(Error)
else:
    print(f"Sucesso - {nome_do_algoritmo} - (1) 20 pontos")