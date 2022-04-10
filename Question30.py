'''
#Program Number: 30
#Problem: Print multiplication table of a number entered by the user. Validate that the number must be between 1 and 20.
'''
num=int(input('Enter number whose table you want: '))
if(num>=1 and num<=20):
    print('Table of',num,':')
    for i in range(1,11):
        print(num,'X',i,'=',num*i)
else:
    print('Enter a number between 1 and 20')
'''
Program Output:
Table of 5 :
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
'''
