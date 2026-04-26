import math
import pygame

# Window
WIDTH, HEIGHT = 800, 600
TARGET_FPS = 100      # ~10 ms per frame
BG_COLOR = (30, 30, 30)
FONT_COLOR = (180, 180, 180)

# Pivot
PIVOT_Y = HEIGHT // 2
PIVOT_SPEED = 300     # pixels per second
PIVOT_COLOR = (100, 200, 255)
PIVOT_RADIUS = 10

# Rod
ROD_LENGTH = 200      # pixels
ROD_COLOR = (210, 180, 140)
ROD_WIDTH = 6
# Angle convention: 0 = straight up, 90 = right, 180 = straight down (hanging)
ROD_ANGLE_DEG = 180.0


def main() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pendulum Simulator")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 18)

    px = float(WIDTH / 2)
    rod_angle = ROD_ANGLE_DEG
    t = 0.0

    running = True
    while running:
        dt = clock.tick(TARGET_FPS) / 1000.0
        t += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            px -= PIVOT_SPEED * dt
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            px += PIVOT_SPEED * dt
        px = max(PIVOT_RADIUS, min(WIDTH - PIVOT_RADIUS, px))

        a = math.radians(rod_angle)
        pivot = (px, PIVOT_Y)
        rod_end = (px + ROD_LENGTH * math.sin(a), PIVOT_Y - ROD_LENGTH * math.cos(a))

        screen.fill(BG_COLOR)
        pygame.draw.line(screen, ROD_COLOR, pivot, rod_end, ROD_WIDTH)
        pygame.draw.circle(screen, PIVOT_COLOR, (int(px), PIVOT_Y), PIVOT_RADIUS)

        ts = font.render(f"t = {t:.3f} s", True, FONT_COLOR)
        screen.blit(ts, (10, HEIGHT - ts.get_height() - 10))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
