
class Node:
    def __init__(self, state: []):
        self.state = state
        self.cost = 0
        self.open = True

    def generate_next_nodes(self) -> []:  # make sure to return list of Nodes
        pass
        # when u create the node make sure to set child.cost to self.cost + getActionCost(child)

    def evaluate_heuristic_function(self):  # return Int
        pass

    def get_action_cost(self, child):  # return 1
        pass

    def is_solution(self):
        pass

    def increment_depth(self):
        pass

    def equals(self, node) -> bool:
        pass

    def is_open(self) -> bool:
        pass

    def set_closed(self):
        pass

    def draw(self):  # Show representation of the node. You can just print something
        pass

    def get_method_name(self) -> str:
        pass
