from pieces_start_location import white_pieces, black_pieces
from random import choice

# Tabuleiro baseado em coordenadas numéricas em vez de notação de xadrez
# a = 1, b = 2, c = 3
# Ex: a2 = (1, 2)
# nome das peças baseado na notação inglesa de xadrez

letters_coordinates = ("a", "b", "c", "d", "e", "f", "g", "h")
# transformar notação numérica em notação de xadrez:
# position = "{}{}".format(letters_coordinates[piece.position[0] - 1], piece.position[1])

game_over = False

colors = ["white", "black"]
bot_color = "white"
colors.remove(bot_color)
player_color = "black"

print("You're playing with the {} pieces".format(player_color))

player_move = None
if player_color == "white":
    player_move = input("Type your move: ")

while not game_over:
    bot_move = "e4"
    print(bot_move)
    player_move = input("Type your move: ")