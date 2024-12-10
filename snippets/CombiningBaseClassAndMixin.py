from AnimalClass import Animal
from LoggingMixin import LoggingMixin


class Dog(Animal, LoggingMixin):
    def speak(self):
        self.log(f"{self.name} says woof!")


dog = Dog("David")
dog.speak()
