""" class Parent:
    def genotype(self):
        print('AS')

    def blood_group(self):
        print('O-')

class Child(Parent):
    def genotype(self):
        print('AA')
        Parent.genotype(self)

aisha = Child()
aisha.genotype()
aisha.blood_group() """


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self, salary):
        return self.salary
    
class Manager(Employee):
    def bonus_one(self):
        self.salary = self.salary * 0.1
        
class Engineer(Employee):
    def bonus_one(self):
        self.salary = self.salary * 0.05

