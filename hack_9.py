"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""
def fn_hack_9():
    """
    Intercala el carácter '@' después de cada número en la lista [1, 2, 3]
    utilizando un bucle while.
    """
    original = [1, 2, 3]
    result = []
    i = 0
    # Mientras el índice sea menor al largo de la lista original
    while i < len(original):
        result.append(original[i]) # Añadimos el número
        result.append("@")         # Añadimos el símbolo
        i += 1                     # Incrementamos el contador
    return result

print(fn_hack_9())
