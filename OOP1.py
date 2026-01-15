#initiate a CLASS
class employee:
    #special method\magic method\dunder method - constuctor
    def __init__(self):
        print("Started executing attributes/data ")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE" 
        print("attributes/data has been initiated")

    def travel(self, destination):
        print("This travel METHOD was called manually")
        print(f"Employee is now travelling to {destination}")

# creat an object of the class
sam = employee()
sam.name = "samkumar"

#calling a method
sam.travel("kerela")
#printing an attriburte
#print(sam.id)
print(type(sam))
print(sam.name)
from oops_proj import chatbook
user1=chatbook()
print(user1._chatbook__name)