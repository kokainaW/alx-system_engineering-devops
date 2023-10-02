#!/usr/bin/python3
#Python program to find middle number among three
num1=int(input("Enter the first number: "))
#get input from the user for first number
num2=int(input("Enter the second number: ")) 
#get input from the user for second number
num3=int(input("Enter the third number: "))
#get input from the user for third number

def middle_digit():#function definition
    middle=0;
    if(num1>num2):
        if(num2>num3):
            middle=num2;

        elif(num3>num1):
            middle=num1;

        else:

            middle=num3;

        else:

            if(num2<num3):
                middle=num2;

            elif(num3<num1):
                middle=num1;

            else:
                middle=num3;

    print("middle_digit(num1,num2,num3)",middle);
middle_digit();#Calling the function
