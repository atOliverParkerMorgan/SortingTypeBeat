import math

import pygame

from audio import playSound

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 150, 175)
GREEN = (100, 250, 40)


def displayArray(screen, array, width, height, selected_index_arr, sorted_index):

    WIDTH = math.ceil(width / len(array))
    SIZE = len(array)

    if sorted_index == -1:
        screen.fill(BLACK)
    else:
        array_copy = array
        array = []

        for i in range(math.ceil(SIZE / 100)):
            if not sorted_index+i >= SIZE:
                array.append(array_copy[sorted_index+i])

    for i, element in enumerate(array):
        if sorted_index != -1:
            i = element - 1

        rect = pygame.Rect(i * WIDTH, int((height * 0.75) / SIZE * (SIZE + 1 - element)), WIDTH,
                           height)

        if sorted_index > -1:
            print(element)
            pygame.draw.rect(screen, GREEN, rect)
            playSound(element-1)

        elif i in selected_index_arr:
            pygame.draw.rect(screen, PINK, rect)
            playSound(element-1)
        else:
            pygame.draw.rect(screen, WHITE, rect)

    pygame.display.update()
