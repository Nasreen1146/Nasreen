#Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
#Addition
#Subtraction
#Multiplication
#Division
#Modulus
#Display the results for each operation.


First_number=float(input("Please Enter the first number: "))
Sec_number=float(input("Please Enter the Second Number: "))

#operations
print("Addition of two numbers: ",First_number + Sec_number)
print("Subtraction of two numbers: ",First_number - Sec_number)
print("Multiplication of two numbers: ",First_number * Sec_number)
print("Division of two numbers: ",First_number / Sec_number)
print("Modulus of two numbers: ",First_number % Sec_number)


#Write a Python program that checks whether a given number is even or odd using the modulus operator.
number=float(input("Enter the number: "))

if number%2 != 0:
   print("Given number",number,"is odd ")
else:
    print("Given number",number,"is even number ")


#Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.

number_type=float(input("Enter the number: "))
if number_type==0:
    print("Given number is 0")
elif number_type>0:
    print("Given number",number_type," is Positive number")
else:
    print("Given number",number_type," is negative number")


#Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:

#90 and above: A
#80 - 89: B
#70 - 79: C
#60 - 69: D
#Below 60: F


marks=float(input("Enter the marks of student and it must <=600"))
total_marks=600
percentage=(marks/total_marks)*100
if percentage>100:
    print("invalid input")
elif percentage>=90 and percentage<=100:
    print("Congratulations your grade is 'A'")
elif percentage>=80 and percentage<=89:
    print("Congratulations your grade is 'B'")
elif percentage>=70 and percentage<=79:
    print("Congratulations your grade is 'C'")
elif percentage>=60 and percentage<=69:
    print("Congratulations your grade is 'D'")
elif percentage<60:
    print("your grade is 'F'")

#Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.
















