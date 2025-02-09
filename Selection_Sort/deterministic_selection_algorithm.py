# ----------------------------------------------------------------------------------------------------------------------
# Deterministic Selection Algorithm
# Author: Unique Karanjit
# Date: 2025-02-08
# ----------------------------------------------------------------------------------------------------------------------

def median_of_medians(arr, k):
    """
    Deterministic Median of Medians Algorithm to find the k-th smallest element in an array.
    
    Parameters:
    arr (list): List of unsorted elements.
    k (int): The k-th smallest element to find (1-based index).

    Returns:
    int: The k-th smallest element in the array.
    
    Complexity:
    - Worst Case: O(n) (guaranteed linear time)
    """

    if len(arr) <= 5:
        return sorted(arr)[k - 1]  # Directly sort and return k-th smallest for small lists

    # Divide into groups of 5 and find medians
    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # Find the median of medians recursively
    pivot = median_of_medians(medians, len(medians) // 2 + 1)

    # Partitioning based on the pivot
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k <= len(left):
        return median_of_medians(left, k)
    elif k <= len(left) + len(mid):
        return pivot  # The pivot is the k-th element
    else:
        return median_of_medians(right, k - len(left) - len(mid))

if __name__ == "__main__":
    test_cases = [
        ([12, 3, 5, 7, 19, 26, 15, 8, 23, 17], 4),  # Expected: 8
        ([4, 2, 2, 2, 5, 1, 6, 7, 8, 2], 5),        # Expected: 2 (handles duplicates)
        ([10], 1),                                  # Single element case: Expected 10
        ([1, 2, 3, 4, 5], 5),                       # Last element case: Expected 5
    ]

    for arr, k in test_cases:
        print(f"Median of Medians result for k={k}: {median_of_medians(arr.copy(), k)}")
