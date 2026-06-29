# PROBLEMA a resolver: Multiplicar todos los números de una lista de números por un valor dado.

# Paradigma Orientado a Objetos (POO)
# El problema se modela encapsulando los datos (la lista) 
# y el comportamiento (la acción de multiplicar) dentro de un objeto que expone un método

class ProcesadorNumeros:
    def __init__(self, lista_numeros):
        self.numeros = lista_numeros  # Estado interno encapsulado

    def multiplicar_por_(self, factor):
        # Método que opera sobre el estado del objeto
        return [num * factor for num in self.numeros]

# Instanciación del objeto e invocación de su método
procesador = ProcesadorNumeros([1, 2, 3, 4, 5])
resultado = procesador.multiplicar_por_(2)

print(resultado)  # Output: [2, 4, 6, 8, 10]