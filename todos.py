user_prompt = "Enter a to-do (or type 'done' to finish): "
todos = []

while True:
    todo = input(user_prompt)
    
    # Check if the user wants to stop
    if todo.lower() == 'done':
        break
    
    # Optional: Validate input to prevent empty to-dos
    if todo.strip():
        todos.append(todo)
    else:
        print("To-do cannot be empty. Please enter a valid task.")

# Print the final list of to-dos
print("Your to-do list:", todos)
