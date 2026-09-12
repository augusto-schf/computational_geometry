## Graham Scan
Algoritmo que depende da velocidade de ordenação da lista de ângulos e comumente usado para solucionar o problema em casos bidimensionais.

### Passos
1. Decidir qual ponto começar $A$, que temos certeza que está no fecho convexo. Por convenção, vamos escolher o ponto inferior.
2. Selecionamos os outros pontos e os ordenamos em relação ao ângulo (critério de desempate é a distância) com o ponto inicial.
3. Iteramos a lista de pontos ordenados da seguinte maneira:
    - Criamos uma stack com o ponto inicial $A$ e o ponto com o menor ângulo $B$
    - Avançamos para o próximo ponto $C$, se ele estiver a direita de $\overline{AB}$, então removemos $B$ da stack
    - Agora fazemos isso para o próximo ponto, mas agora $C$ se tornou $B$
    - Caso $C$ estiver na esquerda de $\overline{AB}$, fazemos $B$ se tornar o novo $A$ e $C$ se tornar o novo $B$
    - Avançamos para o próximo ponto até chegar onde começamos
### Complexidade
O principal desafio desse algoritmo é a ordenação, que possui complexidade $O(nlogn)$. Pois a iteração é de complexidade $O(n)$, onde só passamos por cada ponto uma vez.