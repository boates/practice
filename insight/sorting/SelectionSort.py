

def selection_sort(array):
    """
    Brian's Selection Sort
    """
    N = len(array)

    for i in range(N):
        k = i
        m = array[i]
        for j in range(i, N):
            if array[j] < m:
                m = array[j]
                k = j
        array[i], array[k] = array[k], array[i]

    return array


def main():
    
    array = [10, 8, 14, 3, 6, 3, 14]
    print "Starting Array: ", array
    print selection_sort(array)


if __name__ == "__main__":
    main()
