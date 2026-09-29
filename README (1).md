# Variáveis Aleatórias em Biologia: Bernoulli, Binomial e Poisson

Trabalho em grupo da Tarefa 11 de Bioestatística. Notebook em Python com conceitos introdutórios de Probabilidade aplicados a situações biológicas.

> Os trechos marcados com **[PREENCHER]** dependem de informações do grupo e devem ser completados antes da entrega.

## Integrantes (ordem alfabética)

- Drielly Mathias Albertti (nº USP 16831084)
- Kawana Carvalho (nº USP 14669691)
- Melyssa Ponce Lopes (nº USP 16831017)

**Disciplina / docente / instituição:** [PREENCHER]

## Objetivo do notebook

Apresentar e exemplificar, com foco em Biologia, o conceito de variável aleatória e os modelos de Bernoulli, Binomial e Poisson, interpretando biologicamente os resultados de cálculos e simulações.

## Conteúdos abordados

Arquivo principal: [`tarefa11_variaveis_aleatorias_biologia.ipynb`](tarefa11_variaveis_aleatorias_biologia.ipynb)

1. Variável aleatória
2. Variáveis aleatórias discretas e contínuas
3. Modelo de Bernoulli
4. Modelo Binomial
5. Modelo de Poisson
6. Comparação entre os modelos de Bernoulli, Binomial e Poisson

**Divisão de tarefas (opcional):** [PREENCHER quem elaborou cada tópico]

## Contexto biológico escolhido

Os tópicos 5 e 6 usam como contexto a **tartaruga-verde (*Chelonia mydas*) no Brasil**, com dados do artigo de avaliação do estado de conservação da espécie:

- **Poisson:** número de desovas registradas por noite na temporada reprodutiva em Ilha da Trindade (ES), Atol das Rocas (RN) e Fernando de Noronha (PE).
- **Bernoulli e Binomial (na comparação do tópico 6):** presença ou ausência de fibropapilomatose em indivíduos examinados.

Contexto dos tópicos 1 a 4: **[PREENCHER]**

## Como executar o notebook

**No Google Colab (recomendado):**
1. Acesse [colab.research.google.com](https://colab.research.google.com).
2. Vá em *Arquivo > Abrir notebook > GitHub* e cole o link deste repositório (ou faça upload do arquivo `.ipynb`).
3. Execute todas as células em ordem (*Ambiente de execução > Executar tudo*).

**Localmente (Jupyter):**
```bash
pip install numpy pandas matplotlib seaborn scipy jupyter
jupyter notebook tarefa11_variaveis_aleatorias_biologia.ipynb
```

Uma semente aleatória fixa (`42`) é usada nas simulações, então os resultados são reproduzíveis.

## Bibliotecas utilizadas

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy` (módulo `scipy.stats`)

Outras bibliotecas usadas nos tópicos 1 a 4: **[PREENCHER, se houver]**

## Dados utilizados

### Dados reais: desovas e prevalência em *Chelonia mydas*

| Item | Descrição |
|---|---|
| **Fonte** | ALMEIDA, A. P. *et al.* Avaliação do Estado de Conservação da Tartaruga Marinha *Chelonia mydas* (Linnaeus, 1758) no Brasil. *Biodiversidade Brasileira*, ano I, n. 1, p. 12-19, 2011. ICMBio. Dados originais: Banco de Dados TAMAR/SITAMAR. |
| **Link de acesso** | **[PREENCHER]** |
| **Data de acesso** | 29/09/2026 |
| **Variáveis utilizadas** | Número de desovas por local e temporada; proporção de indivíduos com fibropapilomatose e total de indivíduos examinados |
| **Unidade de observação** | Uma temporada reprodutiva por local (desovas); um indivíduo examinado (fibropapilomatose). No notebook, as desovas são convertidas para taxa por **noite**. |
| **Período e local** | Desovas: Ilha da Trindade/ES (2008/2009: 2.961), Atol das Rocas/RN (2007/2008: 474), Fernando de Noronha/PE (2008/2009: 55). Fibropapilomatose: 15,41% de 8.359 indivíduos examinados pelo Projeto TAMAR, 2000 a 2005. |
| **Relação com o modelo** | Desovas por noite: Poisson. Presença/ausência de tumor: Bernoulli. Número de indivíduos com tumor em uma amostra: Binomial. |
| **Limitações** | Os totais de desovas são anuais, não diários. A duração da temporada (182 noites, dezembro a maio) é uma **suposição do grupo**. Os locais têm temporadas diferentes (Atol das Rocas é 2007/2008). A desova não é uniforme ao longo da temporada e uma mesma fêmea pode desovar mais de uma vez, então taxa constante e independência são aproximações. |

### Dados simulados

**Foram utilizados dados simulados** nos tópicos 5 e 6:

- **Contagens diárias de desovas** (tópicos 5.4 e 5.6): geradas a partir de uma distribuição de Poisson com λ calculado dos totais reais, porque o artigo não traz contagens noite a noite. Ilustram o comportamento do modelo e **não são observações reais**.
- **Amostra de 20 tartarugas** (tópico 6): tamanho hipotético, escolhido para ilustrar a Binomial. A proporção de 15,41% é real.
- **Exemplo n = 1000, p = 0,003** (tópico 6.2): valores hipotéticos para demonstrar a aproximação da Binomial pela Poisson.

Dados simulados dos tópicos 1 a 4: **[PREENCHER, se houver]**

## Referências bibliográficas

Apenas obras efetivamente consultadas:

- ALMEIDA, A. P.; SANTOS, A. J. B.; THOMÉ, J. C. A.; BELINI, C.; BAPTISTOTTE, C.; MARCOVALDI, M. Â.; SANTOS, A. S.; LOPEZ, M. Avaliação do Estado de Conservação da Tartaruga Marinha *Chelonia mydas* (Linnaeus, 1758) no Brasil. *Biodiversidade Brasileira*, ano I, n. 1, p. 12-19, 2011.
- **[PREENCHER]** Livro(s) de Probabilidade e Estatística efetivamente consultado(s), com edição e páginas (por exemplo, Ross; Montgomery e Runger; Magalhães e Lima).
- **[PREENCHER]** Demais referências dos tópicos 1 a 4.

## Uso de ferramentas de inteligência artificial

**[PREENCHER]** O enunciado permite o uso de IA como apoio. Descreva brevemente como foi usada (por exemplo, estruturação inicial do código e revisão de texto). O grupo permanece responsável pela correção conceitual, pela autoria e pelo funcionamento do material.

## Materiais externos

- Artigo-fonte: **[PREENCHER link]**
- Outros materiais externos: **[PREENCHER, se houver]**
