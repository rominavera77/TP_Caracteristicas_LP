# PROBLEMA a resolver: Multiplicar todos los números de una lista de números por un valor dado.

# Paradigma Estructurado
# Se basa en instrucciones secuenciales, bucles y control de flujo paso a paso (el "cómo").
# Modifica estados de forma secuencial empleando variables.

# Lista inicial de números
def multiplicar_por_(lista, factor):
    resultado = []
    for num in lista:
        resultado.append(num * factor)
    return(resultado)

print(multiplicar_por_([1, 2, 3, 4, 5], 2))  # Output: [2, 4, 6, 8, 10]

# numeros = [1, 2, 3, 4, 5]
# resultado = []

# # Un bucle estructurado recorre e indica el paso a paso
# for num in numeros:
#     nuevo_valor = num * 2
#     resultado.append(nuevo_valor)

# print(resultado)  # Output: [2, 4, 6, 8, 10]

