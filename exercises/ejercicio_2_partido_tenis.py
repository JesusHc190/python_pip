# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.

# - Las puntuaciónes de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
# 15 - Love
# 30 - Love
# 30 - 15
# 30 - 30
# 40 - 30
# Deuce
# Ventaja P1
# Ha ganado el P1

from enum import Enum 

class Player(Enum):
    P1 = 1
    P2 = 2


def tenis_game(points):
    game = ["Love", "15", "30", "40"]
    points_p1 = 0
    points_p2 = 0

    for player in points:

        if player == Player.P1:
            points_p1 += 1
        elif player == Player.P2:
            points_p2 += 1

        if points_p1 >= 3 and points_p2 >=3:
            if abs(points_p1 - points_p2) <= 1:
                print("Deuce" if points_p1 == points_p2 else
                    "Ventaja P1" if points_p1 > points_p2 else "Ventaja P2")
            else:
                break
        else:
            if points_p1 < 4 or points_p2 < 4:
                print(f"{game[points_p1]} - {game[points_p2]}")
            else:
                break
    print("Ha ganado P1" if points_p1 > points_p2 else "Ha ganado P2")
        

tenis_game([Player.P1, Player.P1, Player.P2, Player.P2, Player.P1, Player.P2, Player.P1, Player.P1])


