from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __repr__(self):
        return "Position({},{})".format(self.x, self.y)

class Node(object):
    def __init__(self, position, passable=True):
        self.position = position
        self.passable = passable

    def __repr__(self):
        return "Node(x={},y={})".format(self.position.x, self.position.y)


def print_grid(grid, start_node=None, end_node=None, path=None):
    if not grid:
        return ''

    grid_string_list = []
    width = len(grid)
    height = len(grid[0])
    for y in range(0, height):
        grid_string = ""
        for x in range(0, width):
            node = grid[x][y]
            if start_node and node is start_node:
                grid_string += 'S'
            elif end_node and node is end_node:
                grid_string += 'E'
            else:
                grid_string += '0' if node.passable else '1'
        grid_string_list.append(grid_string)

    if path:
        path_index = 0
        for node in path:
            grid_string = grid_string_list[node.position.y]
            grid_string_list[node.position.y] = grid_string[:node.position.x] + '#' + grid_string[node.position.x + 1:]
            path_index += 1
    return_string = "\n".join(grid_string_list)
    print(return_string)
    return return_string