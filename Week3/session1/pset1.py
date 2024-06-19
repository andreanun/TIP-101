#Problem 1: Calling Mississippi
def count_mississippi(limit):
  for num in range(1, limit):
    print( f"{num} mississippi")


limit = 6
count_mississippi(limit)

#Problem 2: Swap Ends
def swap_ends(my_str):
  # 1) Slice the last character from the input string
  # 2) Slice the middle (excluding the first and last) characters from the input string
  # 3) Slice the first character fro:: the input string
  # 4) Return these three components added together in the order: last, middle, first
  if len(my_str) <= 1:
    return
  return my_str[-1:] + my_str[1:-1] + my_str[:1]
  #last   + excluding first and last + first at the 

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

#Problem 3: Is Pangram
def is_pangram(my_str):
  alphabet = 'abcdefghijklmnopqrstuvwxyz' 
  for char in alphabet:
    if char not in my_str.lower():
      return False
    return True


my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

#Problem 4: Reverse String
def reverse_string(my_str):
  return my_str[::-1]
  
my_str = "live"
print(reverse_string(my_str))


#Problem 5: First Unique
def first_unique_char(my_str):
  if not my_str:
    return -1
  dict = {}

  for char in my_str:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1

  for index, char in enumerate(my_str):
    if dict[char] == 1:
      return index
  return -1


my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

str4 = ""
print(first_unique_char(str4))


#Problem 6: Minimum Distance
def min_distance(words, word1, word2):
  for index, word in enumerate(words):
    if word == word1:
      indexWord1 = index
    elif word == word2:
      indexWord2 = index
  return indexWord2 - indexWord1
# 1) Set an initial minimum distance to be the worst case (word1 and word2 are first and last in the list of words)
# 2) Loop through the list of words
#   a) If the word is word1, record a start index
#     i) If the end index has already been found, update the minimum distance (if smaller)
#   b) Otherwise if the word is word2, record a stop index
#     i) If the start index has already been foudn, update the minimum distance (if smaller)
# 3) If the minimum distance was at some point updated, return it
# 4) Otherwise, return -1
# 

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words, "code", "practice")
print(dist3)


  
