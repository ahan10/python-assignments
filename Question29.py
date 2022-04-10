'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 29
#Problem: Write a program to print following pattern. (hint: nested for loop)
A
B B
C C C
D D D D
''' 
alpha = 65
for i in range (0,4):
    for j in range(0,i+1):
        a=chr(alpha)
        print(a, end=' ')
    alpha = alpha + 1
    print('\r')
'''
Program Output:
A
B B
C C C
D D D D
'''