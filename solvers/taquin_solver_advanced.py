from Node import Node


class SlidingPuzzleAdvanced(Node):

    def get_method_name(self) -> str:
        return "Sliding Puzzle with Advanced H function"

    def evaluate_heuristic_function(self):
        result = 0
        for x in range(3):
            for y in range(3):
                (x1, y1) = self.state[3*x + y]
                if (x1, y1) != (0, 0):
                    result += abs(x1 - x) + abs(y1 - y)
        return result

