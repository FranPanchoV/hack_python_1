"""
loop: while [] output => [5,4,3,2,1,0]
"""
def fn_hack_7():
    """
    Llena una lista con los números del 5 al 0 usando un bucle while.
    """
    result = []
    i = 5
    while i >= 0:
        result.append(i)
        i -= 1          
    return result

print(fn_hack_7())
