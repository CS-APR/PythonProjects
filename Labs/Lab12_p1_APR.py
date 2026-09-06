#APR
# 005
# 11/7/2025
# part 1 functions, files

# function return vs print
def area_rectangle(length, width):
    return length*width

print(f"The area of the rectagle is {area_rectangle(5, 4)} cm squared.")

def area_rectangle_2(length, width):
    print(f"The area of the rectangle is {length*width} cm squared.")
area_rectangle_2(7,3)

# multiples of 7
def multiple_of_7(num):
    if ((num % 7) == 0):
        print(f"{num} is a multiple of 7")
    else:
        print(f"{num} is not a multiple of 7")
multiple_of_7(42)
multiple_of_7(57)

# files
data_file = open("data_entry.txt","a")
data_file.write("\n1000\n")

data_file.close()


