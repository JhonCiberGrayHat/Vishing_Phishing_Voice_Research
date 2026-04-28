import pandas as pd
import numpy as np
import seaborn as sns

# URL RAW del archivo CSV en GitHub
#url = "https://raw.githubusercontent.com/usuario/repositorio/main/datos/archivo.csv"

# Cargar el archivo en un DataFrame
df = pd.read_csv("Conteo_de_Víctimas_V2_20251211_delitos_informaticos.csv")

# Verificar carga
print(df.head())  # conozco los encabezados de la data
print(df.info())  # conozco los generales de la data

print(df.describe()) # medidas descriptivas univariadas 

