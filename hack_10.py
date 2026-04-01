"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""
def fn_hack_10():
    """
    Transforma 'fooziman' en una lista de caracteres con reemplazos
    específicos y todo en mayúsculas: ["F","0","0","Z","1","M","@","N"]
    """
    result = "fooziman"
    # 1. Primero aplicamos todos los reemplazos de caracteres y pasamos a mayúsculas
    result = result.replace("o", "0").replace("i", "1").replace("a", "@").upper()
    # 2. Convertimos el string resultante en una lista de caracteres
    result = list(result)
    return result

print(fn_hack_10())
