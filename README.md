# Tarefa 13 — Normal, t de Student, qui-Quadrado e F de Fisher

Repositório pertencente ao grupo.

Este repositório reúne o notebook da **Tarefa 13** de Bioestatística, que apresenta a investigação de distribuições contínuas de probabilidade (**Normal**, **t de Student**, **qui-quadrado** e **F de Fisher**) aplicadas a dados morfológicos reais da flor de *Iris* (*Iris spp.*).

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amelyssaeu-ab/bio-dkm/blob/main/tarefa13_Python_Ciencias_Biologicas.ipynb)

## Integrantes

| Nome | nº USP |
|---|---|
| Drielly Mathias Albertti | 16831084 |
| Kawana Ganeo de Carvalho | 14669691 |
| Melyssa Ponce Lopes | 16831017 |

## Objetivo

Investigar como as distribuições Normal, t de Student, qui-quadrado e F de Fisher ajudam a responder perguntas biológicas reais, distinguindo medidas biológicas de organismos individuais de estatísticas amostrais modeladas, apresentando as equações teóricas, análises de sensibilidade de parâmetros, gráficos com áreas sombreadas e cálculos de probabilidades acumuladas, pontuais e percentis em Python.

## Conteúdo do notebook

O arquivo [`tarefa13.ipynb`](tarefa13_Python_Ciencias_Biologicas.ipynb) está organizado em quatro tópicos principais:

1. **Escolha da base de dados e contextualização:** descrição da base *Iris*, identificação das variáveis morfológicas, unidade experimental e formulação da pergunta biológica orientadora.
2. **Pesquisa teórica e gráficos de densidade:** apresentação das fórmulas das densidades (PDF), parâmetros, definições, limitações de aplicação e sensibilidade visual variando parâmetros em Python para:
   - **Distribuição Normal:** modelagem de medidas contínuas individuais (comprimento de pétalas de *Iris-setosa*).
   - **Distribuição t de Student:** modelagem de estatísticas de médias amostrais padronizadas (teste de hipótese para *Iris-versicolor*).
   - **Distribuição qui-quadrado ($\chi^2$):** modelagem da variância amostral.
   - **Distribuição F de Fisher:** modelagem da razão de variâncias entre duas populações (*Iris-versicolor* vs. *Iris-setosa*).
3. **Probabilidades e Percentis em Python:** cálculos de probabilidades acumuladas, intervalos, cauda superior e percentis via `scipy.stats`, acompanhados de gráficos com áreas sob a curva sombreadas.
4. **Discussão e Conclusões:** análise crítica sobre as condições necessárias para aplicação das distribuições, distinção entre dados observados e estatísticas modeladas e limitações da base amostral.

## Dados utilizados

Os dados vêm do repositório público **UCI Machine Learning Repository**, base clássica criada por R. A. Fisher (1936).

| Variável | Descrição | Unidade |
|---|---|---|
| `sepal_length` | Comprimento da sépala | cm |
| `sepal_width` | Largura da sépala | cm |
| `petal_length` | Comprimento da pétala | cm |
| `petal_width` | Largura da pétala | cm |
| `species` | Espécie (*Iris-setosa*, *Iris-versicolor*, *Iris-virginica*) | Categórica (50 indivíduos/espécie) |

- **Instituição responsável:** UCI Machine Learning Repository / Yale University.
- **Data de Acesso:** 06 de Outubro de 2026.
- **Total de observações:** 150 plantas (50 por espécie), sem dados ausentes.

## Como executar

**No Google Colab:** clique no botão "Abrir no Colab" no início deste README.

**Localmente:**

```bash
git clone [https://github.com/amelyssaeu-ab/bio-dkm.git](https://github.com/amelyssaeu-ab/bio-dkm.git)
cd bio-dkm
pip install numpy pandas matplotlib seaborn scipy jupyter
jupyter notebook tarefa13.ipynb
```

**Bibliotecas:** `numpy`, `pandas`, `matplotlib`, `seaborn` e `scipy`.

## Referências

BUSSAB, Wilton de O.; MORETTIN, Pedro A. Estatística básica. 9. ed. São Paulo: Saraiva, 2017.

FISHER, Ronald A. The use of multiple measurements in taxonomic problems. Annals of Eugenics, London, v. 7, n. 2, p. 179-188, 1936.

SCIPY COMMUNITY. SciPy User Guide: scipy.stats (norm, t, chi2, f). Disponível em: https://docs.scipy.org/doc/scipy/reference/stats.html. Acesso em: 07 out. 2026.

UCI MACHINE LEARNING REPOSITORY. Iris Dataset. Irvine: University of California, School of Information and Computer Science, 1988. Disponível em: https://archive.ics.uci.edu/ml/datasets/iris. Acesso em: 07 out. 2026.
