#Problem 1: Sum of Strings
def sum_of_number_strings(nums):
  total = 0
  for num in nums:
    total += int(num)
  return total

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)

#Problem 2: Remove Duplicates
def remove_duplicates(nums):
  if not nums:
    return []

  i = 0
  while i < len(nums)-1:
    if nums[i] == nums[i+1]:
      nums.pop(i)
    else:
      i += 1

  return nums

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))

#Example Output: no_dups = [1,2,3,4,5,6]

#Problem 3: Reverse Letters
def reverse_only_letters(s):

  reversed = []

  for lett in s:
    if lett.isalpha():
      reversed.append(lett)

  result = ""

  lett_index = len(reversed)-1

  for lett in s:
    if lett.isalpha():
      result += reversed[lett_index]
      lett_index -=1 
    else:
      result += lett

  return result

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

#Example Output: j-Ih-gfE-dCba

#Problem 4: Longest Uniform Substring
def longest_uniform_substring(s):
  if not s:
    return 0

  max_length = 1
  current = 1
  for i in range(1, len(s)):
    if s[i] == s[i-1]:
      current += 1
      max_length = max(max_length, current)
    else: 
      current = 1

  return max_length

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)

#Problem 5: Teemo's Attack
def find_poisoned_duration(time_series, duration):
  # 1) Create an empty variable for total poisoned duration
  # 2) For each attack time except the last one
  #   a) Actual duration is the smaller of: 
  #       - the duration input
  #       - the next attack time minus this attack time
  #   b) Add the actual duration to the total
  # 3) The last attack will always fully complete, 
  #    so add one more duration to the total
  # 4) Return total
  total_duration = 0
  for i in range(len(time_series)-1):
  # Calculate the actual poisoning time between two attacks
    actual_duration = min(time_series[i+1] -time_series[i] - 1, duration)

    total_duration += actual_duration
    # Add the duration of the last attack
    total_duration += duration
  return total_duration


#Problem 6: Sum Unique Elements
def sum_of_unique_elements(lst1, lst2):
  count = {}

  for i in lst1 + lst2:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1

  unique_total = 0
  for num in lst1:
    if count[num] == 1:
      unique_total += num
  return unique_total

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)