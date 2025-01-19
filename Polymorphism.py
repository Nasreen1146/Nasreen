#polymorpism overloading

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Example usage
calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4))


# polymophism overriding

class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

# Example usage
dog = Dog()
cat = Cat()
dog.speak()
cat.speak()