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