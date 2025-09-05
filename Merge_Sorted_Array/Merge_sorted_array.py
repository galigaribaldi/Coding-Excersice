"""
EN
You are given two sorted arrays nums1 and nums2 of sizes m and n, with nums1 having extra space at the end to fit n elements. Merge nums2 into nums1 sorted in-place.
Input: m n, nums1 (length m+n), nums2 (length n).
Output: merged array as space-separated ints.
Constraints: 0 ≤ m, n ≤ 1e5.

ES
Fusiona nums2 en nums1 (con espacio extra al final) para obtener un arreglo ordenado, en el mismo nums1.

Sample tests

m=3, n=3, nums1=[1,2,3,0,0,0], nums2=[2,5,6] -> [1,2,2,3,5,6]  
m=1, n=0, nums1=[1], nums2=[] -> [1]  
Hint: Two pointers starting from the back.
"""

"""
Descripción del Algoritmo:
    Se dan 2 arreglos con 2 índices, en los que estos te dicen el tamaño de ambos (m y n)
    Estos dos arreglos deben tener la finalidad de que Arreglo 1 contenga arreglo 2
    Para ello primero se procede a restarle a m(primer indice del arreglo 1) - 1, donde localizaremos el elemento aún válido dentro del array1
    Despues haremos lo mismo para n (segundo arreglo) - 1, donde localizareos el elemento aún válido dentro del array2
    con ello, hacemos un bucle para recorrer el primer arreglo
        mientras exista algo dentro de arrelgo 1,
            comparamos si aún hay elementos dentro de ese arreglo 1 y si es mayor que el elmento dentro de arreglo 2
                Para recorrer el arreglo, procederemos a retroceder en una posición con i -=1
            De lo contrario, procedemos a poner el numero en la posición actual (ya que por su valor va allí)
                e igual moveremos el puntero en una posición i -=1

Al final retornamos el array 1
"""

"""
Coloco en array1[k] el mayor entre array1[i] y array2[j].
Si usé array1[i], decremento i; si usé array2[j], decremento j.
En cada iteración decremento k.
Repito hasta que j < 0 (todo array2 quedó insertado).”
"""
import sys
def merge_sorted_array(array1, m,array2, n):
    i = m-1 ## the ultimate validate in nums1
    j = n-1 ##ultimate validate in nums 2
    k = m+n-1 ##ultimate validate in (new)nums 1
    while j >= 0:
        if i >= 0 and array1[i]> array2[j]:
            array1[k] = array1[i]
            i -=1
        else:
            array1[k] = array2[j]
            j -=1
        k-=1
    return array1

if __name__ == "__main__":
    print(merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3))