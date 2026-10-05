# sorting_algorithm.py
#
# Contains the merge sort implementation supplied as the baseline algorithm.
#
# An operation is counted each time two elements are compared during sorting.
# This definition is applied consistently across all algorithms in this experiment.
# Your implementations of bubble sort and insertion sort should count comparisons
# in the same way.
#
# Operation counts are returned as the second element of a tuple rather than
# modified in place, since Python does not support pass-by-reference for
# primitive values.
#
# To add a new algorithm, follow the same pattern as merge_sort below:
#   - Accept the array as a parameter
#   - Return a tuple of (sorted_array, operation_count)
#   - Increment operation_count each time two elements are compared


def merge_sort(array: list[int]) -> tuple[list[int], int]:
    """
    Sorts a list of integers using merge sort.
    Returns a tuple of (sorted list, operation count).
    The original list is not modified.
    """
    operation_count = 0
    result, operation_count = _merge_sort_recursive(array[:], operation_count)
    return result, operation_count


def _merge_sort_recursive(array: list[int], operation_count: int) -> tuple[list[int], int]:
    if len(array) <= 1:
        return array, operation_count

    mid = len(array) // 2
    left, operation_count = _merge_sort_recursive(array[:mid], operation_count)
    right, operation_count = _merge_sort_recursive(array[mid:], operation_count)

    merged, operation_count = _merge(left, right, operation_count)
    return merged, operation_count


def _merge(left: list[int], right: list[int], operation_count: int) -> tuple[list[int], int]:
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        # Each iteration performs one comparison between elements.
        operation_count += 1

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result, operation_count


# --- Add your algorithms below this line ---

def bubble_sort(array: list[int]) -> tuple[list[int], int]:
    arr = array[:] #New copy of the dataset
    operation_count = 0
    
    n = len(arr) #size of the array
    for i in range(n - 1): # keep looping through the array until the end is reached
        swapped = False # no items will be swapped within the first loop
        for j in range(n - i - 1): #loop through each comparable numbers left in the array
            operation_count += 1 # add 1 after each operation
            if arr[j] > arr[j + 1]: #if first comparable no is bigger than the on next to it
                arr[j], arr[j + 1] = arr[j+1], arr[j] # swap the numbers
                swapped = True #the numbers swapped
            if not swapped:
                break
    return arr, operation_count #return the sorted array and the number of operations (no of times the numbers were compared and swapped)

def insertion_sort(array: list[int]) -> tuple[list[int], int]:
    arr = array[:] #New copy of the dataset
    operation_count = 0

    n = len(arr) #size of the array
    for i in range(1,n): #keep looping the array from 1 -> n - 1 
        insert_index = i #the index we currently want to compare to the current value
        current_value = arr[i] #the current value we are comparing against
        for j in range(i - 1, -1, -1): #start at i - 1, step -1 and stop -1
            operation_count += 1 # add 1 after each operation

            if arr[j] > current_value: #if value one to the left is bigger then swap them
                arr[j + 1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_value

    return arr, operation_count #return the sorted array and the number of operations (no of times the numbers were compared and swapped)




















# Follow the same pattern as merge_sort above.
# Each algorithm should accept a list[int] and return tuple[list[int], int].
#
# Example structure (do not uncomment, implement your own):
#
# def bubble_sort(array: list[int]) -> tuple[list[int], int]:
#     arr = array[:]
#     operation_count = 0
#     # your implementation here
#     return arr, operation_count
#
# def insertion_sort(array: list[int]) -> tuple[list[int], int]:
#     arr = array[:]
#     operation_count = 0
#     # your implementation here
#     return arr, operation_count