# STUDENT RECORDS ASSIGNMENT

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = (grade)

class StudentRecordSystem:
    def __init__(self):
        self.students = []

    def add_students(self, name, age, grade):
        student_info = Student(name, age, grade)
        self.students.append(student_info)
        print('Student Added Successfully!')

    def display_all_students(self):
        if len(self.students) == 0:
            print('No student was added.')
        else:
            for student in self.students:
                print('--Student Information--')
                print('Name:', student.name)
                print('Age:', student.age)
                print('Grade:', student.grade)

    def save_records(self, filename):
        with open('filename.txt', 'w') as file:
            for student in self.students:
                file.write(f'--Student Information--\n Name: {student.name}\n Age: {student.age}\n Grade: {student.grade}\n')
            print("Records have been added to 'filname.txt' successfully. Please open the file to view.")

    def load_records(self, filename):
        f = open('filename.txt', 'r')
        content = f.read()
        print(content)
        print('Records have been loaded successfully.')

records = StudentRecordSystem()
       
while True:
    print('\nWelcome to the Student Record System!')
    print('1. Add a new Student Record.')
    print('2. Display Student Records')
    print('3. Save Students Records.')
    print('4. Load Students Records.')
    print('5. Exit')

    option = input('What you would like to do: ')

    if option == '1':
        another='Yes'
        while another.lower() == 'yes':
            name = input('Enter Student Name: ')
            age = input('Enter Student Age: ')
            grade = input('Enter Student Grade: ')
            records.add_students(name, int(age), grade)
            another = input('Would you like to add another Student Record? Yes/No: ')
    
            
    elif option == '2':
        records.display_all_students()
    elif option == '3':
        records.save_records('filename.txt')
    elif option == '4':
        records.load_records('filename.txt')
    elif option == '5':
        break
    else:
        print('Please enter a valid option.\n')

