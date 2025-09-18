def checkmate(board: str):
    rows = board.strip().splitlines()
    board_size = len(rows)
    
    if board_size == 0:
        print("Error: invalid board")
        return
        
    for row in rows:
        if len(row) != board_size:
            print("Error: invalid board")  
            return
    
    king_row, king_col = find_king_position(rows, board_size)
    if king_row is None:
        print("Error: no King found")
        return
    
    pawn_attack = is_attacked_by_pawn(rows, board_size, king_row, king_col)
    knight_attack = is_attacked_by_knight(rows, board_size, king_row, king_col)  
    rook_queen_attack = is_attacked_straight_line(rows, board_size, king_row, king_col)
    bishop_queen_attack = is_attacked_diagonal_line(rows, board_size, king_row, king_col)
    
    if pawn_attack or knight_attack or rook_queen_attack or bishop_queen_attack:
        print("Success")
    else:
        print("Fail")


def find_king_position(rows, board_size):
    for i in range(board_size):
        for j in range(board_size):
            if rows[i][j] == 'K':
                return i, j
    return None, None


def is_attacked_by_pawn(rows, board_size, king_row, king_col):
    for i in range(board_size):
        for j in range(board_size):
            if rows[i][j] == 'P':
                pawn_attack_positions = [
                    (i - 1, j - 1),
                    (i - 1, j + 1)
                ]
                if (king_row, king_col) in pawn_attack_positions:
                    return True
    return False


def is_attacked_by_knight(rows, board_size, king_row, king_col):
    knight_moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    
    for dx, dy in knight_moves:
        knight_row = king_row + dx
        knight_col = king_col + dy
        if is_valid_position(knight_row, knight_col, board_size):
            if rows[knight_row][knight_col] == 'N':
                return True
    return False


def is_attacked_straight_line(rows, board_size, king_row, king_col):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    
    for dx, dy in directions:
        if scan_line_for_pieces(rows, board_size, king_row, king_col, dx, dy, ['R', 'Q']):
            return True
    return False


def is_attacked_diagonal_line(rows, board_size, king_row, king_col):
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]
    
    for dx, dy in directions:
        if scan_line_for_pieces(rows, board_size, king_row, king_col, dx, dy, ['B', 'Q']):
            return True
    return False


def scan_line_for_pieces(rows, board_size, start_row, start_col, dx, dy, target_pieces):
    current_row = start_row + dx
    current_col = start_col + dy
    
    while is_valid_position(current_row, current_col, board_size):
        piece = rows[current_row][current_col]
        if piece == '.':
            current_row += dx
            current_col += dy
            continue
        return piece in target_pieces
    
    return False


def is_valid_position(row, col, board_size):
    return 0 <= row < board_size and 0 <= col < board_size
