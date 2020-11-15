from Node import Node
import math

class SlidingPuzzleSimple(Node):

    def get_method_name(self) -> str:
        return "Sliding Puzzle with simple H function"

    def evaluate_heuristic_function(self):
        result = 0
        n = int(math.sqrt(len(self.state)))
        if self.state[0] != (0, 0):
            result -= 1
        for x in range(n):
            for y in range(n):
                if (x, y) != self.state[n*x + y]:
                    result += 1
        return result




