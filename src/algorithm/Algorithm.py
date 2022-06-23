from utility.actions import actions
from utility.restrictions import restrictions
from node.Node import Node


class Algorithm:
    def __init__(self) -> None:
        self.actions = actions()
        self.restrictions = restrictions()

    def heuristic(self, current) -> int:
        rows = current.board
        h = 0
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                # Reinas en la misma rows
                if rows[i] == rows[j]:
                    h += 1
                # Reinas en diagonal
                if rows[i] + i == rows[j] + j:
                    h += 1
                if rows[i] - i == rows[j] - j:
                    h += 1
        return h
    
    def evaluate_path(self, init):
        init_node = Node(init)
        init_node.h = self.heuristic(init_node)
        open_nodes = []
        close_nodes = []
        open_nodes.append(init_node)
        
        while len(open_nodes) > 0:
            i = 0
            for index, item in enumerate(open_nodes):
                if item.f < open_nodes[0].f:
                    i = index
                    
            current = open_nodes.pop(i)
            if current.h == 0:
                if current.next is None:
                    return current
                while current.next.next is not None:
                    current = current.next
                return current
            
            close_nodes.append(current)
            successors = []
            for act, res in zip(self.actions, self.restrictions):
                if res(current):
                    successors.append(act(current))
                    
            for succ in successors:
                g = current.g + 1
                best = False
                
                if succ not in open_nodes:
                    succ.h = self.heuristic(succ)
                    open_nodes.append(succ)
                    best = True
                elif current.g < succ.g:
                    best = True
                if best:
                    succ.next = current
                    succ.g = g
                    succ.f = succ.g + succ.h
        return None
                
            