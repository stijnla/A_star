from Astar import Astar, Node
import numpy as np
from typing import Tuple

class Point():
    def __init__(self, coordinate: Tuple[float]) -> None:
        self._x, self._y = coordinate
        self.coordinate = coordinate


class dummy_graph():
    def __init__(self, points, edges) -> None:
        self.points = points

        self.edges = edges
    
    def get_neighbours(self, idx):
        idxs = np.where(self.edges[idx] != 0)[0].tolist()
        edges = [edge for edge in self.edges[idx] if edge != 0]
        coordinates = [self.points[idx].coordinate for idx in idxs]
        return idxs, edges, coordinates



def test_basic_path1():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 1, 1, 1],
                        [1, 0, 1, 1],
                        [1, 1, 0, 1],
                        [1, 1, 1, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="MANHATTEN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,3)]
    assert path[-1].g == 1

def test_basic_path2():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1],
                        [0, 0, 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,1),(0,2),(0,3)]
    assert path[-1].g == 3

def test_basic_path3():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 0, 1, 0],
                        [0, 0, 0, 1],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,2),(0,1),(0,3)]
    assert path[-1].g == 3

def test_basic_path4():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 0, 1, 0],
                        [1, 0, 0, 0],
                        [0, 1, 0, 1],
                        [0, 0, 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,1), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,1),(0,2),(0,3)]
    assert path[-1].g == 2

def test_basic_path5():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 0, 1, 0],
                        [1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,1), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    assert path == None


def test_basic_path6():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 0, 0, 0],
                        [1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,1), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    assert path == None


def test_basic_path7():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 8, 1, 10],
                        [0, 0, 2, 0],
                        [0, 0, 0, 1],
                        [0, 0, 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,2),(0,3)]
    assert path[-1].g == 2


def test_basic_path8():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 2, 2, 10],
                        [0, 0, 0, 2],
                        [0, 0, 0, 2],
                        [0, 0, 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,2),(0,3)]
    assert path[-1].g == 4


def test_basic_path9():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 1, 2, 10],
                        [0, 0, 0, 2],
                        [0, 0, 0, 2],
                        [0, 0, 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,1),(0,3)]
    assert path[-1].g == 3

def test_basic_path10():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 1, 2, 10],
                        [0, 0, 0, 2],
                        [0, 0, 0, 2],
                        [0, 0, 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,1),(0,3)]
    assert path[-1].g == 3


def test_basic_path11():
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 0.9, 2, 10],
                        [0, 0  , 0, 2],
                        [0, 0  , 0, 2.1],
                        [0, 0  , 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="MANHATTEN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,1),(0,3)]
    assert path[-1].g == 2.9


def test_basic_path12():
    # This one is interesting as it shows how the heuristic fails 
    # by being inconsistent (because the weights are weird), 
    # meaning that the heurstic does not properly represent the 
    # weights. The solution that A* gives is therefor SUBoptimal. 
    # Make sure that the heuristic is always consistent with the 
    # weights.
    #  A heuristic is not consistent if c(u,v) + h(v) >= h(u)
    points = [Point((0,0)),Point((0,1)),Point((0,2)),Point((0,3))]
    edges = np.array([  [0, 0.9, 2, 10],
                        [0, 0  , 0, 2],
                        [0, 0  , 0, 0.8],
                        [0, 0  , 0, 0]])
    g = dummy_graph(points, edges)
    a = Astar(g, (0,0), (0,3), heuristic_method="EUCLIDEAN")
    path = a.run()
    path_c = [node.coordinate for node in path]
    assert path_c == [(0,0),(0,1),(0,3)]
    assert path[-1].g == 2.9


def test_heuristic1():
    a = Astar(None, None, (1,1), heuristic_method="EUCLIDEAN")
    node = Node((0,0), None, None)
    assert a.heuristic(node, "EUCLIDEAN") == np.sqrt(2)


def test_heuristic2():
    a = Astar(None, None, (1,1), heuristic_method="MANHATTEN")
    node = Node((0,0), None, None)
    assert a.heuristic(node, "MANHATTEN") == 0