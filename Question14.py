'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 14
#Problem: Write a Python program to input 3 numbers from user and print the maximum among
them.
'''
numOne=int(input('Enter number 1: '))
numTwo=int(input('Enter number 2: '))
numThree=int(input('Enter number 3: '))
great = numOne
if (numTwo>great):
	great= numTwo
elif (numThree>great):
	great=numThree
print(great,'is the greatest of three')
'''
Program Output:
Enter number 1: 16
Enter number 2: 45
Enter number 3: 35
45 is the greatest of three
'''