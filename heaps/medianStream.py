"""
Median Stream
You're given a list of n integers arr[0..(n-1)]. You must compute a list output[0..(n-1)] such that, 
for each index i (between 0 and n-1, inclusive), output[i] is equal to the median of the elements arr[0..i] 
(rounded down to the nearest integer).
The median of a list of integers is defined as follows. If the integers were to be sorted, then:
If there are an odd number of integers, then the median is equal to the middle integer in the sorted order.
Otherwise, if there are an even number of integers, then the median is equal to the average of the two middle-most integers in the sorted order.

Signature
int[] findMedian(int[] arr)
Input
n is in the range [1, 1,000,000].
Each value arr[i] is in the range [1, 1,000,000].
Output
Return a list of n integers output[0..(n-1)], as described above.
Example 1
n = 4
arr = [5, 15, 1, 3]
output = [5, 10, 5, 4]
The median of [5] is 5, the median of [5, 15] is (5 + 15) / 2 = 10, the median of [5, 15, 1] is 5, and the median of [5, 15, 1, 3] is (3 + 5) / 2 = 4.
Example 2
n = 2
arr = [1, 2]
output = [1, 1]
The median of [1] is 1, the median of [1, 2] is (1 + 2) / 2 = 1.5 (which should be rounded down to 1).

"""

import heapq

def findMedian(arr):
  maxHeap, minHeap = [-1*arr[0]], []
  heapq.heapify(maxHeap)
  heapq.heapify(minHeap)
  
  res = [arr[0]]
  
  # what if number of elements is even
  for index in range(1, len(arr)):
    if (index)%2:
      if arr[index] >= -1*maxHeap[0]:
        heapq.heappush(minHeap, arr[index])
      else:
        top = -1 * heapq.heappushpop(maxHeap, -1 * arr[index])
        heapq.heappush(minHeap, top)
      res.append((-1*maxHeap[0] + minHeap[0])//2)    
            
    else:
      if arr[index] > minHeap[0]:
        top = -1 * heapq.heappushpop(minHeap, arr[index])
        heapq.heappush(maxHeap, top)
      else:
        heapq.heappush(maxHeap, -1 * arr[index])
      res.append(-1 * maxHeap[0])
  return res    

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)
  
  arr_3 = [1, 2]
  expected_3 = [1, 1]
  output_3 = findMedian(arr_3)
  check(expected_3, output_3)

  # Add your own test cases here
  