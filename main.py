from pieces_location import update_position, white_pieces_start, black_pieces_start
from pieces_moves import get_possible_moves
from attacked_squares import get_attacked_squares
from random import choice

white_pieces = white_pieces_start
black_pieces = black_pieces_start

game_over = False

colors = ["white", "black"]
bot_color = choice(colors)
colors.remove(bot_color)
player_color = colors[0]

print("You're playing with the {} pieces".format(player_color))


white_pieces_locations = []
for piece in white_pieces:
    white_pieces_locations.append(piece.position)
black_pieces_locations = []
for piece in black_pieces:
    black_pieces_locations.append(piece.position)

white_possible_moves = []
black_possible_moves = []

print(get_attacked_squares(white_pieces, white_pieces_locations, black_pieces_locations, 1))
if player_color == "white":
    while not game_over:
        white_pieces_locations = []
        for piece in white_pieces:
            white_pieces_locations.append(piece.position)  
            black_pieces_locations = []
        for piece in black_pieces:
            black_pieces_locations.append(piece.position)
        white_possible_moves = get_possible_moves(white_pieces, white_pieces_locations, black_pieces_locations, 1)
        black_possible_moves = get_possible_moves(black_pieces, black_pieces_locations, white_pieces_locations, -1)
        while True:
            player_move = input("Type your move: ")
            if not player_move in white_possible_moves:
                print("Impossible move, try again!")
            else:
                update_position(player_move, player_color, black_pieces, white_pieces)
                break
        bot_move = choice(black_possible_moves)
        update_position(bot_move, bot_color, black_pieces, white_pieces)
        print(bot_move)
elif player_color == "black":
    while not game_over:
        white_pieces_locations = []
        for piece in white_pieces:
            white_pieces_locations.append(piece.position)  
            black_pieces_locations = []
        for piece in black_pieces:
            black_pieces_locations.append(piece.position)
        white_possible_moves = get_possible_moves(white_pieces, white_pieces_locations, black_pieces_locations, 1)
        black_possible_moves = get_possible_moves(black_pieces, black_pieces_locations, white_pieces_locations, -1)
        bot_move = choice(white_possible_moves)
        update_position(bot_move, bot_color, black_pieces, white_pieces)
        print(bot_move)
        while True:
            player_move = input("Type your move: ")
            if not player_move in black_possible_moves:
                print("Impossible move, try again!")
            else:
                update_position(player_move, player_color, black_pieces, white_pieces)
                break

    