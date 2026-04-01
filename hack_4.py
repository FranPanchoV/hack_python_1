"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    """
    Transforma la última letra de la cadena 'fooziman' a mayúscula.
    """
    result = "fooziman"
    # Tomamos todo el texto menos la última letra,
    # y le sumamos la última letra convertida a mayúscula.
    result = result[:-1] + result[-1].upper()

    return result

print(fn_hack_4())
