import json


FILE = "StudentGrade.json"

class MarksException(Exception): pass
class NameValidationError(Exception):pass
class FileMissing(Exception):pass
class JsonLoadError(Exception): pass
class AddStudentError(Exception): pass

def validate_marks(marks):
    try: 
        mark = int(marks)
        if 0 <= mark <=100:
            return mark
        else:
            raise MarksException("Marks must be between 0-100")
    except ValueError:
        raise MarksException("Enter Number only")
    
def validate_name(name):
    if name.isalpha():
        return name
    else:
        raise NameValidationError("Name is invalid")

def grade(marks:int):
    if validate_marks(marks):
        if 90 <= marks:
            return "A"
        elif 75 <= marks <= 89:
            return "B"
        elif 50 <= marks <= 74:
            return "C"
        elif marks < 50:
            return "F"
    else:
        print("Enter Valid Marks")

def student(name,marks):
    return {"name": validate_name(name), "marks" : validate_marks(marks), "grade" : grade(marks)}

def create_file(student):
    with open(FILE,"w") as file:
            create = json.dump([student],file,indent=2)
            return create

def add_student(read_data,student,file):
        read_data.append(student)
        file.seek(0)
        json.dump(read_data,file,indent=2)
        file.truncate()
    
def read(student):
    try:
        with open(FILE, "r") as file:
            try:
                read_data = json.load(file)
                try:
                    with open(FILE, "w") as file:
                        add_student(read_data,student,file)
                except:
                    raise AddStudentError("Error in adding data!")
            except json.JSONDecodeError:
                raise JsonLoadError("Error in loading Json File")
    except FileNotFoundError:
        create_file(student)

def read_all():
    try:
        with open(FILE, "r") as file:
            try:
                read_data = json.load(file)
                return read_data
            except json.JSONDecodeError:
                raise JsonLoadError("Error in loading Json File")
    except FileNotFoundError:
        raise FileMissing("File with this name doen't exist")

def studentgrade(name,marks):
    students = student(name,marks)
    read(students)
    print(read_all())
    
studentgrade("Pranjal",50)