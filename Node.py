
class Node:
    def __init__(self, state: []):
        self.state = state
        self.cost = 0
        self.open = True

    def generate_next_nodes(self) -> []:  # make sure to return list of Nodes
        empty_position_index = self.state.index((0, 0))
        initial_state = self.state.copy()
        items = ""
        if empty_position_index in range(3):
            items += 'b'
        elif empty_position_index in range(3, 6):
            items += 'hb'
        else:
            items += 'h'

        if empty_position_index in [0, 3, 6]:
            items += 'd'
        elif empty_position_index in [1, 4, 7]:
            items += 'gd'
        else:
            items += 'g'

        next_states_list = []
        if items.__contains__('b'):
            new_state = self.state.copy()
            new_state[empty_position_index] = new_state[empty_position_index + 3]
            new_state[empty_position_index + 3] = (0, 0)
            next_states_list.append(new_state)

        if items.__contains__('h'):
            new_state = self.state.copy()
            new_state[empty_position_index] = new_state[empty_position_index - 3]
            new_state[empty_position_index - 3] = (0, 0)
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
            node_to_add = Node(node_state)
            node_to_add.cost = self.cost + self.get_action_cost(node_to_add)
            nodes_list.append(node_to_add)

        return nodes_list

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

    def draw(self):  # Show representation of the node. You can just print something
        for x in range(3):
            print(f'{self.state[3*x]}, {self.state[3*x + 1]}, {self.state[3*x + 2]}')

    def get_method_name(self) -> str:
        pass
