'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 21
#Problem: Accept a year from the user and check whether it is leap year or not.
'''
year=int(input('Enter year to check for: '))
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
elif year % 100 == 0:
    print(year, "is not a Leap Year")
elif year % 400 ==0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
'''
Program Output:
Enter year to check for: 2020
2020 is a Leap Year
'''