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

  def display(self):
    if self is None: return None
    output = []
    node = self
    while node is not None:
      output.append(node.value)
      node = node.next

    print(output)

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


class TreeNode:
  def __init__(self, value= None, parent = None, children= {}):
    self.value = value
    self.parent = parent
    self.children = children


class GraphNode:
  def __init__(self, value= None, connections = {}):
    self.value = value
    self.connections = connections
