import Node as Node


class Solver:
    def __init__(self, initial_node: Node):
        self.nodes = [initial_node]
        self.solution: Node = None

    def __contains__(self, item: Node):
        for c in self.nodes:
            if item.equals(c):
                return True
        return False

    def generate_nodes_from(self, node: Node):
        generated: [] = node.generate_next_nodes()
        for c in generated:
            if c not in self:
                self.nodes.append(c)

    def move_next(self, show_steps: bool):
        min_cost: float = float('inf')
        best_node: Node = None
        c: Node
        # Find best Node
        for c in self.nodes:
            if not c.is_open():
                continue
            h = c.evaluate_heuristic_function()
            f = c.cost
            total_cost = h + f
            if total_cost < min_cost:
                best_node = c
                min_cost = total_cost
        # Close that Node to prevent visiting it again. ( Alert : This can be buggy )
        best_node.set_closed()
        if show_steps:
            best_node.draw()
        if best_node.is_solution():
            self.solution = best_node
            return True
        return False

    def solve(self, show_steps: bool):
        iterations: float = 0
        while self.solution is None:
            if show_steps:
                print("Iteration Number : " + str(iterations))
            self.move_next(show_steps)
            iterations += 1
        # When find solution show it
        print("===============================")
        print("======== Solution Found =======")
        print("======= Iterations :" + str(iterations) + "=====")
        print("===============================")
        self.solution.draw()
