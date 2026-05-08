#🏆 Challenge 1: Even or Odd Checker
#Goal:
#Write a program that asks the user for a number and tells them whether it is even or odd.

#Inputs/Outputs:
# - Input: A single integer entered by the user.
# - Output: A message stating whether the number is even or odd.

#Constraints:
# - Assume the user will always enter a valid integer.
# - No need to handle floats or strings.
# - Use conditional statements (if/else) to decide.

Input1 = None

Input1 = int(input("Enter a number: "))
if Input1 % 2 == 0:
  print("Even")
else:
  print("odd")

#📊 Score: 7.5 / 10
#Logic: 4/4
#Readability: 2/3 (variable naming could improve)
#Efficiency: 1.5/2 (extra initialization line)
#Best Practices: 0/1 (output doesn’t match spec exactly)