

def merge_sort(alist):
    """ An merge sort implementation.

        Usage:

        alist = [78, 98, 47, 51, 92, 31, 97, 76, 69, 49]
        merge_sort(alist)
        alist
        [31, 47, 49, 51, 69, 76, 78, 92, 97, 98]
    """

    if len(alist)>1:
        mid = len(alist) // 2
        lhalf = alist[:mid]
        rhalf = alist[mid:]

        merge_sort(lhalf)
        merge_sort(rhalf)

        i, j, k = 0, 0, 0
 
        while i < len(lhalf) and j < len(rhalf):
            if lhalf[i] < rhalf[j]:
                alist[k]=lhalf[i]
                i = i + 1
            else:
                alist[k]=rhalf[j]
                j = j + 1

            k = k + 1

        while i < len(lhalf):
            alist[k]=lhalf[i]
            i = i + 1
            k = k + 1

        while j < len(rhalf):
            alist[k]=rhalf[j]
            j = j + 1
            k = k + 1
