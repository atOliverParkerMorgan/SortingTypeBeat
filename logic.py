import random


def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def generateShuffledArray(array):

    random_index_1 = random.randint(0, len(array) - 1)
    random_index_2 = random.randint(0, len(array) - 1)

    array[random_index_1], array[random_index_2] = array[random_index_2], array[random_index_1]

    return array
