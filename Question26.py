'''
#Program Number: 26
#Problem: Accept the marks (out of 70) for 3 subjects (Maths, physics, chemistry) from the user and check if the student is eligible for admission.
'''
subjectOne=int(input('Enter number for Maths (out of 70): '))
subjectTwo=int(input('Enter number for Physics (out of 70): '))
subjectThree=int(input('Enter number for Chemistry (out of 70): '))
percentage=((subjectOne + subjectTwo + subjectThree)/210) * 100
percMath=(subjectOne/70)*100
percPhys=(subjectTwo/70)*100
percChem=(subjectThree/70)*100
mathPhy= subjectOne + subjectTwo
if (percentage>=65 and percMath >= 50 and percPhys >= 45 and percChem >= 60):
    print('Eligible')
elif (mathPhy >= 120):
    print('Eligible')
else:
    print('Not Eligible')
'''
Program Output:
Enter number for Maths (out of 70): 56
Enter number for Physics (out of 70): 65
Enter number for Chemistry (out of 70): 59
Eligible
'''
