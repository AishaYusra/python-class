""" class person:
    def __init__(self):
        print('Welcome')
        self.name = 'Yusrah'
        self.age = 19
    def walking(self):
        print('Walking')
    
a = person()
a.walking()
print(a.name)
print(a.age)
 """

#Assessment-three
""" numbers = [4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 20, 22]
n = 4
def largest_divisible(n,lst):
    #In list comprehension
    return [i for i in numbers if i % n == 0]
print(max(largest_divisible(n,numbers))) """

""" lst = []
    for i in numbers:
        if i%n == 0:
            lst.append(i)
    return max(lst) """
""" print(largest_divisible(n,numbers)) """

""" class person:
    def __init__(self, name):
        print(f'Welcome, {name}')

    def occupation(self):
        print('Interior Designer')

a = person('Aisha')
a.occupation() """

class Dog:
    def __init__(self):
        self.name = 'Luna'
        self.breed = 'French Bulldog' 
        self.colour = 'White'
    def barking(self):
        print(f'{self.name}, the {self.breed} {self.colour} is barking!')
        print('Luna, the white French bulldog is barking!')
aa = Dog()
aa.barking()

    

