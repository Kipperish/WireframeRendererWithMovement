class Cube():
    def __init__(self):
        self.vertexMatrix = [[200, 200, 200],
                             [200, 200, -200],
                             [-200, 200, 200],
                             [-200, 200, -200],
                             [200, -200, 200],
                             [200, -200, -200],
                             [-200, -200, 200],
                             [-200, -200, -200]]
        self.edgeMatrix = [[0, 1],
                           [0, 2],
                           [0, 4],
                           [2, 3],
                           [2, 6],
                           [4, 5],
                           [4, 6],
                           [6, 7],
                           [1, 3],
                           [1, 5],
                           [7, 3],
                           [7, 5]]
        self.rotatedVertexMatrix = self.vertexMatrix
        self.movedVertexMatrix = self.vertexMatrix


class SquareBasedPyramid:
    def __init__(self):
        self.vertexMatrix = [[200, 200, -200],
                             [-200, 200, -200],
                             [200, 200, 200],
                             [-200, 200, 200],
                             [0, -200, 0]]
        self.edgeMatrix = [[4,0],
                           [4,1],
                           [4,2],
                           [4,3],
                           [0, 1],
                           [0, 2],
                           [3, 1],
                           [3, 2]]
        self.rotatedVertexMatrix = self.vertexMatrix
        self.movedVertexMatrix = self.vertexMatrix


class TriangleBasedPyramid:
    def __init__(self):
        self.vertexMatrix = [[0, 100, -200],
                             [173, 100, 100],
                             [-173, 100, 100],
                             [0, -173, 0]]
        self.edgeMatrix = [[3, 0],
                           [3, 1],
                           [3, 2],
                           [0, 1],
                           [0, 2],
                           [1, 2]]
        self.rotatedVertexMatrix = self.vertexMatrix
        self.movedVertexMatrix = self.vertexMatrix


class House():
    def __init__(self):
        self.vertexMatrix = [[100, 100, 100],
                             [100, 100, -100],
                             [-100, 100, 100],
                             [-100, 100, -100],
                             [100, -100, 100],
                             [100, -100, -100],
                             [-100, -100, 100],
                             [-100, -100, -100],
                             [0, -200, 0],
                             [-25, 100, -125],
                             [25, 100, -125],
                             [-25, 25, -125],
                             [25, 25, -125],
                             [-25, 100, -100],
                             [25, 100, -100],
                             [-25, 25, -100],
                             [25, 25, -100]]
        self.edgeMatrix = [[0, 1],
                           [0, 2],
                           [0, 4],
                           [2, 3],
                           [2, 6],
                           [4, 5],
                           [4, 6],
                           [6, 7],
                           [1, 3],
                           [1, 5],
                           [7, 3],
                           [7, 5],
                           [8,4],
                           [8,5],
                           [8,6],
                           [8,7],
                           [9, 10],
                           [9, 11],
                           [12, 10],
                           [12, 11],
                           [9, 13],
                           [10, 14],
                           [11, 15],
                           [12,16],
                           [13, 14],
                           [13, 15],
                           [16, 14],
                           [16, 15]]
        self.rotatedVertexMatrix = self.vertexMatrix
        self.movedVertexMatrix = self.vertexMatrix