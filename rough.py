#lst = [1,2,3]
#my_int = 155

#print(type(my_int))
#lst.clear()
#print((lst))
#from oops_proj import chatbook
#user1=chatbook
 
lst = [1,2,3]
#function
a1=len(lst)
print(a1)
#method
##user1.sendmsg()


#getter and setter
from oops_proj import chatbook
user1 = chatbook()
print(user1.id)
# print(user1.get_name()) 
# user1.set_name("Agent X")
# print(user1.get_name())
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)
user3 = chatbook()
print(user2.id)