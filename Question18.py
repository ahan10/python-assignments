'''
#RollNo-Name: AU2020167 Ahan Bhargava
#Program Number: 18
#Problem: Write a program to check whether a character is uppercase or lowercase alphabet.
'''
const=input("Enter Character: ")
if(const.isupper()):
    print('It is Uppercase.')
if(const.islower()):
    print('It is Lowercase.')
else:
    print('Special Character or both upper and lowercase')
'''
Program Output:
Enter Character: a
It is Lowercase.
'''