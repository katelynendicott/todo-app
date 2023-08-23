import functions
import time

now = time.strftime("%b %d, %Y %I:%M:%S %p")
print("It is ", now)
while True:
    # get user input, strip space chars and convert to lowercase
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    user_action = user_action.lower()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid. "
                  "\nPlease enter a todo number")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"The todo, {todo_to_remove}, was removed from the list."
            print(message)
        except IndexError:
            print('There is no item with that number. Please try again.')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")
print('bye!')
