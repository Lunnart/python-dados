# %pip install pandas
# %pip install "psycopg[binary]"
# %pip install -q missingno
# %pip install -q category_encoders
# %pip install -q plotly

import pandasql
import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt
import psycopg
from pandasql import sqldf
from sqlalchemy import create_engine
from matplotlib.backends.backend_pdf import PdfPages

# ======================================================
# Conexão com o PostgreSQL
# ======================================================

engine = create_engine(
    "postgresql+psycopg://postgres:12345678@localhost/corporativo"
)

print("Conexão realizada com sucesso!")

# ======================================================
# Consulta SQL
# ======================================================

sql = """
SELECT
    numero_nf,
    data_venda,
    valor_venda,
    cliente,
    tipo_pessoa,
    valor_parcela,
    forma_pagamento,
    numero_parcela,
    situacao
FROM financeiro.contas_receber_vendas;
"""

df = pd.read_sql(sql, engine)

print(df)

# ======================================================
# Informações do DataFrame
# ======================================================

print(f"\nTotal de registros: {len(df)}")

print(df.columns)
print(df.shape)

df.info()

# ======================================================
# Converter data
# ======================================================

df["data_venda"] = pd.to_datetime(df["data_venda"])

df["data_venda"] = df["data_venda"].dt.strftime("%d/%m/%Y")

print(df.head())

# ======================================================
# Remover valores nulos
# ======================================================

df_limpo = df.dropna()

# ======================================================
# Informações das colunas
# ======================================================

print("Quantidade de clientes:", len(df["cliente"].unique()))

print(
    "Quantidade de formas de pagamento:",
    len(df["forma_pagamento"].unique())
)

print(df["forma_pagamento"].unique())

print(df["forma_pagamento"].value_counts())

print(
    "Quantidade de notas fiscais distintas:",
    len(df["numero_nf"].value_counts().unique())
)

# ======================================================
# DataFrame apenas com colunas numéricas
# ======================================================

df_numerical = df.select_dtypes(include="number")

print(df_numerical.head())

df_numerical.info()

# ======================================================
# Comissão
# ======================================================

df["percentual_comissao"] = 2.5

df["valor_comissao"] = (
    df["valor_venda"] * df["percentual_comissao"] / 100
)

print(df.head())

df.info()

print(df.columns)

# ======================================================
# Top 5 clientes por valor vendido
# ======================================================

top_clientes = (
    df.groupby("cliente")["valor_venda"]
      .sum()
      .sort_values(ascending=False)
      .head(5)
)

fig, ax = plt.subplots(figsize=(12, 6))

top_clientes.plot(
    kind="bar",
    color="#003DA5",
    ax=ax
)

ax.set_title(
    "Top 5 Clientes por Valor Vendido",
    fontsize=14,
    fontweight="bold"
)

ax.set_xlabel("")
ax.set_ylabel("Valor da Venda (R$)")

plt.xticks(rotation=20, ha="right")

for i, valor in enumerate(top_clientes):
    ax.text(
        i,
        valor,
        f"R$ {valor:,.2f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()
plt.show()