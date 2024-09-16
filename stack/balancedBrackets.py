"""
Balance Brackets
A bracket is any of the following characters: (, ), {, }, [, or ].
We consider two brackets to be matching if the first bracket is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type. That means ( and ), [ and ], and { and } are the only pairs of matching brackets.
Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
The sequence is empty, or
The sequence is composed of two or more non-empty sequences, all of which are balanced, or
The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.
You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false
Signature
bool isBalanced(String s)
Input
String s with length between 1 and 1000
Output
A boolean representing if the string is balanced or not
Example 1
s = {[()]}
output: true
Example 2
s = {}()
output: true
Example 3
s = {(})
output: false
Example 4
s = )
output: false
"""

def isBalanced(s):
  # compare s[i] & s[i - 1] if both open and same type do nothing
  # if s[i] & s[i - 1] are opposite then we found a match
  
  stack = []
  op = ['(', '[', '{']
  
  for i in range(len(s)):
    if len(stack) == 0 or s[i] in op:
      stack.append(s[i])   
    else:
      if len(stack) > 0 and (stack[-1] == '(' and s[i] == ')') or (stack[-1] == '{' and s[i] == '}') or (stack[-1] == '[' and s[i] == ']'):
        stack.pop() 
      else:
        return False
  
  return (len(stack) == 0)      


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "{[(])}"
  expected_1 = False
  output_1 = isBalanced(s1)
  check(expected_1, output_1)

  s2 = "{{[[(())]]}}"
  expected_2 = True
  output_2 = isBalanced(s2)
  check(expected_2, output_2)
  
  s3 = "{(})"
  expected_3 = False
  output_3 = isBalanced(s3)
  check(expected_3, output_3)
  
  s4 = ")"
  expected_4 = False
  output_4 = isBalanced(s4)
  check(expected_4, output_4)
  # Add your own test cases here
  