class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Example usage
calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4))