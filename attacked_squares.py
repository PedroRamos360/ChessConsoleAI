def item_in_list(item, list_object):
    if list_object.count(item) > 0:
        return True
    else:
        return False


letters_coordinates = ("a", "b", "c", "d", "e", "f", "g", "h")
def coordinates_to_chess_notation(move):
    new_move = "{}{}".format(letters_coordinates[move[0] - 1], move[1])
    return new_move


def get_attacked_squares(pieces, my_pieces_locations, opponent_pieces_locations, pawn_orientation):
    attacked_squares = []
    for piece in pieces:
        piece.attacking_squares = []
        if piece.name == "pawn":   
            attacking_squares = []
            diagonals = [(1, 1 * pawn_orientation), (-1, 1 * pawn_orientation)]
            for element in diagonals:
                x, y = piece.position
                x += element[0]
                y += element[1]
                if (x > 0 and x < 9) and (y > 0 and y < 9):
                    attacking_squares.append("{}".format(coordinates_to_chess_notation((x, y))))
            
            piece.attacking_squares = attacking_squares


        if piece.name == "knight":
            for i in range(2):
                change_in_x = 0
                change_in_y = 0
                if i == 0:
                    change_in_x = 1
                    change_in_y= 2
                if i == 1:
                    change_in_x = 2
                    change_in_y= 1
                move = (piece.position[0] +change_in_x, piece.position[1] +change_in_y)
                piece.attacking_squares.append(move)
                move = (piece.position[0] +change_in_x, piece.position[1] -change_in_y)
                piece.attacking_squares.append(move)
                move = (piece.position[0] -change_in_x, piece.position[1] +change_in_y)
                piece.attacking_squares.append(move)
                move = (piece.position[0] -change_in_x, piece.position[1] -change_in_y)
                piece.attacking_squares.append(move)

            attacking_squares = []
            for attacking_square in piece.attacking_squares:
                # Checa se tem alguma peça no quadrado
                # Checa se a peça não saiu do tabuleiro
                if (attacking_square[0] >= 1 and attacking_square[1] >= 1 and 
                    attacking_square[0] <= 8 and attacking_square[1] <= 8 and
                    not item_in_list(attacking_square, my_pieces_locations)):
                    attacking_squares.append("{}".format(coordinates_to_chess_notation(attacking_square)))
            
            piece.attacking_squares = attacking_squares

        if piece.name == "bishop":
            pass
        if piece.name == "rook":
            pass
        if piece.name == "queen":
            pass
        if piece.name == "king":
            pass
                
        for attacked_square in piece.attacking_squares:
            attacked_squares.append(attacked_square)
    
    return attacked_squares