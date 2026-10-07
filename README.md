# Tarefa 13 — Normal, t de Student, qui-Quadrado e f de Fisher 

Repositório pertencente ao grupo.

Este repositório reúne o notebook da **Tarefa 11** de Bioestatística, que apresenta os conceitos de variável aleatória e os modelos de **Bernoulli**, **Binomial** e **Poisson**, aplicados a dados reais da tartaruga-verde (*Chelonia mydas*) no Brasil.

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/amelyssaeu-ab/bio-dkm/blob/main/Tarefa011_completa.ipynb)

## Integrantes

| Nome | nº USP |
|---|---|
| Drielly Mathias Albertti | 16831084 |
| Kawana Ganeo de Carvalho | 14669691 |
| Melyssa Ponce Lopes | 16831017 |

## Objetivo

Mostrar, com exemplos biológicos e código em Python, o que é uma variável aleatória e como escolher entre os modelos de Bernoulli, Binomial e Poisson conforme o tipo de fenômeno observado.

## Conteúdo do notebook

O arquivo [`Tarefa011_completa.ipynb`](Tarefa011_completa.ipynb) está organizado em seis tópicos:

1. **Variável aleatória:** definição e exemplos.
2. **Variáveis aleatórias discretas e contínuas:** diferenças e exemplos biológicos.
3. **Modelo de Bernoulli:** um único ensaio com dois desfechos. Exemplo: uma tartaruga-verde apresenta ou não fibropapilomatose, com `p = 0,1541`.
4. **Modelo Binomial:** número de sucessos em `n` ensaios independentes. Exemplo: amostra de 20 tartarugas, com discussão sobre a adequação das suposições ao cenário biológico.
5. **Modelo de Poisson:** contagem de eventos por unidade de observação. Exemplo: desovas por noite na Ilha da Trindade, no Atol das Rocas e em Fernando de Noronha, com distribuição teórica, simulação de uma temporada, mudança da unidade de observação e discussão das suposições do modelo.
6. **Comparação entre Bernoulli, Binomial e Poisson:** tabela comparativa, gráficos lado a lado, verificação de médias e variâncias e relações entre os modelos (Binomial como soma de Bernoullis e aproximação da Binomial pela Poisson).

## Dados utilizados

Os dados vêm do artigo de Almeida *et al.* (2011), que por sua vez cita o Banco de Dados TAMAR/SITAMAR como fonte original.

| Local | Temporada | Desovas registradas |
|---|---|---|
| Ilha da Trindade (ES) | 2008/2009 | 2.961 |
| Atol das Rocas (RN) | 2007/2008 | 474 |
| Fernando de Noronha (PE) | 2008/2009 | 55 |

Também foi usada a proporção de **15,41%** de indivíduos com fibropapilomatose entre os **8.359** examinados.

**Suposições do grupo (não são dados do artigo):**

- A temporada reprodutiva tem **182 noites** (de 1º de dezembro a 31 de maio).
- A amostra de **n = 20 tartarugas** é hipotética e serve apenas para ilustrar o modelo Binomial.
- As contagens noite a noite das seções de simulação são **dados simulados**, pois o artigo traz apenas o total por temporada.

## Como executar

**No Google Colab:** clique no botão "Abrir no Colab" no início deste README.

**Localmente:**

```bash
git clone https://github.com/amelyssaeu-ab/bio-dkm.git
cd bio-dkm
pip install numpy pandas matplotlib seaborn scipy jupyter
jupyter notebook Tarefa011_completa.ipynb
```

**Bibliotecas:** `numpy`, `pandas`, `matplotlib`, `seaborn` e `scipy`.

## Referências

ALMEIDA, A. P. *et al.* Avaliação do estado de conservação da tartaruga marinha *Chelonia mydas* (Linnaeus, 1758) no Brasil. **Biodiversidade Brasileira**, Brasília, ano 1, n. 1, p. 12-19, 2011. Acesso em: 29 set. 2026.

MEYER, Paul L. **Probabilidade**: aplicações à estatística. 2. ed. Rio de Janeiro: LTC, 2000.
