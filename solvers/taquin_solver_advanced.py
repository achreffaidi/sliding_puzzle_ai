from Node import Node
import math


class SlidingPuzzleAdvanced(Node):

    def get_method_name(self) -> str:
        return "Sliding Puzzle with Advanced H function"

    def evaluate_heuristic_function(self):
        result = 0
        n = int(math.sqrt(len(self.state)))
        for x in range(n):
            for y in range(n):
                (x1, y1) = self.state[n*x + y]
                if (x1, y1) != (0, 0):
                    result += abs(x1 - x) + abs(y1 - y)
        return result

