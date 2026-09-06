# Aden Roof
# 005
# 10/3/2025
# Functions to convert temperature

#User Input
name = input("Enter your name:")
conversion_choice = int(input("Enter 1 for CtoF, or 2 for FtoC conversion:"))
temperature = float(input("Enter the temperature value to convert:"))

#Defining functions
def CToF(temperature):
    converted = temperature * 1.8 + 32
    print(f"{converted}F")
def FToC(temperature):
    converted = (temperature-32)/1.8
    print(f"{converted}C")
    
#if/else statements
if conversion_choice == 1:
    CToF(temperature)
elif conversion_choice == 2:
    FToC(temperature)
else:
    print("Invalid Choice")

print(f"Thank you {name} for using this temperature converter.")
