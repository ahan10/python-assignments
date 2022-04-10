'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 22
#Problem: Write a program called ExtractDigits to extract each digit from an int in the reverse order. 
'''
num=int(input("Enter number: "))
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
print("Reverse of the number:",rev)
'''
Program Output:
Enter number: 12345
Reverse of the number: 54321
'''