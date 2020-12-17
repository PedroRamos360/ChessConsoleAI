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


for piece in white_pieces:
    position = "{}{}".format(letters_coordinates[piece.position[0] - 1], piece.position[1])
    print("A peça de {} pode ir para:".format(position))
    if piece.name == "pawn":
        if not piece.has_moved:
            move = (piece.position[0], piece.position[1] + 1)
            piece.legal_moves.append(move)

            move = (piece.position[0], piece.position[1] + 2)
            piece.legal_moves.append(move)
        else:
            move = (piece.position[0], piece.position[1] + 1)
            piece.legal_moves.append(move)

    for legal_move in piece.legal_moves:
        move = "{}{}".format(letters_coordinates[legal_move[0] - 1], legal_move[1])
        print(move)
