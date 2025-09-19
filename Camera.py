import pygame
import math
from pygame.locals import(
    K_w,
    K_a,
    K_s,
    K_d
)

class Camera():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.horizontalRotation = 0
        self.rotationSpeed = math.pi/180
        self.movementSpeed = 10

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.x -= (self.movementSpeed * math.sin(self.horizontalRotation))
            self.z -= (self.movementSpeed * math.cos(self.horizontalRotation))
        if keys[K_s]:
            self.x += (self.movementSpeed * math.sin(self.horizontalRotation))
            self.z += (self.movementSpeed * math.cos(self.horizontalRotation))
        if keys[K_a]:
            self.horizontalRotation += self.rotationSpeed
        if keys[K_d]:
            self.horizontalRotation -= self.rotationSpeed

    def update(self):
        self.move()
        print(self.x, self.z)