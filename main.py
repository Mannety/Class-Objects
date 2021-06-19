'''
animal.py
'''
class Animal:
    # initialize
    def __init__(self, name, age):
        # instance variable
        self.name = name
        self.age = age

    # instance method
    def speak(self):
        return f"My name is {self.name} and I am {self.age} years old"

    def intro(self):
        return f"I am {self.name}"

'''
main.py
'''
# from file import Klass
from animal import Animal

# instance / object
dog = Animal(name='Lizzy', age=3)
cat = Animal(name='Zorka', age=10)
bird = Animal(name='Fufu', age=5)

print(dog.speak())
print(cat.speak())
print(bird.speak())


print(bird.intro())
print(dog.intro())
print(cat.intro())