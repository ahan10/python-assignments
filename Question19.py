'''
#Program Number: 19
#Problem: Write a program to accept two numbers and one mathematical operator. Calculate and display appropriate answer.
'''
numOne=int(input('Enter 1st number: '))
numTwo=int(input('Enter 2nd number: '))
sign=input('Enter sign: ')
if sign=='+': 
	  print('Answer:', (numOne+numTwo))
elif sign=='-': 
	  print('Answer:', (numOne-numTwo))
elif sign=='*': 
	  print('Answer:', (numOne*numTwo))
elif sign=='/': 
	  print('Answer:', (numOne/numTwo))
'''
Program Output:
Enter 1st number: 12
Enter 2nd number: 12
Enter sign: *
Answer: 144
'''
