

def merge_sort(L):
    """ An merge sort implementation.

        Usage:

        alist = [78, 98, 47, 51, 92, 31, 97, 76, 69, 49]
        merge_sort(alist)
        alist
        [31, 47, 49, 51, 69, 76, 78, 92, 97, 98]
    """

    if len(L) > 1:
        mid = len(L) // 2
        left  = L[:mid]
        right = L[mid:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0
 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            L[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            L[k] = right[j]
            j += 1
            k += 1
