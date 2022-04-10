'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 23
#Problem: Accept a number N from the user and print the first N elements of the Fibonacci series.
'''
a = 0
b = 1
i = 0
sum = 0
inp=int(input('Enter number of digits: '))
print("Fibonacci Series: ", end = " ")
while(i <= inp):
  print(sum, end = " ")
  a = b
  b = sum
  sum = a + b
  i = i + 1
'''
Program Output:
Enter number of digits: 6
Fibonacci Series:  0 1 1 2 3 5 8
'''