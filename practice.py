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
    
