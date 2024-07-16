#Problem 1: Long Pressed
#name = aleex
#typed = "aaleex"
def is_long_pressed(name, typed):
  i = 0
  j = 0

  while i < len(name) and j < len(typed):
    if name[i] == typed[j]: #or name[i] == typed[j+1]:
      i += 1
      j += 1
    elif j > 0 and typed[j] == typed[j-1]:
      j += 1
    else:
      return False

  return True

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

#Problem 2: Sharing Cookies
def find_content_children(g, s):
  i = 0
  j = 0
  count = 0

  while i < len(g) and j < len(s):
    if s[j] >= g[i]:
      count +=1
      i +=1
      j += 1
    else:
      i +=1
      j += 1
  return count

g = [1,2,3]
s = [1,1,3]


# There are 3 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 1 --> content child

# child `1` has a greed factor of 2
# cookie `1` has a size of 1, this child will not be content

# child `2` has a greed factor of 3
# cookie `2` has a size of 3 --> content child

#print(find_content_children(g, s))
# Output: 2 

g = [1,1]
s = [2,2,2]
# There are 2 children and 3 cookies
# child `0` has a greed factor of 1
# cookie `0` has a size of 2 --> content child

# child `1` has a greed factor of 1
# cookie `1` has a size of 1 --> content child

print(find_content_children(g, s))
# Output: 2 

#Problem 3: Valid Palindrome
def is_palindrome(s, left, right):
  while left < right:
      if s[left] != s[right]:
          return False
      left, right = left + 1, right - 1
  return True

def valid_palindrome(s):
  left, right = 0, len(s) - 1

  while left < right:
      # When characters mismatch, check the two possibilities
      if s[left] != s[right]:
          # Check by skipping left character or skipping right character
          return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
      left, right = left + 1, right - 1

  # If it's already a palindrome or can be one by removing a character
  return True

#Problem 4: Positive Negative Pairs
'''1) Sort the list of integers.
2) Initialize two pointers at the beginning and end of the sorted list.
3) Initialize a variable to keep track of the largest valid k found, start with -1.
4) While the left pointer is less than the right pointer:
  a) Calculate the sum of the values at the two pointers.
  b) If the sum is less than 0, move the left pointer right to find a less negative number.
  c) If the sum is more than 0, move the right pointer left to find a smaller positive number.
  d) If the sum is 0, update the largest k if the current k (value at the right pointer) is greater than the current largest k.
     Then move both pointers to continue searching.
5) Return the largest k found or -1 if no such pair exists.'''
def findLargestK(nums):
  nums.sort()  # Step 1
  left, right = 0, len(nums) - 1
  largestK = -1  # Initialize largestK with -1

  while left < right:  # Ensure we do not cross pointers
      sum = nums[left] + nums[right]

      if sum < 0:  # The negative number is too small (too negative)
          left += 1
      elif sum > 0:  # The positive number is too large
          right -= 1
      else:  # Found a pair
          largestK = nums[right]  # Update largestK
          left += 1
          right -= 1

  return largestK

#Problem 5: Good Substring
'''1) Initialize a counter for good substrings to 0.
2) Loop through the string until there are less than three characters left to form a substring.
3) For each position, extract a substring of three characters.
4) Convert the substring into a set to remove duplicates and check its length.
5) If the length of the set is 3, increment the counter for good substrings.
6) Return the total count of good substrings found.'''
def count_good_substrings(s):
  # Initialize the count of good substrings
  count = 0
  # Loop through the string, stopping when less than 3 characters remain
  for i in range(len(s) - 2):
      # Extract the current window of size 3
      window = s[i:i+3]
      # Check if all characters in the window are unique
      if len(window) == len(set(window)):
          count += 1
  return count

#Problem 6: Duplicates Within Range
'''1) Create a dictionary to store each element's last seen index.
2) Iterate through the list:
  a) If the element is already in the dictionary and the difference between the current index and the last seen index is less than or equal to k, return True.
  b) Update the dictionary with the current index for the element.
3) If the loop completes without finding any nearby duplicates, return False.'''
def contains_nearby_duplicate(lst, k):
  # Dictionary to store the elements and their last seen indices
  element_indices = {}
  # Loop through the array
  for i, element in enumerate(lst):
      # Check if the element is in the dictionary and within the k distance
      if element in element_indices and i - element_indices[element] <= k:
          return True
      # Update the dictionary with the current index of the element
      element_indices[element] = i
  return False