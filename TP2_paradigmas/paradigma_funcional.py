# PROBLEMA a resolver: Multiplicar todos los números de una lista de números por un valor dado.

# Paradigma Funcional
# Se centra en el "qué" y utiliza funciones puras de orden superior (como map).
# Evita la mutabilidad de los datos y los bucles manuales.

numeros = [1, 2, 3, 4, 5]

# Se aplica una función anónima (lambda) a cada elemento de forma directa
resultado = list(map(lambda x: x * 2, numeros))

print(resultado)  # Output: [2, 4, 6, 8, 10]