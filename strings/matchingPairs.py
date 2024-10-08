
"""

swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s,

respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.
Signature
int matchingPairs(String s, String t)
Input
s and t are strings of length N
N is between 2 and 1,000,000
Output
Return an integer denoting the maximum number of matching pairs
Example 1
s = "abcd"
t = "adcb"
output = 4
Explanation:
Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
Therefore, the number of matching pairs of s and t will be 4.
Example 2
s = "mno"
t = "mno"
output = 1
Explanation:
Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. 
If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.


"""


import math

def matching_pairs(s, t):
  
  ss, ts, hs = set(), set(), set()
  onePairMatch = 0
  for index in range(len(s)):
    if s[index] != t[index]:
      hs.add((s[index], t[index]))
      if (t[index] in ss) or (s[index] in ts):
        onePairMatch = 1
      ss.add(s[index])
      ts.add(t[index])
      
      
  #  case 1: when you have no unmatched pairs: 
  if len(hs) == 0:
    return len(s) - 2
  
  matchingPairs = len(s) - len(hs)
  
  for pair in hs:
    if (pair[1], pair[0]) in hs:
      return matchingPairs + 2
  

  return matchingPairs + onePairMatch
    
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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  