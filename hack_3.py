"""
text: "fooziman" output => "Fooziman"
"""

def fn_hack_3():
    """
    Transforma el texto 'fooziman' para que inicie con mayúscula.
    """
    result = "fooziman"
    result = result.capitalize()
    return result

print(fn_hack_3())
