def app():
    task=[]
    print("---Welcome to Task Managemnet App")


    total_task=int(input("How many tasks you want to add: "))
    for i in range(1,total_task+1):
      task_name=input(f"Add task{i}")
      task.append(task_name)
      print(f"Today's tasks are\n{task_name}")
#Main operation
    while True:
       operation=input("Enter value:\n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit")

#Adding Task
    if operation==1:
      add=input("Enter a new task to add:")
      task.append(add)
      print(f"Task{add}has been successfully addes...")
#update Task
    elif operation==2:
     update_val=input("Task you want to update: ")
     if update_val in task:
       up=input("Enter new task: ")
       update=task.index(update_val)
       tasks[update]=up
       print(f"Updated task{up}")
      
#Delete Task
    elif operation==3:
       delete_val=input("Task you want to update: ")
       if  delete_val in task:
        up=input("Enter new task: ")
        delete=task.index(delete_val)
        tasks[delete]=up
        print(f"Task{delete} has been deleted...")

#exit
    elif operation==4:
        print("Closing the App...")