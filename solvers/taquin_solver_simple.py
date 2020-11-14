from Node import Node


class SlidingPuzzleSimple(Node):

    def get_method_name(self) -> str:
        return "Sliding Puzzle with simple H function"

    def evaluate_heuristic_function(self):
        result = 0
        if self.state[0] != (0, 0):
            result -= 1;
        for x in range(3):
            for y in range(3):
                if (x, y) != self.state[3*x + y]:
                    result += 1
        return result




