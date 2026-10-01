## Brute Force
Algoritmo da força bruta aplicado no problema de encontrar o par mais próximo.

### Passos
1. Percorremos todos os pontos com um loop
2. Para cada ponto, verificamos a sua distância com todos os outros pontos
3. Assim, encontramos a menor distância entre todos os pontos
### Complexidade
Se o algoritmo ainda for optimizado, a primeira iteração do primeiro loop executa $O(n-1)$, a segunda iteração executa $O(n-2)$, até chegarmos em $O(1)$. Somando os passos temos: $O(n-1) + O(n-2) + ... + O(1)$ que forma uma progressão aritmética, de soma total igual a $\frac{n(n-1)}{2} = \frac{n^2+n}{2}$. Chegamos assim, a uma complexidade de $O(n^2)$