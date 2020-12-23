import random


def partition_last(arr, low, high):
    # Choose the last elements as pivot
    i = low
    print("i >>>", i)
    pivot = arr[high]
    print("Pivot >>>", pivot)

    for j in range(low, high):
        if arr[j] < pivot:
            # swap
            # because the code will go from right to left when assigning value
            #   the value of arr[j] and arr[i] is stored and swap without being affected
            arr[i], arr[j] = arr[j], arr[i]

            i += 1
            # print("i >>>", i)
            print("Array after the swap >>>", arr)

    print("Array before this swapping >>>", arr)
    print("arr[i], arr[high]", arr[i], arr[high])
    arr[i], arr[high] = arr[high], arr[i]
    return i


def partition_first(arr, low, high):
    i = high
    pivot = arr[low]
    for j in range(low, high):
        if arr[j] < pivot:
            # swap
            # because the code will go from right to left when assigning value
            #   the value of arr[j] and arr[i] is stored and swap without being affected
            arr[i], arr[j] = arr[j], arr[i]

            i -= 1
            print("i >>>", i)
            print("Array after the swap >>>", arr)

    arr[i], arr[low] = arr[low], arr[i]
    return i


def quick_sort(arr, low, high):
    if low < high:
        pivot = partition_last(arr, low, high)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


if __name__ == '__main__':
    array = [random.randint(1, 20) for i in range(5)]
    print("Unsorted array >>>", array)
    n = len(array)
    quick_sort(array, 0, n - 1)
    print("Sorted array is:")
    print(array)
