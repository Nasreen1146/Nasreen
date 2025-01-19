#1:display the details of the car

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


car1 = Car("Toyota", "Corolla", 2020)


car1.display_details()

#2:uppercase and lowercase letters
def count_case(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

input_string = "Hello World!"
upper, lower = count_case(input_string)
print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")


#3:even numbers

def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_numbers(numbers)

#4:Max of numbers

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = 10
num2 = 20
num3 = 15
print("The maximum of the three numbers is:", max_of_three(num1, num2, num3))

#5 :multiply list of numbers


def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [1, 2, 3, 4]
print("The product of all numbers in the list is:", multiply_list(numbers))


#6:reverse a string

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


input_string = "Hello, World!"
print("Reversed string:", reverse_string(input_string))

