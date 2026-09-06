# APR
# CSCE101 005
# 9/19/25
# Lab 5 Grade Calculator

#presents the % associated with each grade
print('CSCE 101 grade calculator')
print('Test1:         15%')
print('Test2:         15%')
print('Final Project: 15%')
print('Lab Average:   40%')
print('HW/Quizzes:    15%')
print('')

#1.a
print('Please enter the grade for each catagory')
t1 = float(input('Test 1 Grade: '))
t2 = float(input('Test 2 Grade: '))
fp = float(input('Final Project Grade: '))
la = float(input('Lab Average Grade: '))
hq = float(input('HW/Quizzes Grade: '))

#1.b
grade = (t1*.15)+(t2*.15)+(fp*.15)+(la*.40)+(hq*.15)

#1.c
if(grade >= 90):
    print('You got an A with a grade of:')
elif(90>grade>=87):
    print('You got a B+ with a grade of:')   
elif(86>grade>=80):
    print(' You got a B with a grade of:')
elif(80>grade>=77):
    print('You got a C+ with a grade of:')
elif(77>grade>=70):
    print('You got a C with a grade of:')
elif(70>grade>=67):
    print('You got a D+ with a grade of:')
elif(67>grade>=60):
    print('You got a D with a grade of:')
elif(60>grade):
    print('You got a F with a grade of:')
print(grade,'\n')

print('Thank you for using this calculator coded by aden roof')
