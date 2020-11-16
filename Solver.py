import Node as Node
import heapq

class Solver:
    def __init__(self, initial_node):
        self.nodes = [initial_node]
        heapq.heapify(self.nodes)
        self.solution = None
        self.iterations: float = 0

    def __contains__(self, item):
        for c in self.nodes:
            if item.equals(c):
                return True
        return False

    def generate_nodes_from(self, node):
        generated: [] = node.generate_next_nodes()
        for c in generated:
            if c not in self and c is not None and self.nodes is not None:
                heapq.heappush(self.nodes, c)

    def move_next(self, show_steps: bool):
        current = heapq.heappop(self.nodes)
        if show_steps:
            current.draw()
        if current.is_solution():
            self.solution = current
            return True
        self.generate_nodes_from(current)
        return False

    def solve(self, show_steps: bool):

        while self.solution is None:
            if show_steps:
                print("Iteration Number : " + str(self.iterations))
                print("length : " + str(len(self.nodes)))
            self.move_next(show_steps)
            self.iterations += 1
        # When find solution show it
        print("===============================")
        print("======== Solution Found =======")
        print(self.solution.get_method_name())
        print("======= Iterations :" + str(self.iterations) + "=====")
        print("===============================")
        self.solution.draw()

