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

    def generate_next_nodes(self) -> []:  # make sure to return list of Nodes
        empty_position_index = self.state.index((0, 0))
        initial_state = self.state.copy()
        items = ""
        (m, n) = self.size
        if empty_position_index in range(n):
            items += 'b'
        elif empty_position_index in range(m * n - n, m * n):
            items += 'h'
        else:
            items += 'hb'

        if empty_position_index % n == 0:
            items += 'd'
        elif empty_position_index % n == n - 1:
            items += 'g'
        else:
            items += 'gd'

        next_states_list = []
        if items.__contains__('b'):
            new_state = self.state.copy()
            new_state[empty_position_index] = new_state[empty_position_index + n]
            new_state[empty_position_index + n] = (0, 0)
            next_states_list.append(new_state)

        if items.__contains__('h'):
            new_state = self.state.copy()
            new_state[empty_position_index] = new_state[empty_position_index - n]
            new_state[empty_position_index - n] = (0, 0)
            next_states_list.append(new_state)

        if items.__contains__('g'):
            new_state = self.state.copy()
            new_state[empty_position_index] = new_state[empty_position_index - 1]
            new_state[empty_position_index - 1] = (0, 0)
            next_states_list.append(new_state)

        if items.__contains__('d'):
            new_state = self.state.copy()
            new_state[empty_position_index] = new_state[empty_position_index + 1]
            new_state[empty_position_index + 1] = (0, 0)
            next_states_list.append(new_state)

        nodes_list = []

        for node_state in next_states_list:
            node_to_add = SlidingPuzzleSimple(node_state, m, n)
            node_to_add.cost = self.cost + self.get_action_cost(node_to_add)
            nodes_list.append(node_to_add)

        return nodes_list





