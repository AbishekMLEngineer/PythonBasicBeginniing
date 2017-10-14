# class regular and  static methods
# regular methods takes instance as the default argument i.e self now to take make it to take
# class as the default argument We can use @classmethod
import  datetime
class Employee:
    raise_amount = 1.04
    noOFEmployees = 0
    amount = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


'''
    @staticmethod
    def isworkDay(day):
        pass
   '''

''' 
   # @ClassMethods  can also be used as the alternatives constructors
    @classmethod
    def fromString(cls, emp_Str):
        first, last, pay = emp_Str.split('-')
        return  cls(first, last, pay)

empstr = 'Jhon-Don-19955'
newEmp23 = Employee.fromString(empstr)
print(newEmp23.first)
    '''

'''
    @classmethod 
    def setraiseAmt(cls, amount):
        cls.raise_amount = amount
        return cls.raise_amount
emp1 = Employee('corey', 'teacher', 50000)
Employee.setraiseAmt(1.05)
print(Employee.raise_amount)
st =    Employee.setraiseAmt(8888)
print(st)
'''
'''
empstr1= 'jon -doe-400000'
first ,last,pay = empstr1.split('-')
newEmp = Employee(first,last,pay)
print(newEmp.pay)
'''







