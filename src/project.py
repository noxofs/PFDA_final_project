import pygame


class Swatch():

    def __init__(self, color):
        self.color = color


def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((45, 45, 45))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()