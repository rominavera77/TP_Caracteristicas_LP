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

# #Distribución de Rating_Pct
# plt.figure(figsize=(10, 6))
# sns.histplot(df['Rating_Pct'], bins=15, kde=True)
# plt.title("Distribución de Rating_Pct")
# plt.xlabel("Rating %")
# plt.ylabel("Frecuencia")
# plt.show()

# # Boxplot de Chang_Pct
# plt.figure(figsize=(10, 6))
# sns.boxplot(x=df['Change_Pct'])
# plt.title("Boxplot de Chang_Pct")
# # plt.xlabel("Cambio %")
# plt.show()

# # Scatter Plot Rating vs Change
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x='Rating_Pct', y='Change_Pct', hue='Paradigm')
# plt.title("Relación entre Rating y Change")
# plt.xlabel("Rating %")
# plt.ylabel("Cambio %")
# plt.show()

# # Scatter Plot Rating vs Change
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x='Paradigm', y='Language', hue='Paradigm')
# plt.title("Relación entre Paradigma y Lenguaje de Programación")
# plt.xlabel("Paradigma")
# plt.ylabel("Lenguaje")
# plt.show()

# #Distribución de Rating_Pct
# plt.figure(figsize=(10, 6))
# sns.histplot(df['Paradigm'], bins=15, kde=True)
# plt.title("Distribución de Paradigmas")
# plt.xlabel("Paradigma")
# plt.ylabel("Lenguaje")
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.barplot(
#     data=df.head(10),
#     x='Language',
#     y='Rating_Pct',
#     hue='Language',   # asignamos hue
#     palette="viridis",
#     legend=False  # evita mostrar leyenda duplicada
#     )
# plt.title("Top 10 Lenguajes por Rating")
# plt.xticks(rotation=45)
# plt.show()

# # Heatmap de correlaciones
# plt.figure(figsize=(8, 6))
# sns.heatmap(df[['Rating_Pct', 'Change_Pct', 'Year_Created']].corr(), annot=True, cmap='coolwarm')  # [[]] para seleccionar columnas
# plt.title("Mapa de Calor de Correlaciones")
# plt.show()

# # Violin plot por paradigma ajustado a nuevas versiones de Seaborn
# plt.figure(figsize=(12, 6))
# sns.violinplot(
#     data=df,
#     x="Paradigm",
#     y="Rating_Pct",
#     hue="Paradigm",
#     palette='muted',
#     split=True,
#     legend=False
#     )
# plt.title("Ditribución de Change_Pct por Paradigma")
# plt.xticks(rotation=45)
# plt.show()

# ==========================================
# Gráfico de Torta: Predominancia Técnica (Top 10 Paradigmas)
# ==========================================

# 1. Agrupamos el Rating por cada Paradigma para ver la dominancia real en el mercado
predominancia_tecnica = df.head(10).groupby('Paradigm')['Rating_Pct'].sum().sort_values(ascending=False)

# 2. Configuramos el tamaño del gráfico
plt.figure(figsize=(8, 8))

# 3. Definimos una paleta de colores atractiva (puedes cambiar "pastel", "viridis" o "Blues_r")
colores = sns.color_palette("pastel", len(predominancia_tecnica))

# 4. Creamos el gráfico de torta
plt.pie(
    predominancia_tecnica, 
    labels=predominancia_tecnica.index, 
    autopct='%1.1f%%',          # Muestra el porcentaje con un decimal
    startangle=140,              # Gira el gráfico para una mejor lectura
    colors=colores, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}, # Bordes blancos elegantes entre porciones
    textprops={'fontsize': 12, 'weight': 'bold'}       # Texto legible y en negrita
)

# 5. Título del gráfico
plt.title("Predominancia Técnica en el Top 10\n(Distribución del Mercado por Paradigma)", fontsize=14, fontweight='bold', pad=20)

# 6. Desplegamos el gráfico
plt.show()

# ==========================================
# Gráfico de Tipado: Volumen de Mercado por Tipo
# ==========================================

# 1. Aseguramos que la columna no tenga nulos reales (NaN) antes de agrupar
df['Typing'] = df['Typing'].fillna('N/A')

# 2. Agrupamos los datos para obtener el volumen de mercado sumado por cada tipo
tipado_resumen = df.head(10).groupby('Typing')['Rating_Pct'].sum().reset_index()

# 3. Configuramos el lienzo del gráfico
plt.figure(figsize=(10, 6))

# 4. Creamos el gráfico asociando las llaves EXACTAS en minúscula que pide tu consola
sns.barplot(
    data=tipado_resumen,
    x='Typing',
    y='Rating_Pct',
    hue='Typing',
    palette={
        'dynamic': '#ff7f0e', 
        'static': '#1f77b4', 
        'N/A': '#aec7e8',
        'declarative/static': '#aec7e8' # Por si acaso se guardó así
    },
    legend=False,
    edgecolor='black'
)

# 5. Títulos y etiquetas descriptivas
plt.title("Dominio de Mercado por Tipo de Tipado (Top 10)\n¿Estático o Dinámico?", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Tipo de Tipado (Typing)", fontsize=12)
plt.ylabel("Suma Total de Popularidad (Rating %)", fontsize=12)

# Ajustar dinámicamente el límite del eje Y según el valor máximo para evitar recortes
max_val = tipado_resumen['Rating_Pct'].max()
plt.ylim(0, max_val + 10)

# 6. Añadimos las anotaciones dinámicas buscando los índices en minúscula
for index, row in tipado_resumen.iterrows():
    tipo_actual = str(row['Typing']).lower()
    
    if 'static' in tipo_actual:
        texto_nota = f"{row['Rating_Pct']:.2f}%\n(C, C++, Java, C#,\nVisual Basic, Delphi)"
    elif 'dynamic' in tipo_actual:
        texto_nota = f"{row['Rating_Pct']:.2f}%\n(¡Liderado por Python\ncon 21.81%!)"
    else:
        texto_nota = f"{row['Rating_Pct']:.2f}%\n(SQL)"
        
    plt.text(
        x=index,
        y=row['Rating_Pct'] + 1,
        s=texto_nota,
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold'
    )

# Desplegamos el gráfico en Colab / Terminal
plt.tight_layout()
plt.show()


# # 2. Limpieza de datos (Manejo de NaN)
# # Reemplazamos el NaN en SQL poniendo 'Declarative' o 'None' para que no interfiera
# df["Typing"] = df["Typing"].fillna("Static/Declarative")

# # Configuración estética general para los gráficos
# plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
# fig, axes = plt.subplots(3, 1, figsize=(10, 16))

# # --- GRÁFICO 1: Rating de Popularidad Actual (Gráfico de Barras Horizontal) ---
# df_sorted = df.sort_values(by="Rating_Pct", ascending=True)
# bars = axes[0].barh(
#     df_sorted["Language"],
#     df_sorted["Rating_Pct"],
#     color="#2b5c8f",
#     edgecolor="black",
# )
# axes[0].set_title(
#     "1. Cuota de Mercado Actual por Lenguaje (Rating %)",
#     fontsize=14,
#     fontweight="bold",
#     pad=10,
# )
# axes[0].set_xlabel("Rating (%)", fontsize=11)
# axes[0].set_xlim(0, 25)

# # Añadir etiquetas de datos en las barras
# for bar in bars:
#     width = bar.get_width()
#     axes[0].text(
#         width + 0.3,
#         bar.get_y() + bar.get_height() / 2,
#         f"{width}%",
#         va="center",
#         ha="left",
#         fontsize=10,
#         fontweight="bold",
#     )
