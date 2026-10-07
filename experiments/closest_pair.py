# teste de casos degenerados
#

nome_do_algoritmo = "floor_grid"
plot_all = False
#

import importlib
modulo = importlib.import_module(
    f"src.closest_pair.{nome_do_algoritmo}"
)
run = modulo.run

from src.geometry.utils import random_points2D

# teste perfomance
from experiments.utils import test_perfomance
def test_run(n):
    p = random_points2D(n)
    return run(p)

test_perfomance(test_run, n_max=200,name=nome_do_algoritmo, plot=True)