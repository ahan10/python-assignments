'''
#Program Number: 20
#Problem: Write a program to enter a number from the user and display the sum of all the digits in the number.
'''
num=int(input('Enter number: '))
sum = 0
for digit in str(num):
    sum = sum + int(digit)
print('Sum is:',sum)
'''
Program Output:
Enter number: 15
Sum is: 6
'''
