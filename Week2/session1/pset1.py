# #June 10

Problem 1: Subsequence
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def is_subsequence(lst, sequence):
  i, j = 0, 0
  while i < len(lst) and j < len(sequence):
    if sequence[j] == lst[i]:  #keep going since they match up so far
      j +=1
    if j == len(sequence): #we've reached the end at the sub
      return True
    i += 1
  return False
# def is_subsequence(lst, sequence):
#   i = 0  #pointer for lst
#   j = 0  #pointer for sequence
#   while i < len(lst) and j < len(sequence):
#       if lst[i] == sequence[j]:
#           j += 1  
#       i += 1  
#   return j == len(sequence)
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

#Problem 3: Print Pair
def print_pair(dictionary, target):
  #key = dictionary[target]
  if target in dictionary:
    print("Key: " + target)
    print("Value: " + dictionary[target])
  else:  
    print("That pair does not exist!")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

#Problem 4: Keys Versus Values
def keys_v_values(dictionary):
  key_sum = sum(dictionary.keys())
  values_sum = sum(dictionary.values())
  
  if key_sum > values_sum:
    return "keys"
  elif values_sum > key_sum:
    return "values"
  return "balanced"
    

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

#Problem 5: Restock Inventory
def restock_inventory(current_inventory, restock_list):
  for item, quantity in restock_list.items():
      if item in current_inventory:
          current_inventory[item] += quantity
      else:
          current_inventory[item] = quantity

  return current_inventory

current_inventory = {
  "apples": 30,
  "bananas": 15,
  "oranges": 10
}

restock_list = {
  "oranges": 20,
  "apples": 10,
  "pears": 5
}

restock_inventory(current_inventory, restock_list)

print(current_inventory)

#Problem 6: Calculate GPA
def calculate_gpa(report_card):
  grades = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0}

  if not report_card:
    return 0.0
  
  total = 0
  for letter in report_card.values():
    points = grades[letter]
    total += points
  gpa = total / len(report_card)

  return gpa
  
report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

#Problem 7: Best Book
def highest_rated(books):
  if not books:    #empty list edge case
    return None

  highest = books[0]  
  
  for book in books[1:]:       #start with th second item
    if book['rating'] > highest['rating']:
      highest = book
  return highest

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))

#Problem 8: Index-Value Map
def index_to_value_map(lst):
  
  index_value_map = {}     #create empty dictionary
  
  for index in range(len(lst)):
    index_value_map[index] = lst[index]
  return index_value_map
    
lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))


  

    
    
  
  



    
    
