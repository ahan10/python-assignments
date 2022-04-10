'''
#Program Number: 24
#Problem: Calculate the area of triangle given its three sides.
'''
import math
sideOne=int(input('Enter side one: '))
sideTwo=int(input('Enter side two: '))
sideThree=int(input('Enter side three: '))
s = (sideOne + sideTwo + sideThree)/2
formula = s*((s-sideOne)*(s-sideTwo)*(s-sideThree))
area = math.sqrt(formula)
print('The area is:',area)
'''
Program Output:
Enter side one: 12
Enter side two: 15
Enter side three: 13
The area is: 74.83314773547883
'''
