import self as self


class Employee:
    raise_amount = 1.04
    noOFEmployees = 0
    number = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.noOFEmployees += 1
        self.number += 1

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

    def applyraise(self):
        self.pay = int(self.pay * self.raise_amount)

'''
emp1 = Employee('corey', 'teacher', 50000)
print(Employee.noOFEmployees)
emp2 = Employee('corey', 'teacher', 50000)
print(Employee.noOFEmployees)
print(Employee.number)
'''

class Developer(Employee):
    raise_amount = 2.0555
    language ='abi'

    def __init__(self,first,last,pay,language):
        super().__init__(first,last,pay)
        self.language =language

dev1= Employee('corey','schafer',40000)
dev2= Developer('test','testEnd',60000,'java')

print(dev1.pay)
dev1.applyraise()
print(dev1.pay)
print(dev1.first)
print(dev2.language)
#now if we have a raise amount variable in the sub-class then its gonna print that
#and this is not gonna effect the instances of the superclass



'''
print(dev1.first)#it 1st looks for the init methods which is not gonna found over here
#then it founds the chain of inheritance which is called Method resolutionzer
#and then it looks for it in the superclass
#checking the method resolutionzer is the 1st class which gets printed out
print(help(Developer))
'''



class Manager(Employee):
    e1 = Employee('fir','las',30000)

    def __init__(self,first,last,pay,emples=None):
        super().__init__(first,last,pay)
        if emples is None:
            self.emples =[]
        else:
            self.emples= emples

    def addemples(self,emp):
        if emp not in self.emples:
            self.emples.append(emp)

    def removeemples(self,emp):
        if emp in self.emples:
            self.emples.remove(emp)

    def printemples(self):
        for emp in self.emples:
            print('-- Emp - >')

dev1= Employee('corey','schafer',40000)
dev2= Developer('test','testEnd',60000,'java')

mgr1 = Manager('SS','SMI',90000,'[]dev1')#it manages the class of developers
print(mgr1.first)
mgr1.addemples(dev2)
mgr1.printemples()

print(isinstance(mgr1,Manager))#will tell if mgr is instances of Manager
