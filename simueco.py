import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulation d'Écosystème")

# Couleurs
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Classe pour représenter les créatures
class Creature:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)

# Création des créatures
creatures = []
for _ in range(20):
    x = random.randint(0, width)
    y = random.randint(0, height)
    color = GREEN if random.random() < 0.7 else BROWN
    creatures.append(Creature(x, y, color))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des créatures
    for creature in creatures:
        creature.move()

    # Effacer l'écran
    screen.fill((0, 0, 0))

    # Dessiner les créatures
    for creature in creatures:
        creature.draw()

    # Rafraîchir l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
