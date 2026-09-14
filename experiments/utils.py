from datetime import datetime
from time import perf_counter

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

def test_perfomance(func, n_min=4, n_max = 1000, name='nao_providenciado'):
    results = []

    for n in range(n_min, n_max):
        start = perf_counter()
        func(n)
        end = perf_counter()
        dt = end-start

        results.append(f"{name:^15} | {n:^10} | {dt:^15.10f}")
        print(results[-1])

    save_csv_data(name, '\n'.join(results))