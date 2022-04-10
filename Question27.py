'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 27
#Problem: Considering three numbers provided by the user as length of sides of a triangle, first check, if the values are valid for representing the sides of a triangle. If the lengths of sides are valid, print the type of the triangle.
'''
side1=int(input('Enter side 1: '))
side2=int(input('Enter side 2: '))
side3=int(input('Enter side 3: '))
s1 = side1 + side2
s2 = side2 + side3
s3 = side3 + side1
if (s1>side3):
    if(s2>side1):
        if(s3>side2):
            if(side1 == side2 == side3):
                print('Equilateral Triangle')
            elif(side1 == side2 or side2 == side3 or side2 == side1):
                print('Isosceles Triangle')
            else:
                print('Scalene Triangle')
        else:
            print('Triangle not possible.')
    else:
        print('Triangle not possible.')
else:
    print('Triangle not possible.')
'''
Program Output:
Enter side 1: 15
Enter side 2: 16
Enter side 3: 35
Triangle not possible.
'''