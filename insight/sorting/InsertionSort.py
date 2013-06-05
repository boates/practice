


def insertion_sort(array):

    N = len(array)

    for i in range(1, N):
        x = array[i]
        j = i-1
        while j >= 0 and array[j] > x:
            array[j], array[j+1] = array[j+1], array[j]
            j += -1

    return array


def main():


    array = [7, 1, 22, 14, 7, 7, 3, 0, -8]
    print array
    print insertion_sort(array)


if __name__ == "__main__":
    main()
