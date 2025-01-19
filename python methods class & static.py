# static methods:

class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b

# Example usage
print(MathOperations.add_numbers(3, 5))
print(MathOperations.multiply_numbers(3, 5))



#Class methods:

class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Example usage
p1 = Person()
p2 = Person()
print(Person.get_count())



#class & static
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def info(cls):
        return "This class provides methods for temperature conversions."

# Example usage
print(TemperatureConverter.celsius_to_fahrenheit(25))
print(TemperatureConverter.info())