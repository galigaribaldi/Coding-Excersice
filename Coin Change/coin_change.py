"""
Coin Change (Dynamic Programming)
EN
You are given an integer array `coins` representing coins of 
different denominations and an integer `amount` representing 
a total amount of money.
Return the fewest number of coins that you need to make up 
that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

ES
Se te da un array de enteros `coins` que representa monedas de 
diferentes denominaciones y un entero `amount` que representa 
una cantidad total de dinero.
Devuelve el menor número de monedas que necesitas para sumar 
esa cantidad. Si esa cantidad de dinero no se puede completar 
con ninguna combinación de monedas, devuelve -1.
Puedes asumir que tienes un número infinito de cada tipo de moneda.

Example:
coin_change([1, 2, 5], 11) # Should return: 3
# Explanation: 11 = 5 + 5 + 1
"""

def coin_change(coins, amount):
    # Este es un problema clásico de Programación Dinámica (DP).
    
    # Creamos un array `dp` de tamaño (amount + 1).
    # dp[i] guardará el número MÍNIMO de monedas para sumar `i`.
    
    # Lo inicializamos con un valor "infinito" (amount + 1 es > que
    # cualquier respuesta posible, ya que lo peor es usar monedas de 1).
    dp = [amount + 1] * (amount + 1)
    
    # Caso base: Se necesitan 0 monedas para sumar 0.
    dp[0] = 0
    
    # Calculamos la solución para cada cantidad `a` desde 1 hasta `amount`.
    for a in range(1, amount + 1):
        # Probamos cada moneda
        for c in coins:
            # Si la moneda es más pequeña que la cantidad...
            if c <= a:
                # La solución es:
                # 1. La que ya teníamos (dp[a])
                # 2. La solución para (a - c) más 1 moneda (la moneda 'c')
                # Elegimos la que sea MÍNIMA.
                dp[a] = min(dp[a], 1 + dp[a - c])
                
    # Si dp[amount] sigue siendo el valor "infinito",
    # significa que nunca encontramos una solución.
    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]

# --- Demo ---
print("\n--- Coin Change ---")
coins1 = [1, 2, 5]
amount1 = 11
print(f"Input: coins={coins1}, amount={amount1}")
print(f"Output: {coin_change(coins1, amount1)}") # Expected: 3

coins2 = [2]
amount2 = 3
print(f"Input: coins={coins2}, amount={amount2}")
print(f"Output: {coin_change(coins2, amount2)}") # Expected: -1