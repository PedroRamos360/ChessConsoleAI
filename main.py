from pieces_location import update_position, get_new_locations, white_pieces_start, black_pieces_start
from pieces_moves import get_possible_moves
from attacked_squares import get_attacked_squares
from random import choice

white_pieces = white_pieces_start
black_pieces = black_pieces_start

black_wins = False
white_wins = False

colors = ["white", "black"]
bot_color = choice(colors)
# bot_color = "white"
# bot_color = "black"
colors.remove(bot_color)
player_color = colors[0]

print("You're playing with the {} pieces".format(player_color))


white_pieces_locations, black_pieces_locations = get_new_locations(white_pieces, black_pieces)

white_possible_moves = []
black_possible_moves = []

if player_color == "white":
    while True:
        white_possible_moves = get_possible_moves(white_pieces, black_pieces, white_pieces_locations, black_pieces_locations, 1)
        if white_possible_moves == []:
            print("Black wins by checkmate")
            break
        while True:
            player_move = input("Type your move: ")
            if not player_move in white_possible_moves:
                print("Impossible move, try again!")
            else:
                update_position(player_move, player_color, black_pieces, white_pieces)
                white_pieces_locations, black_pieces_locations = get_new_locations(white_pieces, black_pieces)
                break
            
        black_possible_moves = get_possible_moves(black_pieces, white_pieces, black_pieces_locations, white_pieces_locations, -1)
        if black_possible_moves == []:
            print("White wins by checkmate")
            break
        bot_move = choice(black_possible_moves)

        update_position(bot_move, bot_color, black_pieces, white_pieces)
        white_pieces_locations, black_pieces_locations = get_new_locations(white_pieces, black_pieces)

        print(bot_move)
elif player_color == "black":
    while True:
        white_possible_moves = get_possible_moves(white_pieces, black_pieces, white_pieces_locations, black_pieces_locations, 1)
        if white_possible_moves == []:
            print("Black wins by checkmate")
            break
        bot_move = choice(white_possible_moves)

        update_position(bot_move, bot_color, black_pieces, white_pieces)
        white_pieces_locations, black_pieces_locations = get_new_locations(white_pieces, black_pieces)

        print(bot_move)
        black_possible_moves = get_possible_moves(black_pieces, white_pieces, black_pieces_locations, white_pieces_locations, -1)
        if black_possible_moves == []:
            print("White wins by checkmate")
            break
        while True:
            player_move = input("Type your move: ")
            if not player_move in black_possible_moves:
                print("Impossible move, try again!")
            else:
                update_position(player_move, player_color, black_pieces, white_pieces)
                white_pieces_locations, black_pieces_locations = get_new_locations(white_pieces, black_pieces)
                break

    

    