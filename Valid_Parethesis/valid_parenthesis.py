"""
2) Valid Parentheses
EN
Given a string containing only ()[]{}, determine if it is valid (properly nested).
Input: string s.
Output: true or false.
Constraints: 1 ≤ |s| ≤ 1e4.

ES
Dada una cadena con solo ()[]{}, determina si es válida (bien anidada).

Sample tests

rust
Copiar
Editar
"()" -> true  
"()[]{}" -> true  
"(]" -> false  
"([)]" -> false  
"{[]}" -> true  
Hint: Stack to match opening and closing brackets.


"""

"""
Solve:
Uso de una pila (STACK):
    Porque el último que abres es el primero que tienes que cerrar (Last In, First Out — LIFO).    
    Es como una pila de platos: el último que pusiste encima es el primero que sacas.
Algoritmo:
 Cómo se valida realmente
    Recorres la cadena de izquierda a derecha (índice por índice).
    Cada vez que ves una apertura ((, [, {):
        La guardas en la pila.
        Esto implica que "esperas" que algún día venga su cierre correspondiente.
    Cada vez que ves un cierre (), ], }):
        Verificas que la última apertura que guardaste en la pila coincida con este cierre.
        Si no coincide, es inválido (porque se rompió el orden o el tipo).
        Si coincide, sacas esa apertura de la pila (pop).
    Posición implícita:
        No necesitamos comparar índices manualmente.
        La pila ya garantiza que la última apertura en entrar es la primera en salir (LIFO).
        Esto respeta automáticamente la posición y el anidamiento correcto.
"""
import sys
def validator(sample_string):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for i in sample_string:
        if i in pairs.values():
            stack.append(i)
        elif i in pairs:
            ###"Si la pila está vacía o el último paréntesis abierto no coincide con el tipo de cierre que tengo, la cadena no es válida."
            if not stack or stack[-1] != pairs[i]:
                return False
            stack.pop()
        else:
            return False
    return not stack

if __name__ == "__main__":
    #print(validator("()"))        # True
    #print(validator("()[]{}"))    # True
    print(validator("(]"))        # False
    print(validator("([)]"))      # False
    print(validator("{[]}"))  