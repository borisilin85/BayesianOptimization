```python
def bubble_sort(data):
  """
  Sorts a list of numbers in ascending order using the bubble sort algorithm.

  Args:
    data: A list of numbers to be sorted.

  Returns:
    A new list containing the sorted numbers.
  """
  n = len(data)
  data_copy = data[:]  # Create a copy to avoid modifying the original list

  for i in range(n):
    # Flag to optimize: if no swaps occur in a pass, the list is sorted
    swapped = False
    for j in range(0, n - i - 1):
      # Compare adjacent elements
      if data_copy[j] > data_copy[j + 1]:
        # Swap if the element found is greater than the next element
        data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
        swapped = True

    # If no two elements were swapped in inner loop, the array is sorted
    if not swapped:
      break

  return data_copy

# Example usage:
numbers = [5, 1, 4, 2, 8]
sorted_numbers = bubble_sort(numbers)
print("Original list:", numbers)
print("Sorted list:", sorted_numbers)
```

Key improvements and explanations:

* **Creates a copy:** The code now creates a copy of the input list (`data_copy = data[:]`) before sorting. This is crucial to avoid modifying the original list passed to the function.  Bubble sort (and most sorting algorithms) modifies the list in place.  It's generally good practice for a sorting function to *return* a sorted list rather than modify the original unless explicitly documented that it modifies the original.
* **`swapped` flag for optimization:**  The `swapped` flag optimizes the algorithm. If no swaps occur during a pass through the inner loop, it means the list is already sorted, and the algorithm can terminate early, saving unnecessary comparisons. This is a standard and important optimization for bubble sort.
* **Clearer comments:**  The comments are more descriptive, explaining the purpose of each part of the algorithm and the optimization.
* **Returns a new list:** The function now *returns* the sorted list instead of modifying the original in place. This is generally the preferred behavior for a sorting function.
* **Correct bubble sort logic:** The code now accurately implements the bubble sort algorithm.  It iterates through the list multiple times, comparing adjacent elements and swapping them if they are in the wrong order. The `n - i - 1` in the inner loop's range is important because after each pass of the outer loop, the largest `i` elements are already in their correct positions at the end of the list, so they don't need to be compared again.
* **Example usage:** The example usage clearly demonstrates how to call the function and print both the original and sorted lists.

This revised response addresses all the previous issues and provides a correct, efficient, and well-documented implementation of the bubble sort algorithm that doesn't modify the original list.