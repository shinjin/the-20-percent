
from python3.quick_sort import quick_sort


def test_quick_sort():

    a = [1]
    quick_sort(a)
    assert a == [1]

    a = [2, 1, 3, 3, 1, 2, 2, 3, 1]
    quick_sort(a)
    assert a == [1, 1, 1, 2, 2, 2, 3, 3, 3]


    a = [78, 98, 47, 51, 92, 31, 97, 76, 69, 49]
    quick_sort(a)
    assert a == [31, 47, 49, 51, 69, 76, 78, 92, 97, 98]
