from datetime import datetime
from time import perf_counter
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

def parse_csv_file(name): # reimporta arquivo .csv baseado no nome
    folder = Path("results")
    files = folder.glob("*.csv") # busca o primeiro arquivo que contém o nome
    for file in files:
        if name.lower() in file.stem.lower():
            with open(file, "r", encoding="utf-8") as arquivo:
                lines = arquivo.readlines()
                data = list(map(lambda l : l.replace(' ', '').split('|'), lines))
                return data

def plot_csv_data(data, interval=50, fit_curve=True, curve_func=lambda x : x * np.log(x)):
    x = np.array([float(c[1]) for c in data[::interval]])
    y = np.array([float(c[2]) for c in data[::interval]])

    mean = np.mean(y)
    std = np.std(y) # tira a média e o desvio padrão

    mask = np.abs(y - mean) < 5 * std ## mascara para filtrar os dados que estão entre 3 sigmas da média

    x = x[mask]
    y = y[mask]

    z = curve_func(x) # fita a curva baseado nos dados coletados experimentalmente
    a, b = np.polyfit(z, y, 1)
    y_nlogn = a * z + b

    plt.scatter(x,y, label="Dados") # plota ambas as curvas, a dos dados e a fitada
    plt.plot(x,y_nlogn, color="red", label=r"Curva Fitada")
    plt.grid()

    plt.legend()
    plt.show()

plot_csv_data(parse_csv_file("gift_wrapping"))
def save_csv_data(name, data):
    '''Salva dados em .CSV

    args:
        string : Nome do arquivo a ser salvo
        list [string] : Lista com todas linhas a serem salvas no .CSV
    '''
    now = datetime.now()
    tempo = now.strftime("%d_%m_%y %H_%M_%S")

    with open(f"results/{name}_{tempo}.csv", "w", encoding="utf-8") as arquivo:
        arquivo.write(data)

def test_perfomance(func, n_min = 4, n_max = 1000, name='nao_providenciado'):
    '''Testa a performance de algum algoritmo e salva em um .CSV dados
    sobre o tempo de execução do algoritmo dado algum N

    args:
        function : uma função para testar o desempenho, ela deve receber
        um argumento N representando o tamanho N do problema/algoritmo
        int : representa o N mínimo para o teste, o padrão é 4
        int : represenat o N máximo para o teste, o padrão é 1000
        string : o nome do arquivo para salvar na pasta /results/
    '''
    results = []

    for n in range(n_min, n_max+1):
        start = perf_counter()
        func(n) # executa a função e salva o tempo de execução
        end = perf_counter()
        dt = end-start

        results.append(f"{name:^15} | {n:^10} | {dt:^15.10f}")
        print(results[-1]) # salva e printa o resultado

    save_csv_data(name, '\n'.join(results)) # salva como .CSV na pasta /results/