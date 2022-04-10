'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 25
#Problem: Write a program that take input of 3 subjects marks out of 150. Count the percentage
'''
subjectOne=int(input('Enter number for Maths (Out of 150):'))
subjectTwo=int(input('Enter number for Physics (Out of 150): '))
subjectThree=int(input('Enter number for Chemistry (Out of 150): '))
percentage=((subjectOne + subjectTwo + subjectThree)/450) * 100
if (percentage<=100 and percentage>=70):
    print(percentage,'% DISTINCTION')
elif (percentage<=69 and percentage>=60):
    print(percentage,'% FIRST CLASS')
elif (percentage<=59 and percentage>=50):
    print(percentage,'% SECOND CLASS')
elif (percentage<=49 and percentage>=40):
    print(percentage,'% PASS CLASS')
elif (percentage<=40 and percentage>=0):
    print(percentage,'% FAIL')
else:
    print('INVALID NUMBER')
'''
Program Output:
Enter number for Maths (Out of 150):150
Enter number for Physics (Out of 150): 150
Enter number for Chemistry (Out of 150): 150
100.0 % DISTINCTION
'''