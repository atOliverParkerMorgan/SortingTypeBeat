def bubbleSort(array, indexes):
    """
    :param array: sorted array
    :param indexes: list of all indexes that the algorithm is using
    :return: the sorted array by only one cycle,
             a new updated list of the indexes,
             a boolean that indicates weather or not the cycle is at its end
    """

    index = indexes[0]

    if len(array) <= index + 1:
        return array, [0], True

    if array[index] > array[index + 1]:
        array[index], array[index + 1] = array[index + 1], array[index]

    indexes[0] += 1

    return array, indexes, False


def selectSort(array, indexes):
    index = indexes[0]
    minimum = index

    if index >= len(array):
        indexes[0] = 0
        return array, indexes, True

    for i in range(minimum + 1, len(array)):
        if array[minimum] > array[i]:
            minimum = i

    array[index], array[minimum] = array[index], array[minimum]
    indexes[0] += 1

    return array, indexes, False


def insertionSort(array, indexes):
    index = indexes[0]

    if index >= len(array):
        indexes[0] = 0
        return array, indexes, True

    compared_index = index - 1

    while compared_index >= 0 and array[index] < array[compared_index]:
        array[index], array[compared_index] = array[compared_index], array[index]
        compared_index -= 1

    indexes[0] += 1

    return array, indexes, False


def quickSort(array, indexes):
    """
    Same as @bubbleSort, all sorting algorithms should follow the same input output pattern
    """

    def partition(array, low, high):
        pivot = array[high]
        i = low

        for j in range(low, high):
            if pivot >= array[j]:
                array[i], array[j] = array[j], array[i]
                i += 1

        array[i], array[high] = array[high], array[i]

        return i

    low, high = indexes[0], indexes[1]

    if low < high:
        pi = partition(array, low, high)

        indexes = [low, pi - 1, pi + 1, high]

        return array, indexes, False

    return array, [], True

