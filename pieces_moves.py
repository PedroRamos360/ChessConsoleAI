def item_in_list(item, list_object):
    if list_object.count(item) > 0:
        return True
    else:
        return False

letters_coordinates = ("a", "b", "c", "d", "e", "f", "g", "h")

def coordinates_to_chess_notation(move):
    new_move = "{}{}".format(letters_coordinates[move[0] - 1], move[1])
    return new_move


def get_possible_moves(pieces, my_pieces_locations, opponent_pieces_locations, pawn_orientation):
    possible_moves = []
    for piece in pieces:
        piece.legal_moves = []
        if piece.name == "pawn":
            if not piece.has_moved:
                move = (piece.position[0], piece.position[1] + 1 * pawn_orientation)
                piece.legal_moves.append(move)
                if (not item_in_list(move, my_pieces_locations) and
                    not item_in_list(move, opponent_pieces_locations)):
                    move = (piece.position[0], piece.position[1] + 2 * pawn_orientation)
                    piece.legal_moves.append(move)
            else:
                move = (piece.position[0], piece.position[1] + 1 * pawn_orientation)
                piece.legal_moves.append(move)
            
            legal_moves = []
            # Checa se tem alguma peça no caminho
            for legal_move in piece.legal_moves:
                if not (item_in_list(legal_move, my_pieces_locations)
                    or item_in_list(legal_move, opponent_pieces_locations)):
                    legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation(legal_move)))

            diagonals = [(1, 1 * pawn_orientation), (-1, 1 * pawn_orientation)]
            for element in diagonals:
                x, y = piece.position
                x += element[0]
                y += element[1]
                if item_in_list((x, y), opponent_pieces_locations):
                    legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
            
            
            piece.legal_moves = legal_moves


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
                piece.legal_moves.append(move)
                move = (piece.position[0] +change_in_x, piece.position[1] -change_in_y)
                piece.legal_moves.append(move)
                move = (piece.position[0] -change_in_x, piece.position[1] +change_in_y)
                piece.legal_moves.append(move)
                move = (piece.position[0] -change_in_x, piece.position[1] -change_in_y)
                piece.legal_moves.append(move)

            legal_moves = []
            for legal_move in piece.legal_moves:
                # Checa se tem alguma peça no caminho
                # Checa se a peça não saiu do tabuleiro
                if (legal_move[0] >= 1 and legal_move[1] >= 1 and 
                    legal_move[0] <= 8 and legal_move[1] <= 8 and
                    not item_in_list(legal_move, my_pieces_locations) and
                    item_in_list(legal_move, opponent_pieces_locations)):
                    legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation(legal_move)))
                elif ((legal_move[0] >= 1 and legal_move[1] >= 1 and 
                    legal_move[0] <= 8 and legal_move[1] <= 8 and
                    not item_in_list(legal_move, my_pieces_locations) and
                    not item_in_list(legal_move, opponent_pieces_locations))):
                    legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation(legal_move)))
    
            piece.legal_moves = legal_moves
        
        if piece.name == "bishop":
            diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
            for element in diagonals:
                x, y = piece.position
                while True:
                    x += element[0]
                    y += element[1]
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y)))) 
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
        
        if piece.name == "rook":
            for element in [1, -1]:
                x, y = piece.position
                while True:
                    y += element
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
            for element in [1, -1]:
                x, y = piece.position
                while True:
                    x += element
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
        
        if piece.name == "queen":
            diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
            for element in diagonals:
                x, y = piece.position
                while True:
                    x += element[0]
                    y += element[1]
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y)))) 
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
            for element in [1, -1]:
                x, y = piece.position
                while True:
                    y += element
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
            for element in [1, -1]:
                x, y = piece.position
                while True:
                    x += element
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
            
        if piece.name == "king":
            diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
            for element in diagonals:
                for i in range(1):  # para o break quebrar esse loop
                    x, y = piece.position
                    x += element[0]
                    y += element[1]
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))

            for element in [1, -1]:
                for i in range(1):
                    x, y = piece.position
                    y += element
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))

            for element in [1, -1]:
                for i in range(1):
                    x, y = piece.position
                    x += element
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        piece.legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                    

        for legal_move in piece.legal_moves:
            possible_moves.append(legal_move)
    
    return possible_moves