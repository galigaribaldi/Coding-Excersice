"""
4) Best Time to Buy and Sell Stock
EN
Given prices of a stock, find the max profit from one buy and one sell.
Input: n, prices array.
Output: max profit (integer).
Constraints: 1 ≤ n ≤ 1e5.

ES
Dadas las cotizaciones de una acción, encuentra la ganancia máxima con una sola compra y venta.

Sample tests

csharp
Copiar
Editar
[7,1,5,3,6,4] -> 5  
[7,6,4,3,1] -> 0  
"""
"""
Recorro los precios llevando el mínimo visto hasta el momento (posible día de compra).
En cada día calculo la ganancia si vendo hoy: precio_actual − mínimo.
Si es mayor a la mejor ganancia, la actualizo.
Si aparece un precio aún más bajo, actualizo el mínimo.
Al final, la mejor ganancia (o 0 si siempre bajó).
"""

import sys
def solve(array1):
    min_value = array1[0]
    ganancia = 0
    if len(array1) < 2:
        return 0
    for i in array1:
        if i < min_value:
            min_value = i
        diferencia = i - min_value
        if diferencia > ganancia:
            ganancia = diferencia
    return ganancia

if __name__ == "__main__":
    print(solve([7,1,5,3,6,4]))  # 5
    print(solve([7,6,4,3,1]))    # 0
    print(solve([2,4,1,7]))      # 6