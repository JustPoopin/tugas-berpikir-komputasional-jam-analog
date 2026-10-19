# Jam Analog
# Simulasi jam analog

# KAMUS
import pygame
from math import pi, cos, sin
import datetime

WIDTH, HEIGHT = 960, 540
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = min(WIDTH, HEIGHT) * .5
hour_radius = clock_radius * .625
minute_radius = clock_radius * .85
second_radius = clock_radius *.85

bigline_size = 6
smallline_size = 2
number_size = int(clock_radius * .17)
number_offset = int(clock_radius * .25)
hour_size = int(clock_radius * 0.045)
minute_size = int(clock_radius * 0.03)
second_size = int(clock_radius * 0.013)

FPS = 60
clock_color = (255, 255, 255)
background_color = (0, 0, 0)
second_color = (255, 0, 0)
minute_color = (255, 255, 255)
hour_color = (255, 255, 255)
font = "Arial"

time_elapsed = 1
current_time = datetime.datetime.now()
second = current_time.second
minute = current_time.minute
hour = current_time.hour

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Analog Clock")
clock = pygame.time.Clock()


# ALGORITMA
def numbers(number, size, position):
    _font = pygame.font.SysFont(font, size, True, False)
    text = _font.render(number, True, clock_color)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)

def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)

def redraw():
    screen.fill(background_color)
    pygame.draw.circle(screen, clock_color, center, clock_radius - 10, 10)
    pygame.draw.circle(screen, clock_color, center, 12)

    for number in range(1, 13): # draw numbers
        numbers(str(number), number_size, polar_to_cartesian(clock_radius - number_offset, number * 30))

    for number in range(0, 360, 6): # draw lines on the edge
        if number % 5: # small line
            pygame.draw.line(screen, clock_color, polar_to_cartesian(clock_radius - 15, number),
                             polar_to_cartesian(clock_radius - 30, number), smallline_size)
        else: # big line
            pygame.draw.line(screen, clock_color, polar_to_cartesian(clock_radius - 15, number),
                             polar_to_cartesian(clock_radius - 35, number), bigline_size)

    return

def update(second):
    # Hour
    theta = (hour + minute / 60 + second / 3600) * (360 / 12)
    pygame.draw.line(screen, hour_color, center, polar_to_cartesian(hour_radius, theta), hour_size)

    # Minute
    theta = (minute + second / 60) * (360 / 60)
    pygame.draw.line(screen, minute_color, center, polar_to_cartesian(minute_radius, theta), minute_size)

    # Second
    theta = second * (360 / 60)
    pygame.draw.line(screen, second_color, center, polar_to_cartesian(second_radius, theta), second_size)

    pygame.display.update()


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        global time_elapsed
        if (time_elapsed) >= 1:
            global second
            print(second)

            # update second
            second += time_elapsed - (time_elapsed % 1) # ambil angka bulat saja
            second = second % 60 if second > 60 else second # kembali ke 0 jika melebihi 60
            time_elapsed = time_elapsed % 1 # tambahkan sisa dari modulo

            # update display
            redraw()
            update(second)

        time_elapsed += clock.tick(FPS)/1000

    pygame.quit()

main()
