import pygame
from Renderer import *
from Shapes import *
from Camera import *
from Utility import addToElements
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("3D Render")
clock = pygame.time.Clock()
fps = 120

origin = [(1200//2), (600//2)]
shape = Cube()
camera = Camera()

running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        focalLength += 1
    if keys[K_DOWN]:
        focalLength -= 1

    camera.update()
    shape.movedVertexMatrix = addToElements(shape.vertexMatrix, [camera.x, camera.y, camera.z])
    shape.rotatedVertexMatrix = [rotateVertex(vertex, yRotationMatrix) for vertex in shape.movedVertexMatrix]

    xRotationMatrix = [[1, 0, 0],
                    [0, math.cos(xRotation), -math.sin(xRotation)],
                    [0, math.sin(xRotation), math.cos(xRotation)]]

    yRotationMatrix = [[math.cos(camera.horizontalRotation), 0, math.sin(camera.horizontalRotation)],
                    [0, 1, 0],
                    [-math.sin(camera.horizontalRotation), 0, math.cos(camera.horizontalRotation)]]

    zRotationMatrix = [[math.cos(zRotation), -math.sin(zRotation), 0],
                    [math.sin(zRotation), math.cos(zRotation), 0],
                    [0, 0, 1]]

    castModel(screen, (255,255,255), origin, shape.rotatedVertexMatrix, shape.edgeMatrix, focalLength)

    pygame.display.flip()