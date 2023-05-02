list = []

while True:
    try:
        todo = input("Enter your todo's: ")
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    if 'remove' in todo:
       todo = todo.replace('remove', '')
       todo = todo.strip()
       list.remove(todo)
       print('Todo:', list)
    elif todo == 'end':
            break
    else:
        list.append(todo)
        print('Todo:', list)