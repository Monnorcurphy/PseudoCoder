# 28. How to reverse array in place in Java? (solution)
# Now let's see one of the most frequently asked array interview question. You need to write a program which accepts an integer array and your program needs to reverse that array in place, which means you cannot use additional buffer or array, but one or two variables will be fine. Of course you cannot use any open source library or Java API method to directly solve this problem, you need to create your own logic. Here is one such logic to solve this problem


def reverser(array):
  i = 0
  length = len(array)
  while i <= (length/2):
    array[i], array[length - 1] = array[length - 1], array[i]
    i += 1
    length -= 1

  return array

a = [0,1,2,3]
print(reverser(a))


# 26. How to find minimum value in a rotated sorted array? (solution)
# This is another advanced level array coding question and you should only attempt this one, once you have solved the easier ones. Suppose a sorted array is rotated at some pivot unknown to you beforehand.

# 5
a = [3,4,5,1]

def minFinder(array):
  i = 0
  while i + 1 < len(array):
    if array[i] > array[i +1]:
      return array[i + 1]
    else:
      i += 1

  return array[0]


print(minFinder(a))


# 2. How to find duplicate number on Integer array in Java? (solution)
# An array contains n numbers ranging from 0 to n-2. There is exactly one number is repeated in the array. You need to write a program to find that duplicate number. For example, if an array with length 6 contains numbers {0, 3, 1, 2, 3}, then duplicated number is 3.

a= [0,1,2,1]

def duplicatesFind(array):
  i = 0
  duplicate = 0
  actual = 0

  while i < len(array) - 2:
    actual += i
    duplicate += array[i]
    i += 1

  duplicate += array[i + 1]

  return duplicate - actual


print(duplicatesFind(a))


# 3. How to check if array contains a number in Java? (solution)
# Another interesting array problem, because array doesn't provide any builtin method to check if any number exists or not.
# sorted

def binarySearch(array, num):
  if len(array)==0 : return
  mid = int(len(array)/ 2)
  if array[mid] == num: return mid
  if len(array) == 1: return -1

  if num < array[mid]:
    mid = binarySearch(array[:mid], num)
  else:
    output = binarySearch(array[mid:], num)
    if output == -1:
      return -1
    mid += output

  return mid

a = [0,1,2,3,4,5,6]

print(binarySearch(a, 2))
print(binarySearch(a, 100))

# unsorted

def linearSearch(array, num):

  for el in array:
    if el == num:
      return True

  return False

print(linearSearch(a, 3))
print(linearSearch(a, 7))


# 4. How to find largest and smallest number in unsorted array? (solution)
# This is a rather simple array interview question. You have given an unsorted integer array and you need to find the largest and smallest element in the array.
a = [0,10, 13, 100, -9, 45, 382, 9, -100, 7, 18]
b = []
def biggestSmallest(array):
  if len(array) == 0: return None
  largest = array[0]
  smallest = array[0]
  for el in array:
    if el > largest:
      largest = el
    if el < smallest:
      smallest = el

  return [largest, smallest]

print(biggestSmallest(a))
print(biggestSmallest(b))


# Check if a string is a palindrome

def palindrome(string):
  if len(string) == 0: return False
  if len(string) == 1: return True
  odd = False
  length = int(len(string)/2)
  string= list(string)

  if len(string) %2 != 0:
    length += 1
    odd = True

  queue = []

  for idx, el in enumerate(string):
    if idx < length:
      queue.append(el)
    elif idx >= length and not odd:
      if el != queue[-1]: return False
      queue.pop()

    elif idx == length and odd:
      queue.pop()
    else:
      if el != queue[-1]: return False
      queue.pop()


  return True

a = 'bab'
print(palindrome(a))
