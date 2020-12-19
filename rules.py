from pieces_start_location import white_pieces, black_pieces

letters_coordinates = ("a", "b", "c", "d", "e", "f", "g", "h")
piece_name_notation = {
    "pawn": "",
    "knight": "N",
    "bishop": "B",
    "rook": "R",
    "queen": "Q",
    "king": "K",
}

def name_to_notation(piece):
    for key, value in piece_name_notation.items():
        if key == piece:
            return value

def item_in_list(item, list_object):
    if list_object.count(item) > 0:
        return True
    else:
        return False

def coordinates_to_chess_notation(move):
    new_move = "{}{}".format(letters_coordinates[move[0] - 1], move[1])
    return new_move

white_pieces_locations = []
for piece in white_pieces:
    white_pieces_locations.append(piece.position)
black_pieces_locations = []
for piece in black_pieces:
    black_pieces_locations.append(piece.position)


for piece in white_pieces:
    position = "{}{}".format(letters_coordinates[piece.position[0] - 1], piece.position[1])
    print("Movimentos possíveis para a peça de {}:".format(position))
    if piece.name == "pawn":
        if not piece.has_moved:
            move = (piece.position[0], piece.position[1] + 1)
            piece.legal_moves.append(move)

            move = (piece.position[0], piece.position[1] + 2)
            piece.legal_moves.append(move)
        else:
            move = (piece.position[0], piece.position[1] + 1)
            piece.legal_moves.append(move)
        
        legal_moves = []
        # Checa se tem alguma peça no caminho
        for legal_move in piece.legal_moves:
            if not (item_in_list(legal_move, white_pieces_locations)
                or item_in_list(legal_move, black_pieces_locations)):
                legal_moves.append("{}".format(coordinates_to_chess_notation(legal_move)))
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
                not item_in_list(legal_move, white_pieces_locations)):
                legal_moves.append("N{}".format(coordinates_to_chess_notation(legal_move)))
   
        piece.legal_moves = legal_moves
    
    if piece.name == "rook":
        on_board = True
        no_piece_in_way = True
        for element in [1, -1]:
            x, y = piece.position
            while no_piece_in_way and on_board:
                y += element
                if (x < 1 or y < 1 or 
                    x > 8 or y > 8 or
                    item_in_list((x, y), white_pieces_locations)):
                    break
                else:
                    move = (x, y)
                    piece.legal_moves.append("R{}".format(coordinates_to_chess_notation(move)))
        for element in [1, -1]:
            x, y = piece.position
            while no_piece_in_way and on_board:
                x += element
                if (x < 1 or y < 1 or 
                    x > 8 or y > 8 or
                    item_in_list((x, y), white_pieces_locations)):
                    break
                else:
                    move = (x, y)
                    piece.legal_moves.append("R{}".format(coordinates_to_chess_notation(move)))
                

        
    for legal_move in piece.legal_moves:
        print(legal_move)
