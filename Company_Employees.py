class Employee: 
    
    def __init__(self, firstName, lastName, age, address, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.address = address 
        self.pay = pay
    
    @property
    def email(self):
        return '{}.{}@Company.com.do'.format(self.firstName, self.lastName)
    
    #@property
    #def fullname (self):
    #    return '{} {}'.format(self.firstName, self.lastName)

    #def __repr__(self):
    #    return "Employee('{}','{}','{}')".format(self.firstName, self.lastName, self.pay)