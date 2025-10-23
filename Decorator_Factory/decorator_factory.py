"""
HackerRank
"""


import functools
import sys

# -----------------------------------------------------------
# 1. EL DECORADOR (VERSIÓN FINAL)
# -----------------------------------------------------------
def cache(limits=None):
    limit_rules = limits if limits is not None else {}

    def decorator(func):
        _cache = {}

        @functools.wraps(func)
        def wrapper(*args):
            for index, max_value in limit_rules.items():
                if index < len(args) and args[index] > max_value:
                    arg_value = args[index]
                    func_name = func.__name__
                    all_args_str = ', '.join(map(str, args))
                    error_message = f"{func_name} ({all_args_str}): argument {index} value {arg_value} is too high to calculate"
                    raise ValueError(error_message)

            if args in _cache:
                return _cache[args]
            else:
                result = func(*args)
                _cache[args] = result
                return result
        
        return wrapper

    return decorator

# -----------------------------------------------------------
# 2. DEFINICIÓN DE LAS FUNCIONES CON SUS DECORADORES
# -----------------------------------------------------------

@cache(limits={0: 20})
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n <= 1 else n * factorial(n - 1)

@cache(limits={0: 200})
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# El nombre de la función debe ser el que espera el output.
# Si el output dice 'exponent', la función debe llamarse 'exponent'.
@cache(limits={0: 1000, 1: 100})
def exponent(base: int, exponent: int) -> int:
    return base ** exponent

# -----------------------------------------------------------
# 3. LÓGICA PRINCIPAL PARA PROCESAR EL INPUT DE HACKERRANK
# -----------------------------------------------------------
def main():
    # Asegúrate que los nombres en el mapa coincidan con el input y las funciones
    function_map = {
        'factorial': factorial,
        'fibonacci': fibonacci,
        'exponent': exponent, 
    }

    try:
        num_lines_str = sys.stdin.readline()
        if not num_lines_str: return
        num_lines = int(num_lines_str)

        for _ in range(num_lines):
            line = sys.stdin.readline().strip().split()
            if not line: continue
            
            func_name_str = line[0]
            args_str = "".join(line[1:]).split(',')
            args_int = [int(arg) for arg in args_str]

            func_to_call = None
            for key, func in function_map.items():
                # Cambiado a '==' para evitar ambigüedades si hubiera funciones
                # con nombres parecidos (ej: 'exp' vs 'exponent')
                if func_name_str == key:
                    func_to_call = func
                    break
            
            if func_to_call:
                try:
                    result = func_to_call(*args_int)
                    print(result)
                except ValueError as e:
                    print(e)

    except (ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()