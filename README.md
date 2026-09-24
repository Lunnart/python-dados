# 📊 Análise de Vendas e Performance Comercial

> Projeto de análise de dados desenvolvido com **Python, SQL e PostgreSQL**, com foco em transformar dados comerciais em informações para apoiar a análise de vendas e desempenho.

---

## 📌 Sobre o projeto

Este projeto apresenta um fluxo completo de **análise exploratória de dados (EDA)** aplicado a uma base de vendas.

A partir de dados armazenados em um banco **PostgreSQL**, o projeto realiza a extração, tratamento e exploração das informações utilizando Python, além da criação de indicadores e visualizações para facilitar a interpretação dos dados.

O objetivo é demonstrar, de forma prática, conhecimentos fundamentais para atuação como **Analista de Dados Júnior**, conectando banco de dados, programação, tratamento de dados e visualização.

---

## 🎯 Objetivos

* Conectar Python a um banco de dados PostgreSQL;
* Realizar consultas utilizando SQL;
* Carregar dados para análise com Pandas;
* Explorar a estrutura e características da base;
* Realizar tratamento dos dados;
* Identificar informações relevantes sobre clientes e vendas;
* Calcular valores de comissão;
* Identificar os principais clientes por valor vendido;
* Criar visualizações para facilitar a interpretação dos resultados.

---

## 🛠️ Tecnologias e ferramentas

| Tecnologia         | Aplicação                           |
| ------------------ | ----------------------------------- |
| 🐍 **Python**      | Desenvolvimento da análise          |
| 🐼 **Pandas**      | Manipulação e análise dos dados     |
| 🗄️ **PostgreSQL** | Armazenamento dos dados             |
| 🔎 **SQL**         | Extração e consulta das informações |
| 🔌 **SQLAlchemy**  | Conexão entre Python e PostgreSQL   |
| 🐘 **Psycopg**     | Comunicação com PostgreSQL          |
| 📊 **Matplotlib**  | Visualização dos dados              |
| 🔢 **PandasQL**    | Consultas SQL sobre DataFrames      |

---

## 🔄 Pipeline de análise

O projeto segue um fluxo de tratamento e análise de dados:

```text
PostgreSQL
    │
    ▼
Consulta SQL
    │
    ▼
Extração dos dados
    │
    ▼
Pandas DataFrame
    │
    ▼
Tratamento e preparação
    │
    ▼
Análise exploratória
    │
    ├── Clientes
    ├── Formas de pagamento
    ├── Notas fiscais
    └── Valores numéricos
    │
    ▼
Criação de indicadores
    │
    ├── Comissão
    └── Top 5 clientes
    │
    ▼
Visualização dos resultados
```

---

## 🗄️ Fonte dos dados

Os dados utilizados são provenientes da tabela:

```text
financeiro.contas_receber_vendas
```

Entre os campos utilizados na análise estão:

* `numero_nf`
* `data_venda`
* `valor_venda`
* `cliente`
* `tipo_pessoa`
* `valor_parcela`
* `forma_pagamento`
* `numero_parcela`
* `situacao`

A consulta SQL é utilizada para selecionar as informações necessárias antes da etapa de análise em Python.

---

## 🔎 Processo de análise

### 1. Conexão com o banco

A aplicação estabelece uma conexão com o PostgreSQL utilizando **SQLAlchemy** e **Psycopg**.

Após a conexão, os dados são extraídos diretamente do banco para um DataFrame do Pandas.

---

### 2. Exploração inicial

Após a importação dos dados, são verificadas informações como:

* quantidade de registros;
* nomes das colunas;
* dimensões do DataFrame;
* tipos dos dados;
* informações gerais da estrutura da base.

Essa etapa permite compreender a composição dos dados antes da análise.

---

### 3. Tratamento dos dados

A coluna `data_venda` é convertida para o formato de data e posteriormente formatada para apresentação.

