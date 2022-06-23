from utility.functions import get_init
    
class Node:
    def __init__(self, board: tuple = get_init()) -> None:
        self.board = board
        self.next = None
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other) -> bool:
        return self.board == other.board