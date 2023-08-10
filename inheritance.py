#using normal inheritance
""" class Company:
    def __init__(self):
        self.name ='NITDA'

class Staff(Company):
    def staff_name(self, name):
        return f'{name} is the staff name.'
    
    def staff_salary(self, salary):
        return f'{salary} is the staff salary'
    
aisha = Staff()
print(aisha.staff_salary('5000000'))
print(aisha.name)

#inheritance using super
class Company:
    def __init__(self, name, section):
        self.name = name
        self.section = section

class Staff(Company):
    def __init__(self, name, section):
        super().__init__(name, section)
staff1 = Staff('Aisha', 'IT Department')
print(staff1.section) """

#using the class name
""" class Company:
    def __init__(self, name, section):
        self.name = name
        self.section = section
class Staff(Company):
    def __init__(self, name, section):
        Company.__init__(self, name, section)
staff1 = Staff('Aisha','IT department')
print(staff1.section)  """ 

#Classwork
""" class Mylist:
    def __init__(self, data):
        self.data = [1,2,3,4,5,6]
    def getItems (self, index):
        return self.data[index]
    def getSlice(self, start, end):
        return self.data[start:end]
a = Mylist([1,2,3,4,5,6])
a.data
print(a.getItems(2))
print(a.getSlice(2,4)) """

#Classwork 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return f'{int(self.width * self.height)} is the area'
    def get_perimeter(self):
        return f'{int(self.width**2 + self.height**2)} is the perimeter'
    def is_square(self):
        return self.width == self.height

        
r = Rectangle(2,3)
print(r.get_area())
print(r.get_perimeter())
print(r.is_square())
    