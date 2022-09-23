# Numpy is only used in the heuristic, otherwise it is not necessary
import numpy as np

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, coordinate, parent=None, idx=None):
        self.parent = parent
        
        # TODO: Based on a graph, this line below should be changed/deleted to your application accordingly 
        self.idx = idx


        self.coordinate = coordinate
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.coordinate == other.coordinate




class Astar():
    
    
    def __init__(self, graph, start, end, heuristic_method, debug=False) -> None:
        
        """Returns a list of tuples as a path from the given start to the given end in the given graph"""
        self.graph = graph
        # Create start and end node
        self.start_node = Node(start, None, 0)
        self.start_node.g = self.start_node.h = self.start_node.f = 0
        self.end_node = Node(end, None, -1)
        self.end_node.g = self.end_node.h = self.end_node.f = 0

        self.method = heuristic_method
        self.debug = debug

    
    
    
    
    def heuristic(self, node, method) -> float:
        # Euclidian distance between current point and goal node
        x, y = node.coordinate
        if method == "EUCLIDEAN":
            return np.sqrt((x - self.end_node.coordinate[0])**2 + (y - self.end_node.coordinate[1])**2)
        if method == "MANHATTEN":
            return 0


    
    
    
    
    def run(self):
        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(self.start_node)

        # Iterator to count loops, cancel search if limit is exceeded
        it = 0
        limit = 1000

        # Loop until you find the end
        while len(open_list) > 0:
            it = it + 1

            if it > limit:
                print("Iteration limit reached, path not found")
                break

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            if self.debug:
                print("Evaluating node: " + str(current_node.idx))
                print("Closed_list contains: " + str([node.idx for node in closed_list]))
                


            # Found the goal
            if current_node == self.end_node:
                print("Path found!")
                path = []
                current = current_node
                while current is not None:
                    path.append(current)
                    current = current.parent
                return path[::-1] # Return reversed path

            
            
            # Get neighbours
            # TODO: Based on a graph, this line should be changed to your application accordingly.
            #       The costs parent_to_child and start_to_parent should be generated and given 
            #       here.
            neighbours, costs_parent_to_neighbour, coordinates = self.graph.get_neighbours(current_node.idx)

            
            # Generate children
            children = []
            for i, neighbour in enumerate(neighbours):
                # Create new node
                

                # TODO: line below should be changed based on the node
                new_node = Node(coordinates[i], current_node, neighbour)
                
                
                # Append
                children.append(new_node)
            
            if self.debug:
                print("Node " + str(current_node.idx) + " has " + str(len(children)) + "child/children")
                print("Evaluating children...")
                print()
            # Loop through children
            for i, child in enumerate(children):
                already_seen = False
                
                
                if self.debug:
                    print("Evaluating child: " + str(child.idx))


                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        already_seen = True

                # Create the f, g, and h values

                # TODO: The two lines below can be changed according to your application.
                #       The cost to get to child 'g' should come from some sort of graph.
                #       The current heuristic is based on the EUCL DIST from child to goal.
                child.g = current_node.g + costs_parent_to_neighbour[i]
                child.h = self.heuristic(child, self.method)
                
                
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        already_seen = True

                # Add the child to the open list
                
                if not already_seen:
                    if self.debug:
                        print("Child is not seen yet. Appending child to open list")

                    open_list.append(child)
                
                if self.debug:
                    print()
                    print("Open_list contains: " + str([node.idx for node in open_list]))
                    print()
            if open_list == []:
                print("Path not possible, exiting...")
    
        

