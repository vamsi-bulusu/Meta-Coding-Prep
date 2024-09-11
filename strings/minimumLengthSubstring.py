"""
Minimum Length Substrings
You are given two strings s and t. 
You can select any substring of string s and rearrange the characters of the selected substring. 
Determine the minimum length of the substring of s such that string t is a substring of the selected substring.

int minLengthSubstring(String s, String t)
Input
s and t are non-empty strings that contain less than 1,000,000 characters each
Output
Return the minimum length of the substring of s. If it is not possible, return -1
Example
s = "dcbefebce"
t = "fd"
output = 5
Explanation:
Substring "dcbef" can be rearranged to "cfdeb", "cefdb", and so on. 
String t is a substring of "cfdeb". Thus, the minimum length required is 5.

"""

import math
from collections import Counter

def min_length_substring(s, t):
  
  def isSubstring(s, l):
    for i in range(0, len(s) - l, l):
      smap = Counter(s[i: i + l])
      for k, v in freqMapT.items():
        if k not in smap or v != smap[k]:
          return False
    return True
  
  freqMapT = Counter(t)
    
  # answer can be 0 to lens(s) if present
  left, right = 0, len(s) - 1
  answer = -1
  while(left <= right):
    mid = (left + right)//2
    
    if(isSubstring(s, mid)):
      answer = mid
      right = mid - 1
    else:
      left = mid + 1
  
  return answer
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  