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