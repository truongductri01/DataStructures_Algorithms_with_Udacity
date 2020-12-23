"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    """Your code goes here."""
    # array in sorted order
    if value < input_array[0] or value > input_array[-1]:  # value is not in array
        return -1

    try:
        left = 0
        right = len(input_array) - 1
        mid = (left + right) // 2  # choose the middle if odd numbers, else choose the smaller one
        print("Middle >>>", mid, input_array[mid])
        while input_array[left] <= input_array[right]:
            if input_array[mid] == value:
                return mid
            elif input_array[mid] > value:
                right = mid - 1
                print("Right is changed >>>", right)
            else:
                left = mid + 1
                print("Left is changed >>>", left)

            mid = (left + right) // 2
            print("Middle >>>", mid)

        return -1
    except:
        print("Error happen")


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
