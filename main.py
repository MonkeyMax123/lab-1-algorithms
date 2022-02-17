import tabulate
import time


def linear_search(mylist, key):
    for i, v in enumerate(mylist):
        if v == key:
            return i
    return -1


def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 5) == 4
    assert linear_search([1, 2, 3, 4, 5], 1) == 0
    assert linear_search([1, 2, 3, 4, 5], 6) == -1


def binary_search(mylist, key):
    return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
    mid = int(((left + right) / 2))
    if key == mylist[mid]:
        return mid
    elif left >= right:
        return -1
    elif key > mylist[mid]:
        return _binary_search(mylist, key, mid + 1, right)
    elif key < mylist[mid]:
        return _binary_search(mylist, key, left, mid - 1)


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], -1) == -1


def time_search(search_fn, mylist, key):
    time_start = time.time()
    search_fn(mylist, key)
    time.sleep(.001)
    time_end = time.time()
    time_total = (time_end - time_start - .001) * 1000
    return time_total


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
    search_times = []

    for i in range(len(sizes)):
        sample = range(1, int(sizes[i]))
        search_times.append(
            (int(sizes[i]), time_search(linear_search, sample, -1), time_search(binary_search, sample, -1)))

    return search_times


def print_results(results):
    print(tabulate.tabulate(results,
                            headers=['n', 'linear', 'binary'],
                            floatfmt=".3f",
                            tablefmt="github"))


def test_compare_search():
    res = compare_search(sizes=[10, 100])
    print(res)
    assert res[0][0] == 10
    assert res[1][0] == 100
    assert res[0][1] < 1
    assert res[1][1] < 1
