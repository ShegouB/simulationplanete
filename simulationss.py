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
WIDTH, HEIGHT = 1200, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation du Système Solaire")

# Définir les constantes
SUN_RADIUS = 30
AU = 149.6e6 * 1000  # Distance Astronomique en mètres
SCALE = 250 / AU  # 1 AU = 250 pixels
TIMESTEP = 3600 * 24  # 1 jour en secondes

# Classes pour les objets astronomiques
class Planet:
    def __init__(self, name, color, radius, mass, distance, velocity):
        self.name = name
        self.color = color
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = distance
        self.y = 0
        self.velocity_x = 0
        self.velocity_y = velocity
        self.orbit = []

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            dx = planet.x - self.x
            dy = planet.y - self.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            force = Planet.G * self.mass * planet.mass / distance ** 2
            theta = math.atan2(dy, dx)
            fx = math.cos(theta) * force
            fy = math.sin(theta) * force

            total_fx += fx
            total_fy += fy

        self.velocity_x += total_fx / self.mass * TIMESTEP
        self.velocity_y += total_fy / self.mass * TIMESTEP

        self.x += self.velocity_x * TIMESTEP
        self.y += self.velocity_y * TIMESTEP
        self.orbit.append((self.x, self.y))

    def draw(self, window):
        x = self.x * SCALE + WIDTH // 2
        y = self.y * SCALE + HEIGHT // 2

        pygame.draw.circle(window, self.color, (int(x), int(y)), self.radius)

        if len(self.orbit) > 2:
            updated_points = [(point[0] * SCALE + WIDTH // 2, point[1] * SCALE + HEIGHT // 2) for point in self.orbit]
            pygame.draw.lines(window, self.color, False, updated_points, 1)

    G = 6.67428e-11  # Constante gravitationnelle

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet("Sun", YELLOW, SUN_RADIUS, 1.98892 * 10 ** 30, 0, 0)
    mercury = Planet("Mercury", GRAY, 4, 3.30 * 10 ** 23, 0.387 * AU, 47.4 * 1000)
    venus = Planet("Venus", ORANGE, 6, 4.8685 * 10 ** 24, 0.723 * AU, 35.02 * 1000)
    earth = Planet("Earth", BLUE, 8, 5.9742 * 10 ** 24, 1 * AU, 29.78 * 1000)
    mars = Planet("Mars", RED, 5, 6.39 * 10 ** 23, 1.524 * AU, 24.077 * 1000)
    jupiter = Planet("Jupiter", LIGHT_GREEN, 15, 1.898 * 10 ** 27, 5.203 * AU, 13.07 * 1000)
    saturn = Planet("Saturn", LIGHT_BLUE, 12, 5.683 * 10 ** 26, 9.537 * AU, 9.69 * 1000)
    uranus = Planet("Uranus", DARK_BLUE, 10, 8.681 * 10 ** 25, 19.191 * AU, 6.81 * 1000)
    neptune = Planet("Neptune", WHITE, 10, 1.024 * 10 ** 26, 30.07 * AU, 5.43 * 1000)

    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    while run:
        clock.tick(60)
        WINDOW.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            if planet != sun:
                planet.update_position(planets)
            planet.draw(WINDOW)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
