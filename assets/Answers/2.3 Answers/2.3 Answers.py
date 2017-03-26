# Linked Node class
class LinkedNode:
  def __init__(self, value= None, prev = None, next = None,):
    self.value = value
    self.next = next
    self.prev = prev

  # A method for turning an array into a linked list
  def linkedListify(self, array= []):
    if len(array) == 0: return LinkedNode()
    if len(array) == 1: return LinkedNode(array[0])
    i = 0
    last = None
    node = None

    while i < len(array):
      node = LinkedNode(array[i], last)
      if last is not None: last.next = node
      if i == 1: first= last
      last = node
      i += 1

    return first

  # an output method to display the entirity of the linked list, in array form
  def display(self):
    if self is None: return None
    output = []
    node = self
    while node is not None:
      output.append(node.value)
      node = node.next

    print(output)

  # a built in reverse method, returns the new head
  def reverseify(self):
    if self is None: return None
    if self.next is None: return self

    prev = None
    next = self.next
    current = self

    while current is not None:
      current.prev= next
      current.next = prev
      prev = current
      current = next
      if next is not None: next = next.next


    return prev

    # If given a specific node, that node is deleted. If not in the list
    # then we return False
    def deleteNode(self, node):
    deleted= False
    head = self
    while head is not None:
      if head.next == node:
        head.next = node.next
        deleted= True
      elif head.prev == node:
        head.prev = node.prev
        return True
      head = head.next
    return deleted

    # Given a specific value, we delete the first instace of it. If not
    # in the list, we return false
    def deleteValue(self, value):
    deleted = False
    head = self
    while head is not None:
      if head.next.value == value:
        head.next = head.next.next
        deleted = True
      elif head.prev is not None and head.prev.value == value :
        head.prev = head.prev.prev
        while head.prev is not None:
          head = head.prev
        return head
      head = head.next

    return deleted

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!! add a delete all values
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class TreeNode:
  def __init__(self, value= None, parent = None, children= {}):
    self.value = value
    self.parent = parent
    self.children = children


class GraphNode:
  def __init__(self, value= None, connections = {}):
    self.value = value
    self.connections = connections
