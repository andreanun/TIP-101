#June 10

#Problem 1: Subsequence
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def is_subsequence(lst, sequence):
  i, j = 0, 0
  while i < len(lst):
    if sequence[j] == lst[i]:  #keep going since they match up so far
      j +=1
    if j == len(sequence): #we've reached the end at the sub
      return True
    i += 1
  return False

print(is_subsequence(lst, sequence))

#Problem 2: Create a Dictionary
def create_dictionary(keys, values):
  pairs = {}
  for i in range(len(keys)):
    pairs[keys[i]] = values [i]
  return pairs

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

print(create_dictionary(keys, values))
    
    
    
  
  



    
    
