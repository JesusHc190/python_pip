# Escribe un programa que muestre por consola (con un print) los
# números de 1 al 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra de "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y 5 a la vez por la palabra "fizzbuzz".

for i in range(1, 101):
    print("fizzbuzz" if i % 3 == 0 and i % 5 == 0 else
          "fizz" if i % 3 == 0 else
          "buzz" if i % 5 == 0 else i)