#Tip 101 June 4th Session 1!


#MOHAMMED PROBLEMS 6-10
#6
def classify_age(age):
  if age < 18:
    return "child"
  return "adult"


#7
def what_time_is_it(hour):
  if hour == 2:
    return "taco time"
  elif hour == 12:
    return "peanut butter jelly time"
  else:
    return "nap time"

#8
def blackjack(score):
  if score == 21:
    return "Blackjack"
  elif score > 21:
    return "Bust!"
  elif score >= 17 and score < 21:
    return "Nice hand!"
  else:
    return "Hit me!"


#9
def get_first(lst):
  if lst:
    return lst[0]
  return None

#10
def get_last(lst):
  if lst:
    return lst[-1]
  return None


#ANDREA PROBLEMS 11-15

#Problem 11: Counter
def counter(stop):
  for i in range(1,stop + 1):
    print(i)


#Problem 12: Sum of 1 to 10
def sum_ten():
  sum = 0
  for i in range(1, 11):
    sum += i
    return sum


#Problem 13: Total Sum
def sum_positive_range(stop):
  sum = 0
  for i in range(1, stop +1 ):
    sum += i
    return sum


#Problem 14: Total Sum in Range
def sum_range(start, stop):
  sum = 0
  for i in range(start, stop + 1):
    sum += i
  return sum

#Problem 15: Negative Numbers
def print_negatives(lst):
  for num in lst:
    if num < 0:
      print(num)




