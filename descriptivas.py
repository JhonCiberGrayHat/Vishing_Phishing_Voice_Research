# ============================================
# Análisis descriptivo de delitos informáticos
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el dataset
# Cambia la ruta al nombre exacto del archivo que subiste
df = pd.read_csv("Conteo_de_Víctimas_V2_20251211_delitos_informaticos.csv")

# 2. Exploración inicial
print("Dimensiones del dataset:", df.shape)
print("\nPrimeras filas:")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nEstadísticas descriptivas:")
print(df.describe(include="all"))

# 3. Valores nulos
print("\nConteo de valores nulos por columna:")
print(df.isnull().sum())

# 4. Distribución de variables categóricas
for col in df.select_dtypes(include="object").columns:
    print(f"\nDistribución de {col}:")
    print(df[col].value_counts())

# 5. Visualizaciones básicas
plt.figure(figsize=(10,6))
sns.countplot(data=df, x=df.columns[0])  # Cambia por la columna que represente el tipo de delito
plt.xticks(rotation=45)
plt.title("Distribución de delitos informáticos")
plt.show()

# Ejemplo: relación entre dos variables numéricas
if len(df.select_dtypes(include="number").columns) >= 2:
    num_cols = df.select_dtypes(include="number").columns
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=df, x=num_cols[0], y=num_cols[1], hue=df.columns[0])
    plt.title(f"Relación entre {num_cols[0]} y {num_cols[1]}")
    plt.show()

# 6. Correlaciones
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Mapa de correlaciones")
plt.show()