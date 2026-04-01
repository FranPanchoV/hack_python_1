"""
loop: while [] output => [5,4,3,2,1,0]
"""
def fn_hack_7():
    """
    Llena una lista con los números del 5 al 0 usando un bucle while.
    """
    result = []
    i = 5  # Empezamos en 5
    while i >= 0:      # Mientras i sea mayor o igual a 0
        result.append(i) # Añadimos el número actual a la lista
        i -= 1           # Restamos 1 a i en cada vuelta
    return result

print(fn_hack_7())
