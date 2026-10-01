## Delete Point
Algoritmo de optimização do problema do fecho convexo descartando pontos que essencialmente não fazem parte do fecho final.

### Passos
1. Organizamos os pontos no eixo X e no eixo Y
2. Selecionamos os pontos que com certeza estão no fecho, que são os extremos em cada direção (esq. dir. cima baixo)
3. Formamos um quadrilátero com os quatro pontos encontrados
4. Percorremos os outros pontos e verificamos quais deles se encontram dentro do quadrilátero
5. Removemos os pontos que se encontram no interior do quadrilátero
6. Agora temos um número de candidatos ao fecho muito menor, a pouco custo
### Complexidade
O fator mais pesado dessa optimização é a ordenação em $O(nlogn)$, mas que pode ser aproveitada por algoritmos como o _Monotone Chain_. Assim, o seu aproveitamento em alguns casos pode ser muito expressivo. Apesar de existirem casos degenerados, como por exemplo uma circunferência, onde nenhum ponto se encontra no interior do quadrilátero.