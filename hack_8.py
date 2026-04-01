"""
list: [1,3,5,7,9] output => [3,5,7]
"""
def fn_hack_8():
    """
    Extrae una sub-lista (segmento) de la lista original [1, 3, 5, 7, 9].
    """
    result = [1, 3, 5, 7, 9]
    # Usamos slicing para obtener desde el índice 1 hasta el 4 (sin incluir el 4)
    result = result[1:4]
    return result

print(fn_hack_8())
