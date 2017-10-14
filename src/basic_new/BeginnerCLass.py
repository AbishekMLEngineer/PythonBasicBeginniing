class BeginClass:
    #pass  #means I want to know Python That I am skipping this for moment
    def __init__(self,first,last,email):
        self.first= first   #its same emp1.fname ='firstname'
        self.last = last
        self.email = email

    def fullname(self):# it is the constructor in java
        return '{} {}'.format(emp2.first,emp2.last)

emp2 = BeginClass('anku','kachroo','abi111@mai.com') #so when we create the instances over here self is passed automatically so we just need to provide the instances
#print(emp2.fullname()) #so here it automatically sends the instance variable which is self o it should be present at the constructor level
print(BeginClass.fullname(emp2)) #here I need to specify the global instances
print(emp2.fullname()) #so here it automatically sends the instances self

# print(emp2)
#print(emp2.first)
#print(emp2.fullname())





'''
emp1 = BeginClass()
emp1.email ='abi@mai.com'
print(emp1.email)'''


