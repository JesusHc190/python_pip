# Escribe un programa que reciba un texto y transforma lenguaje natural a "lenguaje hacker"
# (conocido realmemte como "leet" o "1337"). Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.

leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
        "J": ",_|", "K": ">|", "L": "1", "M": r"/\/\\", "N": r" ^/", "O": "0", "P": r" |*", "Q": "(_,)",
        "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": r"\/", "W": r"\/\/", "X": "><", "Y": "j", "Z": "2",
        "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}

text = "hola mundo"
hacker_text = ''
for character in text:
    if character.upper() in leet.keys():
        hacker_text += leet[character.upper()]
    else:
        hacker_text += character

print(hacker_text)