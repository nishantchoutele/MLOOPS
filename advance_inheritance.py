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

#heirarchical inheritance

#base class
class Parent:
    def __init__(self,name):
        self.name = name 

    def greet(self):
        print(f"Hello my name is {self.name}")

#derived class 
class Child1(Parent):

    def play(self):
        print(f"{self.name} is playing.")

#derived class 2
class Child2(Parent):

    def study(self):
        print(f"{self.name} is studing")

#Create instance for child1 and child2
child1 = Child1("Dave")
child2 = Child2("Eve")
#obj
child1.greet() # Hello my name is dave
child1.play()  # Dave is playing 

child2.greet()  #Hello my name is Eve
child2.study()  #Eve is studing 


#multiple inheritance(Diamond problem) 3:30:17
#base class
class A:
    def __init__(self, name):
        self.name = name 

    def greet(self):
        print(f"Hello from A, {self.name}.")
        
#intermidate class 1
class B(A):
    def greet(self):
        print(f"Hello from B, {self.name}.")
        super().greet()

#intermediate class 2
class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}.")
        super().greet()

# derived class
class D(B,C):
    def greet(self):
        print(f"Hello from D, {self.name}")
        super().greet()

#create an instance
d = D("Frank")
d.greet()
#Output 
#Hello from D,frank
#Hello from B,Frank
#Hello from C,Frank
#Hello from A,Frank

#Hybrid inheritance
#base class
class Animal:
    def __init__(self , name):
        self.name = name

    def sound(self):
        print(f"{self.name} notes a sound ")


#intermidiate class 1 (herarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk")

#intermidiate class 2 (multiple)
class bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")

#derived class(Multiple inheritance)
class Bat(Mammal, bird):
    def  __init__(self, name):
        super().__init__(name) 

    def nocturnal(self):
        print(f"{self.name} is nocturnal")

#create an instance of bat 
bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()



    
         
