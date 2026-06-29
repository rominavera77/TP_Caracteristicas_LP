import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/UNAHUR/Documents/CaracteristicasLP/TP_Caracteristicas_LP/TP3_ciencia_de_datos/tiobe_index_feb_2026.csv")
df

print("--- Primeras filas del DataFrame ---")
print(df.head())

print("--- Valores nulos ---")
print(df.isnull().sum())

print("--- Filas duplicadas ---")
print(df.duplicated().sum())

print("--- Información del DataFrame ---")
print(df.info())

print("--- Estadísticas descriptivas ---")
print(df.describe())

print("--- Frecuencia de Paradigmas ---")
print(df['Paradigm'].value_counts())

print("--- Suma del Rating por Tipo de Tipado ---")
print(df.groupby('Typing')['Rating_Pct'].sum()) 

df['Language'].unique()
df['Creator'].unique()
df['Paradigm'] = df['Paradigm'].str.lower()
df['Typing'] = df['Typing'].str.lower()
df = df.drop_duplicates()
df.duplicated().sum()
df = df.fillna('N/A')
df.isnull().sum()
df['Paradigm'] = df['Paradigm'].replace({'visual':'multiparadigm'})
df['Paradigm'].unique()

# ==========================================
# Gráfico de Tipado: Volumen de Mercado por Tipo (Filtrado sin N/A)
# ==========================================
import os # Importamos os para manejar rutas si fuera necesario

# 1. Creamos una copia del Top 10 para no alterar tu DataFrame original
df_filtrado = df.head(10).copy()

# 2. Convertimos TODO a minúsculas en el DataFrame para homogeneizar
df_filtrado['Typing'] = df_filtrado['Typing'].astype(str).str.strip().str.lower()

# 3. Filtramos eliminando cualquier variante de N/A, NaN o SQL
df_filtrado = df_filtrado[~df_filtrado['Typing'].isin(['n/a', 'nan', 'none'])]

# 4. Agrupamos los datos filtrados para obtener la suma por cada tipo
tipado_resumen = df_filtrado.groupby('Typing')['Rating_Pct'].sum().reset_index()

# 5. Configuramos el lienzo del gráfico
plt.figure(figsize=(9, 6))

# 6. Creamos el gráfico usando LLAVES EN MINÚSCULA para que coincidan al 100% con los datos
sns.barplot(
    data=tipado_resumen,
    x='Typing',
    y='Rating_Pct',
    hue='Typing',
    palette={
        'dynamic': "#3eb8bd",   # Clave fija en minúscula
        'static': "#b41f94"     # Clave fija en minúscula
    },
    legend=False,
    edgecolor='black'
)

# 7. Títulos y etiquetas descriptivas
plt.title("Dominio de Mercado: Lenguajes Estáticos vs. Dinámicos (Top 10)\n(Excluyendo datos no clasificados)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Tipo de Tipado (Typing)", fontsize=12)
plt.ylabel("Suma Total de Popularidad (Rating %)", fontsize=12)

# Forzamos que las etiquetas del eje X se vean profesionales (posiciones 0 y 1)
plt.xticks(ticks=[0, 1], labels=['Dinámico (Dynamic)', 'Estático (Static)'])

# Ajustar el límite superior del eje Y automáticamente para dar espacio al texto
max_val = tipado_resumen['Rating_Pct'].max()
plt.ylim(0, max_val + 10)

# 8. Añadimos las anotaciones de texto correspondientes buscando la clave en minúscula
for index, row in tipado_resumen.iterrows():
    tipo_actual = str(row['Typing'])
    
    if 'static' in tipo_actual:
        texto_nota = f"{row['Rating_Pct']:.2f}%\n(C, C++, Java, C#,\nVisual Basic, Delphi)"
    elif 'dynamic' in tipo_actual:
        texto_nota = f"{row['Rating_Pct']:.2f}%\n(¡Liderado por Python\ncon 21.81%!)"
    else:
        texto_nota = f"{row['Rating_Pct']:.2f}%"
        
    plt.text(
        x=index,
        y=row['Rating_Pct'] + 1,
        s=texto_nota,
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

# Ajuste automático de los márgenes internos
plt.tight_layout()

# ==========================================
# Guardado Automático de la Imagen
# ==========================================
# Guardamos la imagen antes de plt.show() porque show() limpia la memoria de la figura
nombre_archivo = "grafico_tipado_mercado.png"
plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
print(f"¡Éxito! Gráfico guardado en alta resolución como: {nombre_archivo}")

# Desplegamos el gráfico en pantalla
plt.show()

