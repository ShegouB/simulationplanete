import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulation de particules")

# Couleurs
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Classe pour représenter une particule
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = red
        self.speed_y = 0
    
    def apply_gravity(self):
        self.speed_y += 0.1
        self.y += self.speed_y
        
        if self.y > height - self.radius:
            self.y = height - self.radius
            self.speed_y = -self.speed_y * 0.8
    
    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radius)

# Création de particules
num_particles = 50
particles = [Particle(random.randint(0, width), random.randint(0, height)) for _ in range(num_particles)]

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(black)
    
    for particle in particles:
        particle.apply_gravity()
        particle.display()
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
