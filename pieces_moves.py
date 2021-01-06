from attacked_squares import get_attacked_squares
from pieces_location import update_position

def item_in_list(item, list_object):
    if list_object.count(item) > 0:
        return True
    else:
        return False


letters_coordinates = ("a", "b", "c", "d", "e", "f", "g", "h")
def coordinates_to_chess_notation(move):
    new_move = "{}{}".format(letters_coordinates[move[0] - 1], move[1])
    return new_move


def get_pieces_by_name(name, pieces):
    pieces_wanted = []
    for piece in pieces:
        if piece.name == name:
            pieces_wanted.append(piece)
    
    return pieces_wanted

def get_piece_by_name(name, pieces):
    for piece in pieces:
        if piece.name == name:
            return piece


def get_possible_moves(my_pieces, opponent_pieces, my_pieces_locations, opponent_pieces_locations, pawn_orientation):
    possible_moves = []
    # Roque
    # my_rooks = get_pieces_by_name("rook", pieces)
    for piece in my_pieces:
        piece.legal_moves = []
        if piece.name == "pawn":
            if piece.position[1] != 2 and pawn_orientation == 1:
                piece.has_moved = True
            if piece.position[1] != 7 and pawn_orientation == -1:
                piece.has_moved = True
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
                # Checa se tem alguma peça no quadrado
                # Checa se a peça não saiu do tabuleiro
                if (legal_move[0] >= 1 and legal_move[1] >= 1 and 
                    legal_move[0] <= 8 and legal_move[1] <= 8 and
                    not item_in_list(legal_move, my_pieces_locations)):
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
            legal_moves = []
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
                        legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))

            for element in [1, -1]:
                for i in range(1):
                    x, y = piece.position
                    y += element
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))

            for element in [1, -1]:
                for i in range(1):
                    x, y = piece.position
                    x += element
                    if (x < 1 or y < 1 or 
                        x > 8 or y > 8 or
                        item_in_list((x, y), my_pieces_locations)):
                        break
                    elif item_in_list((x, y), opponent_pieces_locations):
                        legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))
                        break
                    else:
                        legal_moves.append("{}-{}".format(coordinates_to_chess_notation(piece.position), coordinates_to_chess_notation((x, y))))

            attacked_squares = get_attacked_squares(my_pieces, my_pieces_locations, opponent_pieces_locations, pawn_orientation)
            attacked_squares_without_piece_name = []
            for attacked_square in attacked_squares:
                attacked_squares_without_piece_name.append(attacked_square[-2:])
            
            for legal_move in legal_moves:
                if not item_in_list(legal_move[-2:], attacked_squares_without_piece_name):
                    piece.legal_moves.append(legal_move)

        king_attacked = False
        attacked_squares = get_attacked_squares(opponent_pieces, opponent_pieces_locations, my_pieces_locations, pawn_orientation*-1)
        attacked_squares_without_piece_name = []
        for attacked_square in attacked_squares:
            attacked_squares_without_piece_name.append(attacked_square[-2:])
        my_king = get_piece_by_name("king", my_pieces)
        if item_in_list(coordinates_to_chess_notation(my_king.position), attacked_squares_without_piece_name):
            king_attacked = True
        else:
            king_attacked = False


        for legal_move in piece.legal_moves:
            possible_moves.append(legal_move)

    if king_attacked:
        possible_moves_king_attacked = []
        for legal_move in possible_moves:
            # Criação de váriaveis para não mudar a posição original
            my_pieces_after_move = my_pieces
            opponent_pieces_after_move = opponent_pieces
            opponent_pieces_locations_after_move = opponent_pieces_locations
            my_pieces_locations_after_move = my_pieces_locations

            # Usa a cópia das váriaveis acima para atualizar uma posição hipotética que surgiria depois da jogada
            if pawn_orientation == 1:
                #primeiro as peças das pretas depois das brancas
                update_position(legal_move, 'white', opponent_pieces_after_move, my_pieces_after_move)
            else:
                update_position(legal_move, 'black', my_pieces_after_move, opponent_pieces_after_move)

            # pega os ataques
            attacked_squares = get_attacked_squares(opponent_pieces_after_move, 
                opponent_pieces_locations_after_move, 
                my_pieces_locations_after_move, 
                pawn_orientation*-1
            )

            attacked_squares_without_piece_name = []
            for attacked_square in attacked_squares:
                attacked_squares_without_piece_name.append(attacked_square[-2:])
                my_king = get_piece_by_name("king", my_pieces)
            if not item_in_list(coordinates_to_chess_notation(my_king.position), attacked_squares_without_piece_name):
                # Rei não está atacado, portanto o movimento é possível
                possible_moves_king_attacked.append(legal_move)
        
        possible_moves = possible_moves_king_attacked

    '''
    Consertar bug: Jogo interpreta xeque como xeque-mate
    '''
    return possible_moves