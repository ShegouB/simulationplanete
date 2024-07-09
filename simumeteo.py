import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
screen_width = 600
screen_height = 400

# Couleurs
white = (255, 255, 255)
gray = (128, 128, 128)
yellow = (255, 255, 0)

# Classe pour représenter un nuage
class Cloud:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, screen_width - 100), random.randint(0, screen_height - 100), 100, 60)
        self.speed_x = random.randint(1, 3)
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left > screen_width:
            self.rect.right = 0
        if self.rect.top > screen_height:
            self.rect.bottom = 0

    def draw(self, screen):
        pygame.draw.ellipse(screen, gray, self.rect)

# Classe pour représenter une goutte de pluie
class Raindrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = random.randint(5, 20)
        self.speed = random.randint(5, 10)

    def update(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.length), 1)

# Classe pour représenter un éclair
class Lightning:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, screen_width - 50), random.randint(0, 100), 50, 150)
        self.timer = 0

    def show(self, screen):
        if self.timer < 10:
            pygame.draw.rect(screen, yellow, self.rect)

    def update(self):
        self.timer += 1

# Initialisation de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Système météorologique interactif")

# Création des objets météorologiques
clouds = [Cloud() for _ in range(5)]
raindrops = []
lightning = Lightning()

# Boucle principale du jeu
running = True
clock = pygame.time.Clock()

while running:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des objets météorologiques
    for cloud in clouds:
        cloud.update()

    for drop in raindrops:
        drop.update()

    lightning.update()

    # Génération de nouvelles gouttes de pluie
    if random.randint(0, 10) < 3:
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        raindrops.append(Raindrop(x, y))

    # Effacer l'écran
    screen.fill((0, 0, 0))

    # Dessiner les objets météorologiques
    for cloud in clouds:
        cloud.draw(screen)

    for drop in raindrops:
        drop.draw(screen)

    lightning.show(screen)

    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(60)

# Fermeture de Pygame
pygame.quit()
