#simple inheritance 

#base class

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound ")
        

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks.")

# ##Create an instance of animal 
# animal = Animal("Generic Animal")
# animal.speak() #output generic animal makes sound.

# ##create an instance of dog
# Dog = Dog("Buddy")
# Dog.speak()

#Super Keyword

#Base class
class Animal:
    def __init__(self):
         self.name = "Buddy"

    def speak(self):
         print(f"{self.name} makes a sound")

##Derived Class
class Dog(Animal):
        def __init__(self, breed):
              super().__init__()
              self.breed = breed

        def speak(self):
              super().speak() #call the base class method
        print(f"{self.name} barks. It is a {self.breed}.")

## Create an instance of a dog
dog = Dog("Golden Retriver")
dog.speak()    