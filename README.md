# Geometria Computacional
Repositório dedicado ao estudo de Geometria Computacional e de seus algoritmos e métodos principais, no contexto de uma Iniciação Científica de Estudo Orientado.

## Objetivos
- Estudar fudamentos de complexidade e geometria computacional;
- Compreender os principais problemas e algoritmos da área;
- Analisar a complexidade e vantagens de cada algoritmo estudado;
- Implementar algoritmos e realizar experimentos computacionais;
- Desenvolver práticas de iniciação científica.

## Conteúdo
### Fundamentos
- Complexidade computacional, $O(f)$, $\Omega(f)$ e $\Theta(f)$
- Geometria computacional, implementação de objetos geométricos em código
- Abordagem de visualização de dados usando lib's como _NumPy_ e _MatPlotLib_
  
### Problemas Estudados
- Fecho Convexo (convex hull)
    - Jarvis March (Gift Wrapping) - $O(nh)$
    - Graham Scan - $O(nlogn)$
    - Andrew's Monotone Chain - $O(nlogn)$
- Localização de Pontos

## Estrutura
```text
.
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/   -- Documentos de markdown
│   ├── notas/
│   ├── referencias.md
│   └── diario.md
│
├── src/    -- Códigos implementados
│   ├── geometry/
│   └── convex_hull/
│
├── experiments/ -- Experimentos com os códigos
│   └── convex_hull/

└── results/  -- Resultados e dados coletados
    ├── figures/
    └── data/
```

####  Autor: 
Augusto Schaefer Huff, discente no curso de graduação no IMPA Tech

#### Orientador:
Prof. Dr. Emílio Vital Brazil

## Referências

1. **Convex hull algorithms.** Wikipedia, The Free Encyclopedia. Disponível em: <https://en.wikipedia.org/wiki/Convex_hull_algorithms>. Acesso em: 13 set. 2026.

2. **Convex hull.** Wikipedia, The Free Encyclopedia. Disponível em: <https://en.wikipedia.org/wiki/Convex_hull>. Acesso em: 13 set. 2026.

3. FIGUEIREDO, Luiz Henrique de; CARVALHO, Paulo Cezar Pinto. **Notas de Geometria Computacional.** Instituto de Matemática Pura e Aplicada (IMPA), 2005. Versão preliminar para uso pessoal, texto atualizado em 7 de março de 2005.