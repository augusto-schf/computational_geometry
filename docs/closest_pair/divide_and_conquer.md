## Divide & Conquer
Algoritmo que usa o método dividir e conquistar, para otimizar o algoritmo do _Brute Force_

### Passos
1. Ordenamos os pontos pelo eixo X
2. Selecionamos o ponto intermediário (o ponto do meio)
3. Separamos os outros pontos em duas metades, a da esquerda do ponto central e a da direita
4. Fazemos uma recursão em cada metade como se fossem novas instâncias do problema
5. Sabemos com certeza que, se existir um par próximo que utilize um ponto da esquerda e um da direita, a sua distância tem de ser menor que $min(esquerda)$ e $min(direita)$, ou seja $min(global) \le \delta = min(min(esq), min(dir))$, então podemos selecionar os pontos que estão a no máximo uma distância $2\delta$ do centro
6. Agora fazemos força bruta dentre esses pontos
7. Selecionamos o par mais próximo entre os pares da esquerda, os pares da direita e os pares que são mútuos.
### Complexidade
Usa o Teorema Mestre. Não sei justificar.