from utility.constants import N_OF_CELL

def restrictions() -> list:
    return four_restrictions() if N_OF_CELL == 4 else eight_restrictions()

def four_restrictions() -> list:
    return [
        lambda n: n.board[0] < N_OF_CELL-1 and verify_board(n, 0),
        lambda n: n.board[1] < N_OF_CELL-1 and verify_board(n, 1),
        lambda n: n.board[2] < N_OF_CELL-1 and verify_board(n, 2),
        lambda n: n.board[3] < N_OF_CELL-1 and verify_board(n, 3) 
    ]
    
def eight_restrictions() -> list:
    return [
        lambda n: n.board[0] < N_OF_CELL-1 and verify_board(n, 0),
        lambda n: n.board[1] < N_OF_CELL-1 and verify_board(n, 1),
        lambda n: n.board[2] < N_OF_CELL-1 and verify_board(n, 2),
        lambda n: n.board[3] < N_OF_CELL-1 and verify_board(n, 3),
        lambda n: n.board[4] < N_OF_CELL-1 and verify_board(n, 4),
        lambda n: n.board[5] < N_OF_CELL-1 and verify_board(n, 5),
        lambda n: n.board[6] < N_OF_CELL-1 and verify_board(n, 6),
        lambda n: n.board[7] < N_OF_CELL-1 and verify_board(n, 7)
    ]

def verify_board(n, index: int) -> bool:
    return n.board.count(n.board[index] + 1) == 0