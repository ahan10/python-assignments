'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 10
#Problem: Write a Python program to make a Simple Calculator.
'''
a=int(input('Enter number a: '))
b=int(input('Enter number b: '))
print('Enter 1 for Addition \nEnter 2 for Subraction \nEnter 3 for Multiplication \nEnter 4 for Division\n')
c=(input('Enter Choice: '))
if c in ('1', '2', '3', '4'):
	if c=='1': 
		{
		  print('Answer:', (a+b))
		}
	elif c=='2': 
		{
		  print('Answer:', (a-b))
		}
	elif c=='3': 
		{
		  print('Answer:', (a*b))
		}		
	elif c=='4': 
		{
		  print('Answer:', (a/b))
		}
'''
Program Output:
Enter number a: 12
Enter number b: 24
Enter 1 for Addition
Enter 2 for Subraction
Enter 3 for Multiplication
Enter 4 for Division

Enter Choice: 4
Answer: 0.5
'''