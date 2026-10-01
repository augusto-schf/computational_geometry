## Monotone Chain
Algoritmo que separa os pontos em duas metades, a metade superior e a metade inferior. Depois de montar o fecho convexo das duas partes, junta elas formando o resultado final. 

### Passos
1. Organizamos os pontos pelo eixo X
2. Selecionamos o ponto mais a esquerda e separamos os pontos em duas metades
3. Iteramos a lista de pontos ordenados da metade superior seguinte maneira:
    - Partimos para o próximo ponto a direita e salvamos
    - Pegamos o próximo e checamos se dado esses últimos 3 pontos, acaba formando uma ponta concâva ou não
    - Se formar, removemos o ponto do meio para remover essa concavidade
    - Prosseguimos para o próximo ponto
4. Fazemos uma iteração análoga usando o ponto mais a direita, em direção a esquerda, por baixo.
5. Juntamos as duas metades e temos o resultado final
### Complexidade
Como a maioria dos algoritmos do problema, o maior dilema é a ordenação $O(nlogn)$. Pois a iteração executa duas vezes um loop de $\frac{n}{2}$ passos. Logo o algoritmo executa em tempo $O(nlogn + n) = O(nlogn)$