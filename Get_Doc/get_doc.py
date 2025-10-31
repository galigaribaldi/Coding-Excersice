"""
Altimetrik HackerRank
"""
import inspect
from collections.abc import Callable # Para type hinting

def get_doc(callable_obj: Callable) -> str:
    """
    Generates a documentation string for any given callable object.
    """
    
    # 1. Obtener el objeto "signature" (firma)
    try:
        # Si es una clase, inspect.signature() inteligentemente
        # usará __init__
        sig = inspect.signature(callable_obj)
    except (ValueError, TypeError):
        return f"Could not get signature for {callable_obj}"
        
    # 2. Obtener el nombre y el docstring (limpio de indentación)
    # inspect.getdoc es inteligente: si es una clase,
    # puede combinar el docstring de la clase y el de __init__
    func_name = callable_obj.__name__
    full_docstring = inspect.getdoc(callable_obj) or ""

    # --- Separar Descripción y Ejemplo ---
    description_text = ""
    example_text = ""
    # Palabras clave para buscar el inicio de los ejemplos
    example_keywords = ["Example:", "Examples:", "Ejemplo:", "Ejemplos:"]
    
    found_example = False
    for keyword in example_keywords:
        if keyword in full_docstring:
            # Dividimos el docstring en descripción y ejemplo
            parts = full_docstring.split(keyword, 1)
            description_text = parts[0].strip()
            example_text = parts[1].strip() # Tomamos todo después de la palabra clave
            found_example = True
            break
            
    if not found_example:
        # Si no hay "Example:", todo el docstring es la descripción
        description_text = full_docstring.strip()
    
    # --- Construir la cadena de salida ---
    output_lines = []
    output_lines.append(f"Function: {func_name}")
    output_lines.append("") # Línea en blanco

    # 3. Añadir Descripción
    output_lines.append("Description:")
    if description_text:
        # Añadimos indentación al docstring
        for line in description_text.split('\n'):
            output_lines.append(f"  {line}")
    else:
        output_lines.append("  None")
    
    output_lines.append("") # Línea en blanco

    # 4. Añadir Parámetros
    output_lines.append("Parameters:")
    params = sig.parameters.values()
    
    if not params:
        output_lines.append("  None")
    else:
        for param in params:
            param_str = ""
            
            # Manejar *args y **kwargs
            if param.kind == inspect.Parameter.VAR_POSITIONAL:
                param_str = f"  - *{param.name}" # ej: *args
            elif param.kind == inspect.Parameter.VAR_KEYWORD:
                param_str = f"  - **{param.name}" # ej: **kwargs
            else:
                param_str = f"  - {param.name}"
            
            # Añadir anotación de tipo (si existe)
            if param.annotation is not inspect.Parameter.empty:
                param_str += f" ({param.annotation.__name__})"
                
            # Añadir valor por defecto (si existe)
            if param.default is not inspect.Parameter.empty:
                # repr() es útil para poner comillas en los strings
                param_str += f", default={repr(param.default)}"
                
            output_lines.append(param_str)

    output_lines.append("") # Línea en blanco

    # 5. Añadir Tipo de Retorno
    output_lines.append("Returns:")
    return_type = sig.return_annotation
    
    if return_type is not inspect.Signature.empty:
        # Manejar casos donde el tipo no tiene __name__ (ej. Union)
        return_name = getattr(return_type, '__name__', str(return_type))
        output_lines.append(f"  {return_name}")
    else:
        output_lines.append("  None")
    
    output_lines.append("") # Línea en blanco

    # 6. (NUEVO) Añadir Uso de Ejemplo
    output_lines.append("Example Usage:")
    if example_text:
        # Añadimos indentación al texto del ejemplo
        for line in example_text.split('\n'):
            output_lines.append(f"  {line}")
    else:
        output_lines.append("  None")
        
    # Unir todas las líneas con un salto de línea
    return "\n".join(output_lines)

# --- Demo ---

def example_function(a: int, b: str = "default", *args, **kwargs) -> bool:
    """
    This is a complex example function.
    It serves to test the documentation generator.

    Example:
        >>> # Llama a la función con argumentos posicionales y kwargs
        >>> example_function(10, 'test', 1, 2, user='admin')
        True
        
        >>> # Llama con el valor 'a' por debajo del umbral
        >>> example_function(3)
        False
    """
    return a > 5 and bool(kwargs)

class MyClass:
    """
    A simple demo class. 
    El docstring de __init__ será combinado.
    """
    def __init__(self, value: int):
        """
        Initializes MyClass.

        Example:
            >>> c = MyClass(10)
            >>> c.value
            10
        """
        self.value = value

print("--- Demo 1: example_function ---")
print(get_doc(example_function))
print("\n" + "="*30 + "\n")

print("--- Demo 2: MyClass (combina docstrings) ---")
# get_doc es inteligente y combinará el docstring de la
# clase Y el de __init__, encontrando el bloque "Example:"
print(get_doc(MyClass))