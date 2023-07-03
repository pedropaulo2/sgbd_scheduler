class Dog:
    # Class attribute
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # # Instance method
    # def description(self):
    #     return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
class Bulldog(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)