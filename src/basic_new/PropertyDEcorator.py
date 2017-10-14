class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        self.mix=first+last

    @property
    def email(self):
        return '{}'.format(self.mix)
    @property
    def fullname(self):
        return  '{} {} awneyyy hii'.format(self.first,self.last)

    @fullname.setter
    def setEmail(self,name):
        first,last= name.split('')
        self.first =first
        self.last=last


emp1 =Employee('john','schafer')
print(emp1.fullname)
##definig the method and accessing  like an attribute  is Decoartor
print(emp1.mix)

print(emp1.first,end='         ')
print(emp1.last)



