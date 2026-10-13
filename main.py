import pygame
from math import pi, cos, sin
import datetime

WIDTH, HEIGHT = 960, 540
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = min(WIDTH, HEIGHT) * .5
hour_radius = clock_radius * .625
minute_radius = clock_radius * .85
second_radius = clock_radius *.85

number_size = int(clock_radius * .17)
number_offset = int(clock_radius * .25)
hour_size = int(clock_radius * 0.045)
minute_size = int(clock_radius * 0.03)
second_size = int(clock_radius * 0.013)

current_time = datetime.datetime.now()
second = current_time.second
minute = current_time.minute
hour = current_time.hour

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def numbers(number, size, position):
    font = pygame.font.SysFont("Arial", size, True, False)
    text = font.render(number, True, WHITE)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)

def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)

def init():
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, center, clock_radius - 10, 10)
    pygame.draw.circle(screen, WHITE, center, 12)

    for number in range(1, 13):
        numbers(str(number), number_size, polar_to_cartesian(clock_radius - number_offset, number * 30))

    for number in range(0, 360, 6):
        if number % 5:
            pygame.draw.line(screen, WHITE, polar_to_cartesian(clock_radius - 15, number),
                             polar_to_cartesian(clock_radius - 30, number), 2)
        else:
            pygame.draw.line(screen, WHITE, polar_to_cartesian(clock_radius - 15, number),
                             polar_to_cartesian(clock_radius - 35, number), 6)

    return


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        init()
        global second

        # Hour
        theta = (hour + minute / 60 + second / 3600) * (360 / 12)
        pygame.draw.line(screen, WHITE, center, polar_to_cartesian(hour_radius, theta), hour_size)

        # Minute
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, WHITE, center, polar_to_cartesian(minute_radius, theta), minute_size)

        # Second
        theta = second * (360 / 60)
        pygame.draw.line(screen, RED, center, polar_to_cartesian(second_radius, theta), second_size)

        pygame.display.update()

        ## update tick
        second += clock.tick(FPS) / 1000

    pygame.quit()


main()