"""
Process User Purchases (Data Aggregation)
EN
Given a list of purchase dictionaries, each containing a "user_id" and an "amount", 
write a function that returns a list of tuples (user_id, total_amount), 
sorted in descending order by total_amount. Only include users with a total_amount > 0.

ES
Dada una lista de diccionarios de compras, cada uno con "user_id" y "amount", 
escribe una función que devuelva una lista de tuplas (user_id, total_amount), 
ordenada de forma descendente por el total_amount. Incluye solo a usuarios con un total_amount > 0.

Example:
purchases = [
    {"user_id": "u1", "amount": 10},
    {"user_id": "u2", "amount": 5},
    {"user_id": "u1", "amount": 20},
    {"user_id": "u3", "amount": 15},
    {"user_id": "u2", "amount": 5},
]
process_purchases(purchases) 
# Should return: [("u1", 30), ("u3", 15), ("u2", 10)]
"""

from collections import defaultdict

def process_purchases(purchases):
    # Usar defaultdict es muy eficiente y demuestra conocimiento de 'collections'.
    # defaultdict(int) inicializa cualquier clave nueva con 0.
    user_totals = defaultdict(int)
    
    for purchase in purchases:
        user_id = purchase.get("user_id")
        amount = purchase.get("amount", 0)
        
        if user_id and amount > 0:
            user_totals[user_id] += amount
            
    # .items() convierte el dict en una lista de tuplas [(key, value), ...]
    # 'sorted' es clave. Usamos 'key=lambda' para decirle que ordene por el segundo
    # elemento de la tupla (el total) y 'reverse=True' para que sea descendente.
    sorted_totals = sorted(
        user_totals.items(), 
        key=lambda item: item[1], 
        reverse=True
    )
    
    return sorted_totals

# --- Demo ---
purchases_list = [
    {"user_id": "u1", "amount": 10},
    {"user_id": "u2", "amount": 5},
    {"user_id": "u1", "amount": 20},
    {"user_id": "u3", "amount": 15},
    {"user_id": "u2", "amount": 5},
    {"user_id": "u4", "amount": -10}, # Should be ignored
    {"user_id": "u5", "amount": 0},   # Should be ignored
    {},                              # Should be ignored
]

print("--- Process User Purchases ---")
print(f"Input: {purchases_list}")
print(f"Output: {process_purchases(purchases_list)}")
# Expected: [('u1', 30), ('u3', 15), ('u2', 10)]