todos = []
while True:
    user_action = input("Enter to add ,show or exit: ")
    match user_action:
        case "add":
            todo = input("Enter a To do:")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
print("bye!")
