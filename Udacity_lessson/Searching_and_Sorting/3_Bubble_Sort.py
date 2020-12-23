def bubble_sort(arr):
    for i in range(len(arr)):
        # iterate through the array
        # then swap the element
        for j in range(len(arr) - i - 1):
            # ignores the last part which is already sorted after each iteration
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        print("Array after {} iteration: {}".format(i, arr))


if __name__ == '__main__':
    array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    bubble_sort(array)
