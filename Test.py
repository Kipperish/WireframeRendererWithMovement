import pygame
import math
from pygame.locals import K_w, K_a, K_s, K_d, K_UP, K_DOWN, K_LEFT, K_RIGHT

# Utility functions for vector operations
def vector_add(v1, v2):
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_scale(v, scale):
    return [v[i] * scale for i in range(len(v))]

def cross_product(v1, v2):
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

# Camera class with yaw and pitch for full orientation control
class Camera:
    def __init__(self):
        self.position = [0, 0, -500]
        self.yaw = 0           # Horizontal rotation (yaw) in radians
        self.pitch = 0         # Vertical rotation (pitch) in radians
        self.rotation_speed = math.pi / 180
        self.movement_speed = 10

    def get_direction_vectors(self):
        # Calculate forward, right, and up vectors based on yaw and pitch
        forward = [
            math.cos(self.pitch) * math.sin(self.yaw),
            math.sin(self.pitch),
            math.cos(self.pitch) * math.cos(self.yaw)
        ]
        right = [
            math.cos(self.yaw),
            0,
            -math.sin(self.yaw)
        ]
        up = cross_product(right, forward)  # Up is the cross product of right and forward
        
        return forward, right, up

    def update(self):
        keys = pygame.key.get_pressed()
        
        # Get forward and right vectors for movement
        forward, right, _ = self.get_direction_vectors()
        
        # Movement in the direction of the camera's orientation
        if keys[K_w]:  # Move forward
            self.position = vector_add(self.position, vector_scale(forward, self.movement_speed))
        if keys[K_s]:  # Move backward
            self.position = vector_add(self.position, vector_scale(forward, -self.movement_speed))
        if keys[K_a]:  # Move left
            self.position = vector_add(self.position, vector_scale(right, -self.movement_speed))
        if keys[K_d]:  # Move right
            self.position = vector_add(self.position, vector_scale(right, self.movement_speed))
        
        # Adjust yaw and pitch based on key inputs
        if keys[K_RIGHT]:
            self.yaw += self.rotation_speed
        if keys[K_LEFT]:
            self.yaw -= self.rotation_speed
        if keys[K_UP]:
            self.pitch = max(-math.pi / 2, self.pitch + self.rotation_speed)
        if keys[K_DOWN]:
            self.pitch = min(math.pi / 2, self.pitch - self.rotation_speed)
        
        print(f"Camera position: {self.position}, yaw: {self.yaw}, pitch: {self.pitch}")

# Function to project 3D coordinates to 2D screen coordinates
def project_vertex(vertex, focal_length):
    x, y, z = vertex
    if z != 0:
        return [(focal_length * x) / z + 600, (focal_length * y) / z + 300]
    return [600, 300]  # Center if z is zero to avoid division error

# Check if a vertex is behind the camera
def is_behind_camera(vertex, camera):
    direction = camera.get_direction_vectors()[0]
    return sum(vertex[i] * direction[i] for i in range(3)) < 0

# Cube class representing a 3D model with vertices and edges
class Cube:
    def __init__(self):
        self.vertices = [
            [100, 100, 100],
            [100, 100, -100],
            [-100, 100, 100],
            [-100, 100, -100],
            [100, -100, 100],
            [100, -100, -100],
            [-100, -100, 100],
            [-100, -100, -100]
        ]
        self.edges = [
            (0, 1), (0, 2), (0, 4), (2, 3), (2, 6),
            (4, 5), (4, 6), (6, 7), (1, 3), (1, 5),
            (7, 3), (7, 5)
        ]

    def get_transformed_vertices(self, camera):
        transformed_vertices = []
        for vertex in self.vertices:
            # Translate by camera position
            translated_vertex = [
                vertex[0] - camera.position[0],
                vertex[1] - camera.position[1],
                vertex[2] - camera.position[2]
            ]
            # Rotate around yaw and pitch
            transformed_vertices.append(rotate_vertex(translated_vertex, camera.yaw, camera.pitch))
        return transformed_vertices

# Rotate a vertex by yaw and pitch
def rotate_vertex(vertex, yaw, pitch):
    x, y, z = vertex
    # Rotate around yaw (y-axis)
    xz = math.cos(yaw) * x - math.sin(yaw) * z
    z = math.sin(yaw) * x + math.cos(yaw) * z
    x = xz
    # Rotate around pitch (x-axis)
    yz = math.cos(pitch) * y - math.sin(pitch) * z
    z = math.sin(pitch) * y + math.cos(pitch) * z
    y = yz
    return [x, y, z]

# Render function to draw the cube edges based on transformed vertices
def render(screen, cube, camera, focal_length=500):
    transformed_vertices = cube.get_transformed_vertices(camera)
    for edge in cube.edges:
        # Check if either vertex is behind the camera
        if is_behind_camera(transformed_vertices[edge[0]], camera) and is_behind_camera(transformed_vertices[edge[1]], camera):
            continue  # Skip rendering if both vertices are behind the camera
        # Project each vertex of the edge to 2D
        v1 = project_vertex(transformed_vertices[edge[0]], focal_length)
        v2 = project_vertex(transformed_vertices[edge[1]], focal_length)
        # Draw line if vertices are partially on screen
        if (0 <= v1[0] <= 1200 and 0 <= v1[1] <= 600) or (0 <= v2[0] <= 1200 and 0 <= v2[1] <= 600):
            pygame.draw.line(screen, (255, 255, 255), v1, v2)

# Initialize pygame and run the main loop
pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("3D Render")
clock = pygame.time.Clock()
fps = 60

camera = Camera()
cube = Cube()

running = True
while running:
    screen.fill((0, 0, 0))
    camera.update()
    render(screen, cube, camera)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(fps)

pygame.quit()
