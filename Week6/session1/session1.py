#Problem 1: Nested Constructors
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  #we are simply creating three nodes and linking them
Node(4, Node(3, Node(2)))

#Problem 2: Find Frequency
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def count_element(head, val):
  count = 0  # Initialize a counter for the occurrences
  current = head  # Start with the head of the list

  while current:
      if current.value == val:
          count += 1  # Increment count if the current node's value matches val
      current = current.next  # Move to the next node

  return count  # Return the total count of occurrences

#Problem 3: Remove Tail
class Node:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

# Helper function to print the linked list
def print_list(node):
  current = node
  while current:
      print(current.value, end=" -> " if current.next else "")
      current = current.next
  print()

def remove_tail(head):
    if head is None:
        print("List is empty. No tail to remove.")
        return None
    if head.next is None:
        print("Only one node in the list. Removing the node.")
        return None

    current = head
    while current.next.next:  # Stop at the second-to-last node
        print(f"Current Node: {current.value} -> Next Node: {current.next.value}")
        current = current.next
    print(f"Removing tail node with value: {current.next.value}")
    current.next = None
    return head

#Problem 4: Find the Middle
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#Problem 5: Is Palindrome?
class Node:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

def is_palindrome(head):
  if head is None or head.next is None:
      return True  # A list with 0 or 1 element is a palindrome

  # Find the middle of the list
  slow = fast = head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

  # Reverse the second half of the list
  prev = None
  while slow:
      next_node = slow.next
      slow.next = prev
      prev = slow
      slow = next_node

  # Compare the first half and the reversed second half
  left, right = head, prev
  while right:  # Only need to compare till the end of the second half
      if left.value != right.value:
          return False
      left = left.next
      right = right.next

  return True

#Problem 6: Put it in Reverse
class Node:
  def __init__(self, value=None, next=None):
      self.value = value
      self.next = next

def reverse(head):
  previous = None  # This will eventually become the new head of the reversed list
  current = head  # Start with the head of the original list

  while current:
      next_node = current.next  # Temporarily store the next node
      current.next = previous  # Reverse the current node's pointer
      previous = current  # Move pointers one position forward
      current = next_node  # Continue to next node

  return previous  # At the end, 'previous' will be the new head of the reversed list