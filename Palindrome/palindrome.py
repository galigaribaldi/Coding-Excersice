import string

def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome ignoring spaces and punctuation.
    """
    # Normalizamos el string: minúsculas + solo caracteres alfanuméricos
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Comparamos con su reverso
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("hello"))  # False
    print(is_palindrome("No 'x' in Nixon"))  # True
