class ToDoList:
    def __init__(self):
        self.storetasks = []
        self.completed_task = []
    
    def add_task(self, task):
        self.storetasks.append(task)
        print('Task added successfully!')

    def complete_task(self, index):
        if len(self.storetasks) == 0:
            print('No task added.')
        else:
            self.completed_task.append(self.storetasks[index])
        

    def display_task(self):
        if len(self.storetasks) == 0:
            print('This is no task added.')
        else:
            for id, task in enumerate(self.storetasks, 1):
                badge = '[]'
                if task in self.completed_task:
                   badge = '[x]'
                print(f'{id}. {badge} {task}')



def main():

    toDo = ToDoList()

    while True:

        print('\nWelcome to the Simple To Do List!')
        print('1. Add a new task.')
        print('2. Mark a task as completed.')
        print('3. Display Tasks.')
        print('4. Exit.')

        option = input('Please enter your choice: ')

        if option == '1':
            desired_task = input('Enter task description: ')
            toDo.add_task(desired_task)
        elif option == '2':
            index = int(input('Enter task index to mark as completed: '))
            toDo.complete_task(index)
        elif option == '3':
            toDo.display_task() 
        elif option == '4':
            print('Thank you for using the Simple ToDo List. Goodbye!')
            break
        else:
            print('Invalid option, Please select a valid option.')

main()