Também é realizada a remoção de registros que possuem valores nulos.

Além disso, são identificadas as colunas numéricas para apoiar análises quantitativas.

---

## 📈 Indicadores e análises

### 💰 Comissão sobre vendas

O projeto utiliza uma taxa de comissão de **2,5%** sobre o valor das vendas.

O cálculo é realizado diretamente no DataFrame:

```python
df["percentual_comissao"] = 2.5

df["valor_comissao"] = (
    df["valor_venda"] * df["percentual_comissao"] / 100
)
```

Isso permite acrescentar à base uma nova métrica relacionada à comissão das vendas.

---

### 🏆 Top 5 clientes por valor vendido

Uma das análises realizadas é a identificação dos **cinco clientes com maior valor total de vendas**.

Para isso, os valores são agrupados por cliente, somados e ordenados de forma decrescente:

```python
top_clientes = (
    df.groupby("cliente")["valor_venda"]
      .sum()
      .sort_values(ascending=False)
      .head(5)
)
```

O resultado é apresentado visualmente por meio de um gráfico de barras.

Os valores também são exibidos diretamente no gráfico, tornando a leitura dos resultados mais objetiva.

---

## 📊 Visualização

A visualização dos dados é realizada utilizando **Matplotlib**, permitindo transformar os resultados da análise em informações mais fáceis de interpretar.

Um dos gráficos desenvolvidos apresenta o ranking dos cinco clientes com maior valor vendido.

```text
        Valor vendido
             ▲
             │
        █    │
        █    │
        █    │       █
        █    │       █
        █    │       █       █
        █    │       █       █
        █    │       █       █       █
        └──────────────────────────────►
          Cliente 1  Cliente 2  Cliente 3...
```

---

## 💡 Principais competências demonstradas

Este projeto demonstra conhecimentos práticos em:

### 🐍 Python

* Pandas
* Manipulação de DataFrames
* Criação de novas métricas
* Tratamento de dados
* Visualização

### 🗄️ Banco de dados

* PostgreSQL
* SQL
* Consultas em tabelas relacionais
* Conexão entre banco e Python

### 📊 Análise de dados

* Análise exploratória
* Agrupamento e agregação
* Identificação de padrões
* Criação de indicadores
* Ranking de clientes

### 📈 Visualização

* Construção de gráficos
* Apresentação de valores
* Comunicação visual dos resultados

---

## 📁 Estrutura do projeto

```text
📦 analise-vendas
│
├── 📄 index.py
├── 📓 index.ipynb
└── 📄 README.md
```

---

## 🚀 Possíveis melhorias

Como evolução do projeto, podem ser incorporadas novas análises e funcionalidades, como:

* 📅 análise da evolução das vendas ao longo do tempo;
* 👤 análise de desempenho por vendedor;
* 💳 análise das formas de pagamento;
* 🏆 ranking de clientes;
* 💰 análise de comissão por período;
* 📊 criação de um dashboard interativo;
* 📄 geração automatizada de relatórios.

---

## 🎓 Objetivo profissional

Este projeto faz parte da construção de um portfólio voltado para **Análise de Dados**, colocando em prática conhecimentos de programação, SQL, banco de dados, tratamento de dados e visualização.

A proposta é demonstrar não apenas a utilização das ferramentas, mas também a capacidade de construir um fluxo de análise que parte dos dados brutos e chega a informações que podem apoiar a compreensão do negócio.

> **Dados não são apenas números. Quando bem analisados, eles ajudam a contar a história do negócio. 📊**

---

## 👩‍💻 Sobre

Projeto desenvolvido como parte da jornada prática de aprendizado em **Análise de Dados**.

**Tecnologias principais:** Python • Pandas • SQL • PostgreSQL • SQLAlchemy • Matplotlib

---

⭐ **Se você achou o projeto interessante, fique à vontade para explorar o código e acompanhar sua evolução.**
