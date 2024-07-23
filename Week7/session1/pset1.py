#July 23, 2024
#Unit7 Session1 version1
#Problem 1: Hello Hello

# def repeat_hello(n):
#   if n > 0:
#     print("Hello")
#     repeat_hello(n - 1)

# repeat_hello(5)

def repeat_hello_iterative(n):
  for i in range(n):
    print("Hello")

repeat_hello_iterative(5)

#Problem 2: Factorial Cases
def factorial(n):
  '''1) Base Case: If `n` is 0, return 1 (since 0! = 1).
  2) Recursive Case: Return `n * factorial(n - 1)`.'''
  #base case
  if n == 0 or n == 1:
    return 1
  #recursive call
  result = n * factorial(n - 1)
  return result

print(factorial(5))

#Problem 3: Recursive Sum
def sum_list(lst):
  '''1) Base Case: If the list is empty, return 0.
  2) Recursive Case: Return the first element of the list plus the result of a recursive call to `sum_list()` with the rest of the list.'''
  #base case
  if len(lst) == 0:
    return 0
  return lst[0] + sum_list(lst[1:])


lst = [1, 2, 3, 4, 5]
# print(sum_list(lst))

#Problem 4: Recursive Power of 2
def is_power_of_two(n):
  '''1) Base Case: If `n` is 1, return True because \(2^0 = 1\).
  2) If `n` is less than 1 or not divisible by 2, return False.
  3) Recursive Case: Recursively call the function with \(n/2\).'''
  print(n)
  if n == 1:
    return True

  if n % 2 != 0 or n < 1:  # Base case: if n is less than 1 or not divisible by 2, it's not a power of 2
    return False

  return is_power_of_two(n // 2)

print(is_power_of_two(6))
print(is_power_of_two(2))
print(is_power_of_two(16))

#Problem 5: Binary Search I
def binary_search(lst, target):
  # Initialize a left pointer to the 0th index in the list
  left = 0
  # Initialize a right pointer to the last index in the list
  right = len(lst) - 1

  # While left pointer is less than right pointer:
  while left <= right:
    # Find the middle index of the array
    mid = (right + left) // 2
    # If the value at the middle index is the target value:
    if lst[mid] == target:
      # Return the middle index
      return mid
    # Else if the value at the middle index is less than our target value:
    elif lst[mid] < target:
      # Update pointer(s) to only search right half of the list in next loop iteration
      left = mid + 1
    # Else
    else:
      # Update pointer(s) to only search left half of the list in next loop iteration
      right = mid - 1

  # If we search whole list and haven't found target value, return -1
  return -1

# Example Input: lst = [1, 3, 5, 7, 9, 11, 13, 15], target = 11
lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(lst, target))

#Problem 6: Backwards Binary Search
def find_last(lst, target):
  '''1) Initialize pointers for the left and right bounds of the list.
  2) Initialize a variable `last_occurrence` to store the index of the last found target.
  3) While the left pointer is not greater than the right:
     - Calculate the middle index.
     - If the middle element is the target, update `last_occurrence` and move the left pointer to continue searching on the right for possible later occurrences.
     - If the target is less than the middle element, adjust the right pointer to narrow the search to the left half.
     - If the target is greater than the middle element, adjust the left pointer to narrow the search to the right half.
  4) Return `last_occurrence` if found; otherwise, return -1.'''
  left = 0
  right = len(lst) - 1
  last_seen = - 1

  while left <= right:
    mid = (left + right) // 2

    if lst[mid] == target:
      last_seen = mid
      left = mid + 1   # Continue searching in the right half
    elif lst[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return last_seen


lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
target = 11
print(find_last(lst, target))


#Problem 7: Find Floor
'''1) Initialize pointers for the low and high bounds of the array.
2) Initialize a variable `floor_value` to None to track the highest value encountered that is <= x.
3) While the low pointer is not greater than the high:
   - Calculate the middle index.
   - If the middle element is less than or equal to x, update `floor_value` and shift the low pointer to the right to look for a possibly higher floor value.
   - If the middle element is greater than x, shift the high pointer to the left.
4) Return `floor_value`.'''
def find_floor(arr, x):
  low, high = 0, len(arr) - 1
  floor_value = None  # Initialize to None to handle the case where all elements are greater than x

  while low <= high:
      mid = (low + high) // 2

      if arr[mid] <= x:
          floor_value = arr[mid]  # arr[mid] could be a potential floor
          low = mid + 1  # Look for a larger element that might also be a floor
      else:
          high = mid - 1  # Search in the left half

  return floor_value