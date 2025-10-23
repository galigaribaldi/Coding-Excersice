"""
Group Anagrams (Hashmaps)
EN
Given an array of strings `strs`, group the anagrams together. 
You can return the answer in any order. An Anagram is a word formed 
by rearranging the letters of a different word, typically using all 
the original letters exactly once.

ES
Dado un array de strings `strs`, agrupa los anagramas. 
Puedes devolver la respuesta en cualquier orden. Un Anagrama es una 
palabra formada al reordenar las letras de otra, usando todas las 
letras originales exactamente una vez.

Example:
group_anagrams(["eat","tea","tan","ate","nat","bat"])
# Should return: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""
from collections import defaultdict

def group_anagrams(strs):
    # La clave del problema es encontrar una "llave" única para cada grupo de anagramas.
    # La llave más fácil es la palabra ordenada alfabéticamente.
    # "eat", "tea", "ate" -> "aet"
    # "tan", "nat" -> "ant"
    # "bat" -> "abt"
    
    # Usamos defaultdict(list) para que el valor por defecto de cada llave sea una lista vacía.
    anagram_map = defaultdict(list)
    
    for s in strs:
        # sorted(s) devuelve una lista de caracteres ['a', 'e', 't']
        # "".join(...) los une para formar la llave "aet"
        sorted_key = "".join(sorted(s))
        
        # Agregamos la palabra original 's' a la lista de esa llave
        anagram_map[sorted_key].append(s)
        
    # Finalmente, solo devolvemos los valores (las listas de anagramas) del diccionario.
    return list(anagram_map.values())

# --- Demo ---
strs = ["eat","tea","tan","ate","nat","bat"]
print("\n--- Group Anagrams ---")
print(f"Input: {strs}")
print(f"Output: {group_anagrams(strs)}")
# Expected: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']] (el orden de los grupos no importa)