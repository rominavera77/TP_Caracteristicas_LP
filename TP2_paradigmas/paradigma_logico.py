# PROBLEMA a resolver: Multiplicar todos los números de una lista de números por 2.

# Paradigma Lógico
# Se declaran hechos y reglas matemáticas (lógica formal), y el motor de inferencia deduce la solución 
# basándose en relaciones.
# No se define un algoritmo de pasos.

# % Regla base: una lista vacía multiplicada por 2 da una lista vacía.
# multiplicar_lista([], []).

# % Regla recursiva: multiplica la cabeza (H) por 2 y procesa el resto (T).
# multiplicar_lista([H|T], [H2|T2]) :-
#     H2 is H * 2,
#     multiplicar_lista(T, T2).

# % Consulta para ejecutar en la consola de Prolog:
# % ?- multiplicar_lista([1, 2, 3, 4, 5], Resultado).
# % Resultado = [2, 4, 6, 8, 10].
 