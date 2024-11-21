import pygame
import random


def draw_grid(screen):
    """
    Draws a 20x16 grid of 32x32 squares on the screen.
    """
    for x in range(0, 640, 32):  # Vertical lines
        pygame.draw.line(screen, "black", (x, 0), (x, 512))
    for y in range(0, 512, 32):  # Horizontal lines
        pygame.draw.line(screen, "black", (0, y), (640, y))


def get_random_position():
    """
    Generates a random position for the mole within the grid.
    Each square is 32x32, so the position must align with the grid.
    """
    grid_x = random.randrange(0, 20) * 32  # Random column in the 20x16 grid
    grid_y = random.randrange(0, 16) * 32  # Random row in the 20x16 grid
    return grid_x, grid_y


def main():
    try:
        pygame.init()

        # Load the mole image
        mole_image = pygame.image.load("mole.png")

        # Initialize screen and clock
        screen = pygame.display.set_mode((640, 512))
        pygame.display.set_caption("Whack-A-Mole")
        clock = pygame.time.Clock()

        # Initial mole position (top-left corner)
        mole_x, mole_y = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Check if the mole is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Check if the mouse position is inside the mole's rectangle
                    if mole_x <= mouse_x < mole_x + 32 and mole_y <= mouse_y < mole_y + 32:
                        # Move mole to a new random position
                        mole_x, mole_y = get_random_position()

            # Clear the screen
            screen.fill("light green")

            # Draw the grid
            draw_grid(screen)

            # Draw the mole
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

            # Update the display
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
