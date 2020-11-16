import math


class Node:
    def __init__(self, state: []):
        self.state = state
        self.cost = 0
        self.f = self.evaluate_heuristic_function()
        self.open = True

    def __lt__(self, other):
        return self.f < other.f

    def generate_next_nodes(self) -> []:
        pass

    def evaluate_heuristic_function(self):  # return Int
        pass

    def get_action_cost(self, child):  # return 1
        return 1

    def is_solution(self) -> bool:
        return self.evaluate_heuristic_function() == 0

    def increment_depth(self):
        pass

    def equals(self, node) -> bool:
        return self.state == node.state

    def is_open(self) -> bool:
        return self.open

    def set_closed(self):
        self.open = False

    def draw(self):# Show representation of the node. You can just print something
        n = int(math.sqrt(len(self.state)))
        for x in range(n):
            line = ""
            for y in range(n):
                line += f'{self.state[n*x +y]} '
            print(line)

    def get_method_name(self) -> str:
        pass
