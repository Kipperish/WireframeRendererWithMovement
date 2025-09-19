import pygame
import math
from Utility import matrixMultiply, arrayToVector, vectorToArray

focalLength = 1000

xRotation = 0
yRotation = 0
zRotation = 0

xRotationMatrix = [[1, 0, 0],
                   [0, math.cos(xRotation), -math.sin(xRotation)],
                   [0, math.sin(xRotation), math.cos(xRotation)]]

yRotationMatrix = [[math.cos(yRotation), 0, math.sin(yRotation)],
                   [0, 1, 0],
                   [-math.sin(yRotation), 0, math.cos(yRotation)]]

zRotationMatrix = [[math.cos(zRotation), -math.sin(zRotation), 0],
                   [math.sin(zRotation), math.cos(zRotation), 0],
                   [0, 0, 1]]

def projectVertex(vertex: list[int, int, int], focalLength: int) -> list[int, int]:
    x, y, z = vertex
    projectionX = (focalLength * x)//(focalLength + z)
    projectionY = (focalLength * y)//(focalLength + z)
    return([projectionX, projectionY])

def rotateVertex(vertex, rotationMatrix):
    return(vectorToArray(matrixMultiply(rotationMatrix, arrayToVector(vertex))))

def castModel(screen, colour, origin, vertexMatrix, edgeMatrix, focalLength):
    for edge in edgeMatrix:
        pygame.draw.line(screen, colour, [x + y for x,y in zip(origin, projectVertex(vertexMatrix[edge[0]], focalLength))], [x + y for x,y in zip(origin, projectVertex(vertexMatrix[edge[1]], focalLength))])

