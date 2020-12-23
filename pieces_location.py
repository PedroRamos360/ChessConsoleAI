from piece import Piece

white_pieces_start = [
    # Peças
    Piece((1, 1), "rook", "white"),
    Piece((2, 1), "knight", "white"),
    Piece((3, 1), "bishop", "white"),
    Piece((4, 1), "queen", "white"),
    Piece((5, 1), "king", "white"),
    Piece((6, 1), "bishop", "white"),
    Piece((7, 1), "knight", "white"),
    Piece((8, 1), "rook", "white"),
    # Peões
    Piece((1, 2), "pawn", "white"),
    Piece((2, 2), "pawn", "white"),
    Piece((3, 2), "pawn", "white"),
    Piece((4, 2), "pawn", "white"),
    Piece((5, 2), "pawn", "white"),
    Piece((6, 2), "pawn", "white"),
    Piece((7, 2), "pawn", "white"),
    Piece((8, 2), "pawn", "white")
]

black_pieces_start = [
    # Peças
    Piece((1, 8), "rook", "black"),
    Piece((2, 8), "knight", "black"),
    Piece((3, 8), "bishop", "black"),
    Piece((4, 8), "queen", "black"),
    Piece((5, 8), "king", "black"),
    Piece((6, 8), "bishop", "black"),
    Piece((7, 8), "knight", "black"),
    Piece((8, 8), "rook", "black"),
    # Peões
    Piece((1, 7), "pawn", "black"),
    Piece((2, 7), "pawn", "black"),
    Piece((3, 7), "pawn", "black"),
    Piece((4, 7), "pawn", "black"),
    Piece((5, 7), "pawn", "black"),
    Piece((6, 7), "pawn", "black"),
    Piece((7, 7), "pawn", "black"),
    Piece((8, 7), "pawn", "black")
]

letters_coordinates = ("a", "b", "c", "d", "e", "f", "g", "h")

def delete_piece_by_location(piece_position, list_of_pieces):
    for piece in list_of_pieces:
        if piece.position == piece_position:
            list_of_pieces.remove(piece)

def move_piece(position_now, new_position, list_of_pieces):
    for piece in list_of_pieces:
        if piece.position == position_now:
            piece.position = new_position

def update_position(move, piece_color, black_pieces, white_pieces):
    position_now, new_position = move.split("-")

    x = letters_coordinates.index(new_position[-2]) + 1
    y = int(new_position[-1])
    new_position = (x, y)

    x = letters_coordinates.index(position_now[-2]) + 1
    y = int(position_now[-1])
    position_now = (x, y)
    
    if piece_color == "white":
        delete_piece_by_location(new_position, black_pieces)
        move_piece(position_now, new_position, white_pieces)
    elif piece_color == "black":
        delete_piece_by_location(new_position, white_pieces)
        move_piece(position_now, new_position, white_pieces)

