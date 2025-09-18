def checkmate(board: str):
    rows_data = board.strip().splitlines()
    board_size = len(rows_data)
        
    for row in rows_data:
        if len(row) != board_size or board_size == 0:
            print("Error: invalid board")  
            return
    
    kr, kc = find_king_position(rows_data, board_size)

    if kr is None or kc is None:
        print("Error: no King found")
        return
    
    pawn_attack = is_attacked_by_pawn(rows_data, board_size, kr, kc)
    rook_queen_attack = is_attacked_straight_line(rows_data, board_size, kr, kc)
    bishop_queen_attack = is_attacked_diagonal_line(rows_data, board_size, kr, kc)
    
    if pawn_attack or rook_queen_attack or bishop_queen_attack:
        print("Success")
    else:
        print("Fail")


def find_king_position(rows_data, board_size):
    for i in range(board_size):
        for j in range(board_size):
            if rows_data[i][j] == 'K':
                return i, j
    return None, None

def is_attacked_by_pawn(rows_data, board_size, kr, kc):
    for i in range(board_size):
        for j in range(board_size):
            if rows_data[i][j] == 'P':
                pawn_attack_positions = [
                    (i - 1, j - 1),
                    (i - 1, j + 1)
                ]
                if (kr, kc) in pawn_attack_positions:
                    return True
    return False

def is_attacked_straight_line(rows_data, board_size, kr, kc):
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    
    for dx, dy in directions:
        if scan_line_for_pieces(rows_data, board_size, kr, kc, dx, dy, ['R', 'Q']):
            return True
    return False

def is_attacked_diagonal_line(rows_data, board_size, kr, kc):
    directions = [
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]
    
    for dx, dy in directions:
        if scan_line_for_pieces(rows_data, board_size, kr, kc, dx, dy, ['B', 'Q']):
            return True
    return False

def scan_line_for_pieces(rows_data, board_size, start_row, start_col, dx, dy, target_pieces):
    current_row = start_row + dx
    current_col = start_col + dy
    
    while is_valid_position(current_row, current_col, board_size):
        piece = rows_data[current_row][current_col]
        if piece == '.':
            current_row += dx
            current_col += dy
            continue
        return piece in target_pieces
    
    return False


def is_valid_position(row, col, board_size):
    return 0 <= row < board_size and 0 <= col < board_size
