# def check_users_age(value):
#     assert value > 18, 'Value Should be greater than 18'
#     print('Welcome')
# check_users_age(17)
#you'll get an assertion error if you insert a number less than 18.

# def check_name_age(name, age):
#     assert (name != 'John') & (age > 18), 'Name must be John and age greater than 18.'
#     print(name, age)
# check_name_age('John',17)
#if you use 'John' and an age less than 18 , you get an assertion error.

#TryExcept can be used to handle exceptions.
# try:
#     result = 10/0
# except Exception:
#     print('You should not have done that')
# else:
#     print('Successful')


# try:
#    def cel_to_fah(temp):
#       assert temp >= 0
#       result = (temp * (9/5)) + 32
#       print(result)
#       with open('demo.txt', 'w') as anything:
#          anything.write(str(result))
#    cel_to_fah(20)
# except AssertionError:
#    print('Please enter a temperature greater than zero.')

# try:
#    try:
#       print('Hello World')
#    finally: #you can have try without except using finally but not the other way round
#          print('Hello World')
# except Exception:
#       print('You had an error')
# finally:
#       print('Successful')

#raise an exception(raise can raise any type of error)

# def convert_cel_to_fah(temp):
#     if temp < 0:
#        raise Exception
#     return(temp * (9/5)) + 32
# convert_cel_to_fah(-20)

#user-defined exceptions
# class CelsiusError(Exception):
#     def __init__(self, *args: object) -> None:
#         super().__init__(*args)

# def convert_cel_to_fah(temp):
#     if temp < 0:
#        raise CelsiusError
#     return(temp * (9/5)) + 32

# try:
#     convert_cel_to_fah(-20)
# except CelsiusError:
#     print('Wrong option')


# def kelv_to_fah(temp):
#     assert temp >= 0, 'Colder than absolute Zero'
#     result = (temp-273.15)* 9/5 + 32
#     print(result)
# kelv_to_fah(20)

# def get_age(age):
#     if age < 10:
#         raise ValueError
#     print(age)

# get_age(15)

# def KelvinToFarenheit(temp):
#     assert temp >= 0,'Colder that absolute Zero'
#     value = (temp-273.15)*9/5 + 32
#     print(value)

# KelvinToFarenheit(5)



        
