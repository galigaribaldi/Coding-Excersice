"""
Generate Parentheses (Backtracking / Recursion)
EN
Given `n` pairs of parentheses, write a function to generate all 
combinations of well-formed parentheses.

ES
Dado `n` pares de paréntesis, escribe una función para generar 
todas las combinaciones de paréntesis bien formados.

Example:
generate_parentheses(3)
# Should return: ["((()))","(()())","(())()","()(())","()()()"]
"""

def generate_parentheses(n):
    # Este es un problema clásico de Backtracking (Recursión).
    
    results = []
    
    # `current_string` es la cadena que estamos construyendo.
    # `open_count` es cuántos '(' hemos usado.
    # `close_count` es cuántos ')' hemos usado.
    def backtrack(current_string, open_count, close_count):
        # 1. Caso base: la cadena está completa
        if len(current_string) == 2 * n:
            results.append(current_string)
            return
            
        # 2. Decisión 1: ¿Podemos añadir un '('?
        #    Solo si no hemos usado todos los 'n' disponibles.
        if open_count < n:
            backtrack(current_string + "(", open_count + 1, close_count)
            
        # 3. Decisión 2: ¿Podemos añadir un ')'?
        #    Solo si el número de ')' es MENOR que el de '('.
        #    Esto garantiza que estén bien formados.
        if close_count < open_count:
            backtrack(current_string + ")", open_count, close_count + 1)
    
    # Iniciamos el proceso
    backtrack("", 0, 0)
    return results

# --- Demo ---
print("\n--- Generate Parentheses ---")
n = 3
print(f"Input: n={n}")
print(f"Output: {generate_parentheses(n)}")
# Expected: ["((()))","(()())","(())()","()(())","()()()"]