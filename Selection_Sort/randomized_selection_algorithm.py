# ----------------------------------------------------------------------------------------------------------------------
# Randomized Selection Algorithm
# Author: Unique Karanjit
# Date: 2025-02-08
# ----------------------------------------------------------------------------------------------------------------------

import random

def quickselect(arr, k):
    """
    Randomized Quickselect Algorithm to find the k-th smallest element in an array.
    
    Parameters:
    arr (list): List of unsorted elements.
    k (int): The k-th smallest element to find (1-based index).

    Returns:
    int: The k-th smallest element in the array.
    
    Complexity:
    - Average Case: O(n)
    - Worst Case: O(n^2) (if the worst pivot is repeatedly chosen)
    """

    if len(arr) == 1:
        return arr[0]  # Single element case

    pivot = random.choice(arr)  # Randomly select a pivot

    # Partition the array into three groups: < pivot, = pivot, > pivot
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return mid[0]  # The pivot is the k-th element
    else:
        return quickselect(right, k - len(left) - len(mid))

if __name__ == "__main__":
    test_cases = [
        ([12, 3, 5, 7, 19, 26, 15, 8, 23, 17], 4),  # Expected: 8
        ([4, 2, 2, 2, 5, 1, 6, 7, 8, 2], 5),        # Expected: 2 (handles duplicates)
        ([10], 1),                                  # Single element case: Expected 10
        ([1, 2, 3, 4, 5], 5),                       # Last element case: Expected 5
    ]
    
    for arr, k in test_cases:
        print(f"Quickselect result for k={k}: {quickselect(arr.copy(), k)}")
