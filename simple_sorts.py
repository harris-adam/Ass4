# simple_sorts.py
# bubble sort, selection sort, insertion sort
# Strongly suggest you turn off LLMs like
# GitHub Copilot, TabNine, etc. when working on this file.
# Writing a sorting algorithm yourself is the best
# way to learn how it works.
# Modified by: Harris Adam
# Help from Classmate, Google, And Cs Tutor 

def bubble_sort(lst):
    """Sort lst in place. Repeatedly swap adjacent out-of-order items."""
    n = len(lst)
    for i in range(n - 1):
        swapped = False
        # After i passes, the last i items are already in their final place
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:  # no swaps means the list is already sorted
            break


def selection_sort(lst):
    """Sort lst in place. Select the smallest remaining item each pass."""
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]


def insertion_sort(lst):
    """Sort lst in place. Insert each item into the sorted prefix."""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        # Shift larger items right to open a slot for key
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
