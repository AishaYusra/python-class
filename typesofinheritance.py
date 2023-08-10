""" #multilevel inheritance
class Staff:
    def staff_profile(self):
        print('Works in accounting')

class Manager(Staff):
    def manager_profile(self):
        print('Manages staff relations')

class Ceo(Manager):
    def profile(self):
        print('CEO of the company')

john = Ceo()
john.manager_profile()

#hierarchical inheritance
class Company:
    def __init__(self):
        self.company = 'FIRS'
    def about_company(self):
        print('This is the Federal Inland Revenue Service')

class Staff1(Company):
    def staff1_details(self):
        print('This is Angela')

class Staff2(Company):
    def staff2_details(self):
        print('This is Aisha')

class Staff3(Company):
    def staff3_details(self):
        print('This is Ahmad')

c = Staff3()
c.staff3_details()

#hybrid inheritance

        
class Company:
    def __init__(self) -> None:
        self.company = 'FIRS'
    def about_company(self):
        print('This is the Federal Inland Revenue Service')

class Engineering(Company):
    def staff1_details(self):
        print('This is Civil Engineering')

class Accounting(Company):
    def staff2_details(self):
        print('This is Accounting dept.')

class Manager(Engineering, Accounting):
    def manager_details(self):
        print('Manages the departments')

p = Engineering()
p.about_company() """

#classwork

class Grandparent:
    def about_grandparent(self):
        print('Radiya and Aisha are my grandmothers.')

class Parent(Grandparent):
    def about_parent(self):
        print('Hauwa is my mother.')

class Child(Parent):
    def about_child(self):
        print('I was named after one of my grandmothers.')

t = Child()
t.about_parent()
y = Parent()
y.about_grandparent()
me = Child()
me.about_child()


class Employee:
    def __init__(self) -> None:
        self.name = 'Aisha Shafii'
        self._age = 23
        self.__course = 'Computer Science'
        

    def profile(self):
        print(self.__course)
# def _profile = protected
#def __profile = private
e = Employee()
e.profile()
print(e._Employee__course)




    



        