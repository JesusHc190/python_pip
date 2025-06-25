# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar contraseñas con los siguientes parámetros;
# - Longitud: Entre 8 y 16.
# - Con o sin mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos esos parámetros entre ellos).

import random
def generar_pass(lenght, is_mayus = False, is_number = False, is_simb = False):
    password = ""

    charts = list(range(97, 123))

    if is_mayus:
        charts += list(range(65, 91))
    if is_number:
        charts += list(range(48, 58))
    if is_simb:
        charts += list(range(33, 48)) + list(range(58, 65))
    
    if lenght > 16 or lenght < 8:
        lenght = 8
    while (len(password) < lenght):
        password += chr(random.choice(charts))
    return password

pass_gen = generar_pass(1, True, True, True)
print(pass_gen)
