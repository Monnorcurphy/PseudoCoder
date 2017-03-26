

class staticArray():

    # initialize this so you can build many instances of arrays
    def __init__(self, limit = 2, store = []):
      self.store = store
      self.limit = limit
      if len(self.store) > limit: self.limit = limit
      self.adjust()
      self.fill()
      self.last = self.find()

    #   Fill the array with none objects. This step is not necessary
    def fill(self):
      while self.limit != len(self.store):
        self.store = self.store + [None]

    #finds the last empty element in the array
    def find(self):
      if len(self.store) == 0: return 0
      i = 0
      while i < len(self.store):
        if self.store[i] is None:
          return i
        i += 1

      return i

    # #  returns the whole array
    def stack(self):
      return self.store

    #  returns the maximum length of the array
    def max(self):
      return self.limit

    # Adds to the array, returns false if the array is full
    def push(self, value):
      if self.last >= self.limit: return False
      self.store[self.last] = value
      self.last += 1
      return value


    # Removes the element from the array, allows you to put in an index
    # so you can remove from a specific position. Returns false if there
    # is nothing in the array.
    def pop(self, index = -1):
      if self.limit <= index: return False
      if len(self.store) == 0: return False
      if index == -1: index = self.last
      if self.store[index] is None: return False
      output= self.store[index]
      self.store[index] = None
      self.adjust()
      return output

    # Keeps the end of the array as the None objects.
    def adjust(self):
      i = 0
      j = 0
      while j < len(self.store):
        if self.store[i] is None and self.store[j] is not None:
          self.store[i], self.store[j] = self.store[j], self.store[i]
          i += 1
          j += 1
        elif self.store[i] is not None:
          i += 1
          j += 1
        else:
          j += 1


# Dynamic array using static array

class dynamicArray:
    def __init__(self, store=[]):
      self.limit = len(store*2)
      if len(store) == 0: self.limit = 2
      self.store = staticArray(self.limit, store)

    #   If you want to read about amoritization you can do so here:
    #
    # Readjusts the array size
    def amortize(self, value):
      self.limit = self.store.limit * 2
      self.store = staticArray(self.limit, self.store.stack())
      self.store.push(value)

    #  returns the array
    def stack(self):
      return self.store.stack()

    #  adds to the array, ups the size if limit of static array has been
    # reached
    def push(self, value):
      if self.store.last == self.limit:
        self.amortize(value)
        return value
      else:

        self.store.push(value)
        return value

    # removes the last element in the index, static array hanldes
    # the mess
    def pop(self, index):
      self.store.pop(index)

# stacks

class stack:

  def __init__(self, store= []):
    self.store= store

  # Add to the top
  def push(self, value):
    self.store = [value] + self.store

  # Take from the top
  def pop(self):
    output = self.store[0]
    self.store = self.store[1:]
    return output

  # Look at the top
  def peek(self):
    if len(self.store) == 0: return
    return self.store[0]


# Queues
class queue:

  def __init__(self, store= []):
    self.store= store

  # add to the back
  def push(self, value):
    self.store =  self.store + [value]

  # Take from the top
  def pop(self):
    output = self.store[0]
    self.store = self.store[1:]
    return output

  # look at the top
  def peek(self):
    if len(self.store) == 0: return
    return self.store[0]
