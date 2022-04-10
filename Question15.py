'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 15
#Problem: Write a program to find the sum of odd numbers and even numbers from 1 to N, N entered by the user.
'''
chk=1
cnt=int(input('Enter end number : '))
sumOdd = 0
sumEven = 0
for chk in range(1,cnt+1):
	if(chk%2==0):
    		sumEven = sumEven + chk
	else:
    		sumOdd = sumOdd + chk
print('Sum of odd numbers is: ', sumOdd)
print('Sum of even numbers is: ', sumEven)
'''
Program Output:
Enter end number : 15
Sum of odd numbers is:  64
Sum of even numbers is:  56
'''
