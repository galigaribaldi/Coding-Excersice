"""
Climbing Stairs
EN
You can climb n stairs taking 1 or 2 steps. How many distinct ways can you climb to the top?
ES
Puedes subir n escalones tomando 1 o 2 pasos. ¿Cuántas formas distintas hay para llegar a la cima?
Hint: Fibonacci sequence.
Example:
n=3 → 3
"""
def climbing_stairs(number):
    if number <= 1:
        return 1
    return climbing_stairs(number-1) + climbing_stairs(number -2)
print(climbing_stairs(6))