from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost)

        while True:
            if frontier.is_empty():
                return NoSolution(reached)

            node = frontier.pop()
            if grid.objective_test(node.state):
                return Solution(node, reached)

            for action in grid.actions(node.state):
                new_state = grid.result(node.state, action)
                new_costo = node.cost + grid.individual_cost(node.state,
                                                             action)
                if new_state not in reached.keys() or new_costo < reached[
                    new_state]:
                    new_node = Node("", state=new_state, cost=new_costo,
                                    parent=node, action=action)
                    reached[new_state] = new_costo
                    frontier.add(new_node, new_costo)

        return NoSolution(reached)
