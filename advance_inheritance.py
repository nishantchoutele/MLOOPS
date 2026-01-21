#single or basic inheritance 

#Base class 
class Parent:
    def __init__(self,name):
        self.name = name 

    def greet(self):
        print(f"Hello my name is {self.name}")

#derived class
class Child(Parent):
    
    def play(self):
        print(f"{self.name} is playing ")

# create an instance of child 
child = Child("Alice")
child.greet() #Output hello my name is alice 
child.play() #Alice is playing

# multilevel inheritance
#base class
class Grandparent:
    def __init__(self,name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story ")

#intermidiate class
class Parent(Grandparent):
    
    def work(self):
        print(f"{self.name} is working")

#Derived class
class Child(Parent):

    def play(self):
        print(f"{self.name} is playing")

#create an  instance of child 
child = Child("Charlie")
child.tell_story() # Charlie tells a story
child.work()       # Charlie is working 
child.play()       # Charlie is working 

        

         
