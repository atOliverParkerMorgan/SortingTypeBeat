import math

import logic
import pygame

from audio import generateSound
from SortingAlgorithms import bubbleSort, quickSort, insertionSort
from graphics import displayArray

pygame.init()

info = pygame.display.Info()
width, height = info.current_w, info.current_h

screen = pygame.display.set_mode((width, height - 50))
# Set the FPS
clock = pygame.time.Clock()

FPS = 50
NUMBER_OF_ELEMENTS = 200

# bubbleSort selectSort insertSort quickSort mergeSort
SORTING_ALGORITHM = "quickSort"

if __name__ == '__main__':
    sorted_index = 0

    array = [i for i in range(1, NUMBER_OF_ELEMENTS + 1)]

    # display shuffle
    for _ in range(2*NUMBER_OF_ELEMENTS):
        array = logic.generateShuffledArray(array)
        displayArray(screen, array, width, height, [], -1)

    # indexes used in sorting algorithms
    sort_index_array = [0, len(array) - 1, 0, 0]

    is_finished = False
    show_animation = False

    generateSound(array)

    pygame.time.wait(500)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if sorted_index == len(array):
            continue

        if logic.isSorted(array) and is_finished or show_animation:
            if not show_animation:
                displayArray(screen, array, width, height, [], -1)
                FPS = len(array)

            show_animation = True
            displayArray(screen, array, width, height, [], sorted_index)
            sorted_index += math.ceil(len(array) / 100)

        elif SORTING_ALGORITHM == "bubbleSort":

            displayArray(screen, array, width, height, [sort_index_array[0], sort_index_array[0] + 1], -1)

            # run another cycle of the sorting algorithm
            array, sort_index_array, is_finished = bubbleSort(array, sort_index_array)

        elif SORTING_ALGORITHM == "selectSort":

            displayArray(screen, array, width, height, [sort_index_array[0]], -1)

            array, sort_index_array, is_finished = bubbleSort(array, sort_index_array)

        elif SORTING_ALGORITHM == "insertSort":

            displayArray(screen, array, width, height, [sort_index_array[0]], -1)

            array, sort_index_array, is_finished = insertionSort(array, sort_index_array)

        elif SORTING_ALGORITHM == "quickSort":
            displayArray(screen, array, width, height, sort_index_array[:4], -1)

            array, sort_index_array1, is_finished_1 = quickSort(array, [sort_index_array[0], sort_index_array[1]])
            array, sort_index_array2, is_finished_2 = quickSort(array, [sort_index_array[2], sort_index_array[3]])

            sort_index_array = sort_index_array[4:]
            sort_index_array += sort_index_array1 + sort_index_array2

            is_finished = is_finished_1 and is_finished_2

        elif SORTING_ALGORITHM == "mergeSort":
            # lol pass
            pass

        clock.tick(FPS)
