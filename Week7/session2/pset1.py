#Problem 1: Neatly Nested
'''1) If the string is empty, return True (base case).
2) If the string starts with '(' and ends with ')', recursively validate the substring between them.
3) Otherwise, return False.'''
def is_nested_parens(s):
    if s == "":
        return True
    if len(s) >= 2 and s[0] == '(' and s[-1] == ')':
        return is_nested_parens(s[1:-1])
    return False

#Problem 2: How Many 1s
'''1) If the last element of the array is 0, return 0.
2) Use binary search to find the first occurrence of 1.
3) If 1 is found, subtract its index from the length of the array to get the count of 1's.
4) If no 1 is found during the search, return 0.'''
def count_ones(lst):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == 0:
            low = mid + 1
        else:
            high = mid - 1

    # Check if low is within the array bounds and points to a 1
    if low < len(lst) and lst[low] == 1:
        return len(lst) - low
    return 0

#Problem 3: Binary Search IV
'''1) Base Case: If the range is exhausted without finding the target, return -1.
2) Calculate the middle index of the current search range.
3) If the middle element is the target, return its index.
4) If the target is less than the middle element, recursively search the left half.
5) If the target is greater than the middle element, recursively search the right half.'''
def binary_search(nums, left, right, target):
    if left > right:
        return -1  # Target is not found

    mid = (left + right) // 2

    # Found the target, return its index.
    if nums[mid] == target:
        return mid

    # Decide to search left or right half.
    if target < nums[mid]:
        return binary_search(nums, left, mid - 1, target)
    else:
        return binary_search(nums, mid + 1, right, target)

def binary_search_recursive(nums, target):
    # Initial call to the external binary search function
    return binary_search(nums, 0, len(nums) - 1, target)

#Problem 4: Count Rotations
'''1) Establish pointers for the beginning (`low`) and end (`high`) of the array.
2) If the element at `low` is less than or equal to the element at `high`, the array is not rotated.
3) Use a loop to continue searching as long as `low` is less than `high`:
   - Calculate the middle index (`mid`).
   - Check the relationship between `mid`, `low`, and `high` to determine the unsorted part:
     - If the element at `mid` is greater than the element at `high`, the rotation is in the right half, set `low` to `mid + 1`.
     - Otherwise, set `high` to `mid`.
4) At the end of the loop, `low` will point to the smallest element, which is the number of rotations.'''
def count_rotations(nums):
    low, high = 0, len(nums) - 1
    while low <= high:
        if nums[low] <= nums[high]:  # Array is sorted, no rotation
            return low
        mid = (low + high) // 2
        next_index = (mid + 1) % len(nums)  # circular indexing
        prev_index = (mid - 1 + len(nums)) % len(nums)  # circular indexing

        # Check if the mid element is the minimum element
        if nums[mid] <= nums[next_index] and nums[mid] <= nums[prev_index]:
            return mid
        elif nums[mid] > nums[high]:
            low = mid + 1  # Min must be in the right unsorted portion
        else:
            high = mid - 1  # Min must be in the left unsorted portion

    return 0  # This return is technically unreachable due to the logic

#Problem 5: Merge Sort I
'''1) If the list length is 0 or 1, it is already sorted, so return it.
2) Split the list into two halves.
3) Recursively apply merge sort to both halves.
4) Merge the two sorted halves into a single sorted list using the merge function.
5) Return the merged and sorted list.'''
def merge_sort(lst):
    if len(lst) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursive calls to merge_sort for sorting the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = [] 
    i = j = 0  
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

#Problem 6: Circle Search
'''1) Start with pointers at the beginning (`low`) and end (`high`) of the array.
2) While `low` is less than or equal to `high`:
   - Calculate the middle index (`mid`).
   - Check if `mid` is the target. If so, return `mid`.
   - Determine which half of the array is properly sorted:
     - If the left half is sorted (i.e., `arr[low] <= arr[mid]`):
       - If the target lies within this sorted half, adjust `high`.
       - Otherwise, adjust `low`.
     - If the right half is sorted:
       - If the target lies within this sorted half, adjust `low`.
       - Otherwise, adjust `high`.
3) If the loop concludes without finding the target, return -1.'''
def search_in_rotated_array(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:  # Left half is sorted
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1  # Target not found