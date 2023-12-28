while True:
    user_action = input("Type add,show,edit,complete,exit :-")
    user_action = user_action.strip()


    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file: #read files
            todos = file.readlines()

        todos.append(todo )

        with open('todos.txt', 'w') as file:  # save the new todos to the file
            file.writelines(todos)
    elif user_action.startswith('show'):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index}-{item}"
            print(row)


    elif 'edit' in user_action:

        with open('todos.txt', 'r') as file: #read files
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index}-{item}"
            print(row)
        edit_num = int(input("Enter number -"))

        replaced_todos = input("enter new todo")
        todos[edit_num] = replaced_todos + '\n'

        with  open('todos.txt', 'w') as file: # save the new todos to the file
            file.writelines(todos)

    elif user_action.startswith('complete'):
        try:
            with open('todos.txt', 'r') as file: #read files
                todos = file.readlines()

            for index, item in enumerate(todos):
                row = f"{index}-{item}"
                print(row)
            pop_num = int(input("which one is complete:- "))
            todos.pop(pop_num)

            with  open('todos.txt', 'w') as file: # save the new todos to the file
                file.writelines(todos)
        except IndexError:
            print("No item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not found")


print("Bye Bye")
