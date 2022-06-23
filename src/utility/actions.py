from utility.constants import N_OF_CELL
from node.Node import Node


def actions() -> list:
    return four_actions() if N_OF_CELL == 4 else eight_actions()

def four_actions() -> list:
    return [
        lambda n: Node((n.board[0]+1, n.board[1], n.board[2], n.board[3])),
        lambda n: Node((n.board[0], n.board[1]+1, n.board[2], n.board[3])),
        lambda n: Node((n.board[0], n.board[1], n.board[2]+1, n.board[3])),
        lambda n: Node((n.board[0], n.board[1], n.board[2], n.board[3]+1))
    ]
    
def eight_actions() -> list:
    return [
        lambda n: Node((n.board[0]+1, n.board[1], n.board[2], n.board[3], n.board[4], n.board[5], n.board[6], n.board[7])),
        lambda n: Node((n.board[0], n.board[1]+1, n.board[2], n.board[3], n.board[4], n.board[5], n.board[6], n.board[7])),
        lambda n: Node((n.board[0], n.board[1], n.board[2]+1, n.board[3], n.board[4], n.board[5], n.board[6], n.board[7])),
        lambda n: Node((n.board[0], n.board[1], n.board[2], n.board[3]+1, n.board[4], n.board[5], n.board[6], n.board[7])),
        lambda n: Node((n.board[0], n.board[1], n.board[2], n.board[3], n.board[4]+1, n.board[5], n.board[6], n.board[7])),
        lambda n: Node((n.board[0], n.board[1], n.board[2], n.board[3], n.board[4], n.board[5]+1, n.board[6], n.board[7])),
        lambda n: Node((n.board[0], n.board[1], n.board[2], n.board[3], n.board[4], n.board[5], n.board[6]+1, n.board[7])),
        lambda n: Node((n.board[0], n.board[1], n.board[2], n.board[3], n.board[4], n.board[5], n.board[6], n.board[7]+1))
    ]