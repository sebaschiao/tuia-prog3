from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...
        # 3 if (problema.test-objetivo(n₀.estado)) then return solución(n₀)
        if grid.objective_test(root.state):
            return Solution(root,reached)
        # frontera ← Cola()
        frontier = QueueFrontier()
        # frontera.encolar(n₀)
        frontier.add(root)

        while True:
        # if frontera.vacía() then return fallo
            if frontier.is_empty():
                return NoSolution(reached)
            # 9 n ← frontera.desencolar()
            node = frontier.remove()
            # forall a in problema.acciones(n.estado) do
            for action in grid.actions(node.state):
                #s’ ← problema.resultado(n.estado, a)
                new_state = grid.result(node.state, action)
                if new_state not in reached.keys():
                    new_node = Node("", state=new_state, cost = node.cost+grid.individual_cost(node.state,action), parent=node, action=action)
                    if grid.objective_test(new_state):
                        return Solution(new_node,reached)                    
                    reached[new_state] = True
                    frontier.add(new_node)
        