# Aden Roof
# 005
# 9/26/2025
# Lab Activity 06 Practicing loops lists and random

import random
snack_list = []
for i in range(5):
    print('Enter a snack')
    snack_in = input()
    snack = snack_in
    snack_list.append(snack)
    i+1

print(snack_list)
print()

for i in range(3):
    num = random.randint(0,4)
    print(snack_list[num])
