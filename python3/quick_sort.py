

def partition(array, start, end):
    pivot = start

    for i in range(start + 1, end + 1):
        if array[i] <= array[start]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]

    array[pivot], array[start] = array[start], array[pivot]

    return pivot


def quick_sort(array, start=0, end=None):
    """ A quick sort implementation that sorts in place.

        Usage:

        alist = [78, 98, 47, 51, 92, 31, 97, 76, 69, 49]
        quick_sort(alist)
        alist
        [31, 47, 49, 51, 69, 76, 78, 92, 97, 98]
    """

    if end is None:
        end = len(array) - 1

    def _quicksort(array, start, end):
        if start >= end:
            return

        pivot = partition(array, start, end)
        _quicksort(array, start, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, start, end)
