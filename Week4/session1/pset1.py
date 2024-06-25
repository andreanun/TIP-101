#Problem 1: Prime Number
'''1) If n is less than or equal to 1, return False (not a prime).
2) Use a loop to check divisibility from 2 up to the square root of n:
  a) If n is divisible by any number in this range, it's not a prime, return False.
  b) If no divisors are found, it's a prime, return True.'''
def is_prime(n):
  if n <= 1:
      return False
  i = 2
  while i * i <= n:
      if n % i == 0:
          return False
      i += 1
  return True

#Problem 2: Two-Pointer Reverse List
'''1) Initialize two pointers: one at the beginning (`left`) and one at the end (`right`).
2) While `left` is less than `right`:
  a) Swap the elements at `left` and `right`.
  b) Move `left` pointer one step right (increase by 1).
  c) Move `right` pointer one step left (decrease by 1).
3) Return the list as the elements are now reversed in place.'''
def reverse_list(lst):
  if not lst:
    return []

  pointer_1 = 0
  pointer_2 = len(lst) -1

  while pointer_1 < pointer_2:
    temp = lst[pointer_1]
    lst[pointer_1] = lst[pointer_2]
    lst[pointer_2] = temp


    pointer_1 += 1
    pointer_2 -= 1 
    temp = lst[pointer_1]

  return lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))


#Problem 4: Move Even Integers
'''1) 1) Initialize two pointers: `left` at the start and `right` at the end of the list.
2) While `left` is less than `right`:
  a) If the number at `left` is even, move `left` pointer one step to the right.
  b) If the number at `right` is odd, move `right` pointer one step to the left.
  c) If the number at `left` is odd and the number at `right` is even, swap them, then move both pointers.
3) Return the modified list.'''
def sort_array_by_parity(nums):
  i = 0
  j = len(nums) - 1
  while i < j:
    if nums[i] % 2 == 0: #  till it finds odd
      i += 1
    elif nums[j] % 2 != 0: # till it finds even
      j -= 1
    else:
      temp = nums[i]
      nums[i] = nums[j]
      nums[j] = temp
      i += 1
      j -= 1

  return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))


#Problem 5: Palindrome
'''1) Define a helper function is_palindrome(s):
  a) Initialize two pointers, left starting at the beginning of the string, and right at the end.
  b) Loop while left is less than right:
      i) If characters at left and right are not the same, return False (not a palindrome).
     ii) Move left pointer one step to the right.
    iii) Move right pointer one step to the left.
  c) If no mismatches are found, return True (it is a palindrome).

2) Define the main function first_palindrome(words):
  a) Loop through each word in the list:
     i) Use the is_palindrome function to check if the current word is a palindrome.
    ii) If a palindrome is found, return that word immediately.
  b) If no palindromes are found after checking all words, return an empty string.'''
def is_palindrome(s):
  left, right = 0, len(s) - 1
  while left < right:
      if s[left] != s[right]:
          return False
      left += 1
      right -= 1
  return True

def first_palindrome(words):
  for word in words:
      if is_palindrome(word):
          return word
  return ""
#Chatgpt solution :
# def first_palindrome(words):
#   def is_palindrome(word):
#       return word == word[::-1]

#   if not isinstance(words, list): #This check ensures that the function only processes valid input (a list of strings)
#       return ""

#   for word in words:
#       if isinstance(word, str) and is_palindrome(word):
#           return word
#   return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

#Problem 6: Remove Duplicates with O(1)
'''1) If the list is empty, return 0.
2) Initialize a pointer j to 1.
3) Iterate through the list from the second element:
  a) If the current element is different from the previous one, place it at the j-th position.
  b) Increment j.
4) Return j as the new length of the list.'''
def remove_duplicates(nums):
  if not nums:
      return 0

  # Pointer j for the position of the next unique element
  j = 1

  # Iterate through the array with i
  for i in range(1, len(nums)):
      if nums[i] != nums[i-1]:
          nums[j] = nums[i]
          j += 1

  return j  # The new length after removing duplicates


nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list
