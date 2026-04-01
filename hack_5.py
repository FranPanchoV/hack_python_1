"""
text: "fooziman" output => "f00z1m@n"
"""
def fn_hack_5():
    """
    Reemplaza letras específicas por números y símbolos en 'fooziman'.
    'o' -> '0', 'i' -> '1', 'a' -> '@'
    """
    result = "fooziman"
    # Reemplazamos cada carácter uno por uno
    result = result.replace("o", "0").replace("i", "1").replace("a", "@")
    return result

print(fn_hack_5())
