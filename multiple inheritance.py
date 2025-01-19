class LivingBeing:
    def breathe(self):
        print("Breathing")

class Mammal(LivingBeing):
    def walk(self):
        print("Walking")

class Human(Mammal):
    def think(self):
        print("Thinking")


human = Human()
human.breathe()
human.walk()
human.think()

# creating 2 classes

class Bird:
    def fly(self):
        print("Flying")

class Fish:
    def swim(self):
        print("Swimming")

class Duck(Bird, Fish):
    pass

# Example usage
duck = Duck()
duck.fly()
duck.swim()