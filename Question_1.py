# Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]


def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # Find the minimum element in the unsorted part of the array
        min_index = i

        # Traverse through the unsorted part of the array
        for j in range(i + 1, n):
            # Find a smaller element and update the minimum index
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    # Return the sorted array
    return arr

input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)
