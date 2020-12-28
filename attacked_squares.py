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
                attacking_squares.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
            
            piece.attacking_squares = attacking_squares


        if piece.name == "knight":
            pass
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