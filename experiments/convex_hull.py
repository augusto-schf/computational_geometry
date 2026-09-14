# teste de casos degenerados
#

nome_do_algoritmo = "monotone_chain"
plot_all = False
#

import importlib
modulo = importlib.import_module(
    f"src.convex_hull.{nome_do_algoritmo}"
)
run = modulo.run

from src.geometry.utils import random_points2D
from src.convex_hull.utils import plot_convex_hull

# 3 pontos colineares
try:
    points = random_points2D(2)
    points += [(points[0] + points[1])*0.5]
    hull = run(points)
    if plot_all:
        plot_convex_hull(points,hull)
except Exception as Error:
    print(f"Erro    - {nome_do_algoritmo} - (1) 3 pontos colineares")
    print(Error)
else:
    print(f"Sucesso - {nome_do_algoritmo} - (1) 3 pontos colineares")

# 2 pontos iguais
try: 
    points = random_points2D(10)
    points += [points[0], points[5]]
    hull = run(points)
    if plot_all:
        plot_convex_hull(points,hull)
except Exception as Error:
    print(f"Erro    - {nome_do_algoritmo} - (1) 2 pontos iguais")
    print(Error)
else:
    print(f"Sucesso - {nome_do_algoritmo} - (1) 2 pontos iguais")

# 20 pontos
try: 
    points = random_points2D(20)
    hull = run(points)
    if plot_all:
        plot_convex_hull(points,hull)
except Exception as Error:
    print(f"Erro    - {nome_do_algoritmo} - (1) 20 pontos")
    print(Error)
else:
    print(f"Sucesso - {nome_do_algoritmo} - (1) 20 pontos")

# teste perfomance
from experiments.utils import test_perfomance
def test_run(n):
    p = random_points2D(n)
    return run(p)

test_perfomance(test_run, n_max=5000,name=nome_do_algoritmo)