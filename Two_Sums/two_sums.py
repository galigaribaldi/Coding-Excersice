import sys

"""
Description: 
EN
Given an array nums and integer target, return indices i, j (i < j) such that nums[i] + nums[j] == target. If multiple, return any.
Input: n, nums, target.
Output: i j (0-based) or -1 -1 if none.
Constraints: 1 ≤ n ≤ 1e5.

ES
Dado un arreglo nums y un entero target, devuelve índices i, j (i < j) con nums[i] + nums[j] == target. Si hay varios, cualquiera.

Sample tests
n=4, nums=[2,7,11,15], target=9 -> 0 1  
n=3, nums=[3,2,4], target=6 -> 1 2  
n=3, nums=[1,2,3], target=7 -> -1 -1  

"""

"""
Algoritmo escrito en simples palabras:
“Recorro nums con índice i y valor x. Calculo need = target - x.
Si need ya está en el diccionario, devuelvo (dic[need], i).
Si no, guardo dic[x] = i.
Si termino el recorrido sin encontrar pareja, devuelvo (-1, -1).”
"""

def two_sums(num, target):
    dictionary_1 = {}
    for i, x in enumerate(num):
        need = target - x
        if need in dictionary_1:
            return dictionary_1[need], i
        dictionary_1[x] = i
    return -1, 1
if __name__ == "__main__":
    two_sums([2, 7, 11, 15],9)
    #two_sums([3, 2, 4, 6],6)
    #two_sums([1, 2, 3],7)