class Employee:
    raise_amount =1.04
    noOFEmployees=0
    number=0

    def __init__(self,first,last,pay):
        self.first = first
        self.last =last
        self.pay =pay
        self.email= first +'.'+last+'@company.com'
        Employee.noOFEmployees +=1
        self.number +=1

    def fullname(self):
        return  '{} {} '.format(self.first,self.last)

    def applyraise(self):
        self.pay = int(self.pay *self.raise_amount)

emp1 = Employee('corey','teacher',50000)
print(Employee.noOFEmployees)
emp2 =Employee('corey','teacher',50000)
print(Employee.noOFEmployees)
print(Employee.number)



'''
print(emp1.pay)
emp1.applyraise()
print(emp1.pay)
print(Employee.raise_amount)
#Employee.applyraise(self)
print(emp1.applyraise())
print(emp1.__dict__)
print(Employee.__dict__)#it will include the instances variable 
'''
'''
Employee.raise_amount =1.05
print(Employee.raise_amount)
print(emp1.raise_amount) #here the value will change both for the class aswell as for Instamces
#vice-versa will not work
emp1.raise_amount =14 #it will changed only for the instances not at the class level
print(emp1.__dict__)#emp1 has name space withIN its own namespace and returns its value

print(Employee.raise_amount)
print(emp1.raise_amount)
'''

