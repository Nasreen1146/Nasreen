#1

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


my_car = Car("Toyota", "Corolla", 2020)


my_car.display_details()

#2

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print("Student Details:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)


student1 = Student("John Doe", 101, 85)


student1.display_info()

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


rect1 = Rectangle(4, 6)
rect2 = Rectangle(5, 8)
rect3 = Rectangle(7, 3)


print("Rectangle 1: Area =", rect1.area(), "Perimeter =", rect1.perimeter())
print("Rectangle 2: Area =", rect2.area(), "Perimeter =", rect2.perimeter())
print("Rectangle 3: Area =", rect3.area(), "Perimeter =", rect3.perimeter())

#3

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius


circle1 = Circle(5)


print("Area of the circle:", circle1.get_area())
print("Circumference of the circle:", circle1.get_circumference())

#4

class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited: {amount}. New Balance: {self.balance}")

    def print_balance(self):
        print(f"Account No: {self.account_no}, Balance: {self.balance}")


account1 = Account("123456789", 1000)


account1.credit(500)
account1.debit(300)

# Print balance
account1.print_balance()


#5

class EmployeeSalary:
    bonus_percentage = 10  # Default bonus percentage

    def __init__(self, basic_salary):
        self.basic_salary = basic_salary

    @classmethod
    def set_bonus_percentage(cls, new_percentage):
        cls.bonus_percentage = new_percentage

    def calculate_total_salary(self):
        bonus = (self.basic_salary * EmployeeSalary.bonus_percentage) / 100
        total_salary = self.basic_salary + bonus
        return total_salary


employee1 = EmployeeSalary(5000)
employee2 = EmployeeSalary(7000)


EmployeeSalary.set_bonus_percentage(15)


print("Employee 1 Total Salary:", employee1.calculate_total_salary())
print("Employee 2 Total Salary:", employee2.calculate_total_salary())