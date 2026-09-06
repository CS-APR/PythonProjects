# APR
# CSCE101 005
# 9/19/25
# Lab 5 if statements and prompts practice
print('Please enter a number between 1 and 10')
num = int(input())

if (num >= 1 and num <= 5):
    print('Blue')
elif (num>=6 and num <= 10):
    print('Green')
else:
    print('Out of range')
