## Gift Wrapping
É o algoritmo mais simples para solucionar o problema do fecho convexo. Uma analogia muito boa a ele é a ideia de embrulhar um presente, como o nome sugere.

### Passos
1. Decidir qual ponto começar $A$, que temos certeza que está no fecho convexo. Por convenção, vamos escolher o da extrema esquerda.
2. Fazemos uma iteração nos outros pontos, da seguinte maneira:
    - Selecionamos um ponto inicial $B$
    - Agora selecionamos outro ponto $P$
    - Checamos se $P$ esta a esquerda de $\overline{AB}$
    - Se estiver, ele vira o nosso novo candidato e avançamos para o próximo candidato $P$
    - Retornamos por fim, o último ponto, que será o ponto mais a esquerda do ponto $A$
    - Atualizamos quem é $A$ e repetimos o loop até voltamos para o ponto inicial

### Complexidade
Como o algoritmo faz uma iteração por todos os pontos da borda e em cada iteração dessa ele itera por todos os pontos, a sua complexidade é de $O(nh)$ sendo $h$ o número de pontos extremos.
No pior caso, $n = h \implies O(n^2)$