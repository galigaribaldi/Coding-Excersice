"""
Longest Substring Without Repeating Characters (Sliding Window)
EN
Given a string `s`, find the length of the longest substring 
without repeating characters.

ES
Dada una cadena `s`, encuentra la longitud de la subcadena (substring) 
más larga que no contenga caracteres repetidos.

Example:
length_of_longest_substring("abcabcbb")
# Should return: 3 (because of "abc")
"""

def length_of_longest_substring(s):
    # Este es el patrón clásico de "sliding window" (ventana deslizante).
    # Usamos un 'set' para saber qué caracteres están en la ventana actual.
    char_set = set()
    
    # 'left' es el inicio de la ventana, 'right' es el final.
    left = 0
    max_length = 0
    
    # 'right' itera por toda la cadena, expandiendo la ventana.
    for right in range(len(s)):
        # Si el caracter ya está en la ventana, debemos achicarla
        # desde la izquierda ('left') hasta que ese caracter ya no esté.
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        # Ahora que es seguro, agregamos el nuevo caracter a la ventana.
        char_set.add(s[right])
        
        # La longitud actual de la ventana es (right - left + 1).
        # Comparamos si es la más larga que hemos visto.
        max_length = max(max_length, right - left + 1)
        
    return max_length

# --- Demo ---
print("\n--- Longest Substring Without Repeating Characters ---")

s1 = "abcabcbb"
print(f"Input: '{s1}'")
print(f"Output: {length_of_longest_substring(s1)}") # Expected: 3

s2 = "bbbbb"
print(f"Input: '{s2}'")
print(f"Output: {length_of_longest_substring(s2)}") # Expected: 1

s3 = "pwwkew"
print(f"Input: '{s3}'")
print(f"Output: {length_of_longest_substring(s3)}") # Expected: 3 (por "wke")