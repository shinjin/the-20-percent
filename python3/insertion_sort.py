

def insertion_sort(alist):
    """ An insertion sort implementation.

        Usage:

        alist = [37, 45, 44, 31, 60, 43, 56, 99, 66, 33]
        insertion_sort(alist)
        alist
        [31, 33, 37, 43, 44, 45, 56, 60, 66, 99]
    """

    for idx in range(1, len(alist)):
        pos = idx
        val = alist[idx]

        while pos > 0 and alist[pos - 1] > val:
            alist[pos] = alist[pos - 1]
            pos = pos - 1

        alist[pos] = val
