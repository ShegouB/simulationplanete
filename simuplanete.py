import pygame
import math

# Initialisation de Pygame
pygame.init()

# Définir les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
DARK_BLUE = (0, 0, 139)

# Définir les dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation du Système Solaire")

# Définir les constantes
SUN_RADIUS = 30
PLANET_RADIUS = {
    "Mercure": 4,
    "Vénus": 6,
    "Terre": 8,
    "Mars": 5,
    "Jupiter": 15,
    "Saturne": 12,
    "Uranus": 10,
    "Neptune": 10
}
PLANET_COLOR = {
    "Mercure": GRAY,
    "Vénus": ORANGE,
    "Terre": BLUE,
    "Mars": RED,
    "Jupiter": LIGHT_GREEN,
    "Saturne": LIGHT_BLUE,
    "Uranus": DARK_BLUE,
    "Neptune": WHITE
}
ORBIT_RADIUS = {
    "Mercure": 50,
    "Vénus": 70,
    "Terre": 100,
    "Mars": 150,
    "Jupiter": 200,
    "Saturne": 250,
    "Uranus": 300,
    "Neptune": 350
}
ORBIT_SPEED = {
    "Mercure": 0.04,
    "Vénus": 0.03,
    "Terre": 0.02,
    "Mars": 0.015,
    "Jupiter": 0.01,
    "Saturne": 0.007,
    "Uranus": 0.005,
    "Neptune": 0.003
}

# Fonction pour dessiner le système solaire
def draw_solar_system(angles):
    WINDOW.fill(BLACK)

    # Dessiner le soleil
    pygame.draw.circle(WINDOW, YELLOW, (WIDTH // 2, HEIGHT // 2), SUN_RADIUS)

    # Dessiner les planètes
    for planet, radius in ORBIT_RADIUS.items():
        x = WIDTH // 2 + radius * math.cos(angles[planet])
        y = HEIGHT // 2 + radius * math.sin(angles[planet])
        pygame.draw.circle(WINDOW, PLANET_COLOR[planet], (int(x), int(y)), PLANET_RADIUS[planet])

    pygame.display.update()

# Main loop
def main():
    clock = pygame.time.Clock()
    angles = {planet: 0 for planet in ORBIT_RADIUS}

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mettre à jour les angles des planètes
        for planet in angles:
            angles[planet] += ORBIT_SPEED[planet]

        # Dessiner le système solaire
        draw_solar_system(angles)

    pygame.quit()

if __name__ == "__main__":
    main()
