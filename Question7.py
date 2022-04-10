'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 7
#Problem: Write a Python program to input angles of a triangle and check whether triangle is valid or not.
'''
angleOne=int(input('Enter angle 1: '))
angleTwo=int(input('Enter angle 2: '))
angleThree=int(input('Enter angle 3: '))
sum = angleOne + angleTwo + angleThree
if (sum == 180):
    print('It is a valid triangle')
else:
    print('It is not a valid triangle')
'''
Program Output:
Enter angle 1: 60
Enter angle 2: 60
Enter angle 3: 60
It is a valid triangle
'''