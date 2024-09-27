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

with open('sample.txt', 'w') as file:
    file.write("Hello, this is a sample file.")


with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            # Split the content into words and count them
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
        return 0

filename = 'data.txt'

word_count = count_words_in_file(filename)
print(f"The number of words in '{filename}' is: {word_count}")

#Write a Python program to print the numbers from 1 to 10 using a for loop.
for number in range(1, 11):
    print(number)

#Write a Python program to display the multiplication table of a number entered by the user using a for loop.
user_number= float(input("enter a number"))

for i in range(1, 10):
    mul=user_number * i
    print(user_number ,"*",i,"=",mul)

#Write a Python function to find the maximum of three numbers
def max(a,b,c):
    if a>b:
        if a>c:
            print(a)
    elif b>a:
        if b>c:
            print(b)
    else:
        print(c)
max( 15,19,4)


#Write a Python function to multiply all the numbers in a list.

N = [1, 2, 3, 4, 5]


def multiple(New_List):
    result = 1
    for i in New_List:
        result = result * i
    return result


MUL = multiple(N)
print(MUL)



String= "reverse"

rev_string=String[::-1]

print(rev_string)


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

number = int(input("Enter a non-negative integer: "))
try:
    fact = factorial(number)
    print(f"The factorial of {number} is: {fact}")
except ValueError as e:
    print(e)


def distinct_elements(input_list):

    return list(set(input_list))


original_list = [1, 2, 2, 3, 4, 4, 5]
distinct_list = distinct_elements(original_list)
print("The original list: ",original_list)
print("The list with distinct elements:",distinct_list)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

#Write a Python program to print the even numbers from a given list.

List=float(input("enter list"))
 for i in List:
     result=i/2
     if result==0:
         print(result)

#Write a Python program to print the even numbers from a given list.

def even_numbers(list):
   for i in list:
       if i%2==0:
           print("Even numbers in the list:", i)

# Example usage
input_list = [1, 2, 3, 4,]
even_numbers(input_list)


#Write a Python function that accepts a string and counts the number of upper and lower case letters.

def count_letters(s):
    upper_count = 0
    lower_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

input_string = "MnoYT"
upper, lower = count_letters(input_string)
print("Uppercase letters:",upper)
print("Lowercase letters: ",lower)