'''
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = (l+r)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
'''


def merge_sort(arr):
    print("Array to merge sort >>>", arr)
    if len(arr) > 1:
        # finding the middle
        mid = len(arr) // 2

        # Divide the array into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting each half:
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        # merging data back into the old array
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # checking if any element was left:
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print("Array sorted: ", arr)


if __name__ == '__main__':
    array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("Given array is", end="\n")
    print(array)
    merge_sort(array)
    print("Sorted array is: ", end="\n")
    print(array)
