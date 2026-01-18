# to - do list app File based
import json

TO_DO_LIST = "to_do_list.json"

class FileMissingError(Exception):pass
class LoadingError(Exception):pass
class TaskError(Exception):pass

def taskFields(id,title,description,status):
    return {
        "id": id,
        "title":title,
        "description" : description,
        "status" : status
    }

def createToDoList(toDoTask):
    with open(TO_DO_LIST, "w") as toDOList:
            json.dump([toDoTask], toDOList)

def UniqueIdCheck(fromTasks, new_id):
    for id in fromTasks:
        if id["id"] != new_id:
            return True
    return False

def addTask(Tasks,toDoTask, toDoList):

    if not UniqueIdCheck(Tasks, toDoTask["id"]):
        print("Please use a unique id")
        return  Tasks
        
    Tasks.append(toDoTask)

    toDoList.seek(0)
    json.dump(Tasks,toDoList,indent=4)
    toDoList.truncate()

    print("New Task Added")

    return Tasks
       
            
def UpdateTask(idTask): 
    with open(TO_DO_LIST, "r+") as toDoList:
        loadList = json.load(toDoList)

        update = int(input("What you want you update? Enter 1 for title, 2 for description & 3 for status : "))

        for id in loadList:
            if id["id"]==idTask:
                print("Found id")
                break

        if update==1:
                print(f"The title is ; {id["title"]}")
                updateTitle = input("Enter new title ; ")
                id["title"] = updateTitle
        elif update==2:
                print(f"The description is ; {id["description"]}")
                updateDesc = input("Enter new description ; ")
                id["description"] = updateDesc
        elif update==3:
                print(f"The status is ; {id["status"]}")
                updateStatus = input("Enter new title ; ")
                id["status"] = updateStatus
        else:
                print("please choose from option only!")
            
            
        toDoList.seek(0)
        json.dump(loadList, toDoList, indent=4)
        toDoList.truncate()

        print("Task Updated", loadList)

        return toDoList            
   
def seeToDoList(toDoTask):
    try:
        with open(TO_DO_LIST, "r+")  as toDoList:
            try:
                Tasks = json.load(toDoList)
                try:   
                    addTask(Tasks,toDoTask, toDoList)
                except:
                    raise TaskError("Error in adding task")
            except json.JSONDecodeError:
                raise LoadingError("Error in reading the tasks")
    except FileNotFoundError:
        createToDoList(toDoTask)

def delete(taskId): 
    with open(TO_DO_LIST, "r+") as toDoList:
        Tasks = json.load(toDoList)
        for id in Tasks:
            if id["id"]==taskId:
                print("Found id")
                break            
        
        Tasks.remove(id)
        toDoList.seek(0)
        json.dump(Tasks, toDoList, indent=4)
        toDoList.truncate()

        print("Task Deleted Check new list", Tasks)

        return toDoList

def seeTaskList():
    try:
        with open(TO_DO_LIST, "r") as toDoList:
            loadTaskList = json.load(toDoList)
            print(loadTaskList)
    except FileNotFoundError:
        print("File not exist")

def searchForATask(taskId):
    with open(TO_DO_LIST, "r") as toDoList:
        loadTaskList = json.load(toDoList)
        for id in loadTaskList:
            if id["id"] == taskId:
                print(f"This was the task {id}")
                break

def toDoList():
    operation = int(input("Enter what you want to do Choose number :\n1. Add\n2. Update a Task\n3. Delete Task\n4. Search For a task\n5. See all the tasks\n : "))
    if operation==1:
        id = int(input("Unique Id : "))
        title = input("Title : ")
        desc = input("Description : ")
        status = input("Status :  ")
        task = taskFields(id, title, desc, status)
        seeToDoList(task)
    elif operation==2:
        id = int(input("Please enter it's Unique Id for which you want to edit/update : "))
        UpdateTask(id)
    elif operation==3:
        id = int(input("Please enter it's Unique Id for deleting task : "))
        delete(id)
    elif operation==4:
        id = int(input("Please enter it's Unique Id for search: "))
        searchForATask(id)
    elif operation ==5:
        print("Here is all the task : ")
        seeTaskList()
    else:
        print("Any other operation? Please suggest we'll add or create functionality for it!")

toDoList()

# TO-DO :

# 1. what if the task id is not there for update & delete
# 2. Search strong - based on title/desc/status
# 3. Status (enum value)
# 4. All kind of error handling